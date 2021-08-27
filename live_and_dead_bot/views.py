import json, re

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from django.conf import settings

from live_and_dead_bot import actions as actions_module
from api.api import api_request
from live_and_dead_bot.utils import get_action, delete_message


@method_decorator(csrf_exempt, name='dispatch')
class MessageView(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message', None)
        callback_data = data.get('callback_query', None)
        chat_id = None
        delete_message_params = None
        response = None
        if not message and not callback_data:
            return HttpResponse('ok', status=200)

        try:
            chat_id = (message and message['chat']['id']) or callback_data['message']['chat']['id']
            if callback_data:
                callback_data = json.loads(callback_data['data'])
                (callback_action_name, callback_params) = (callback_data['action'], callback_data['data'])
                callback = getattr(actions_module, f'{callback_action_name}_callback')
                if not callable(callback):
                    raise Exception('Нет такого коллбэка')

                (method, request) = callback(chat_id, callback_params)

            elif message:
                text = (message and message['text']) or callback_data['data']
                message_parse = re.match(r'/(?P<action_name>[\w]+)?', text)
                possible_action = get_action(text)
                if possible_action:
                    action = possible_action
                    delete_message_params = [chat_id, message['message_id']]
                elif message_parse:
                    action = getattr(actions_module, '{0}_message'.format(message_parse.group('action_name')))
                    if not callable(action):
                        raise Exception('Нет такой команды')
                else:
                    raise Exception('Не могу распарсить сообщение')

                (method, request) = action(chat_id, message)

            else:
                raise Exception('Я умею принимать только команды из списка /help')

            response = api_request(
                'post',
                method,
                request
            )

        except Exception as e:
            if settings.DEBUG and chat_id :
                (method, request) = (
                    'sendMessage',
                    {
                        'chat_id': chat_id,
                        'text': e.__str__()
                    }
                )

                response = api_request(
                    'post',
                    method,
                    request
                )

        if response and response.json()['ok'] and delete_message_params:
            delete_message(*delete_message_params)

        return HttpResponse('ok', status=200)
