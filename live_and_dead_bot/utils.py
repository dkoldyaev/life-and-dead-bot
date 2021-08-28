import json
from inspect import getmembers, isfunction
from typing import List, Callable, Optional
from urllib.parse import urljoin

from api.api import api_request

def get_main_keyboard():
    from cards.models import MainMenuButtons
    keyboard = []
    current_row = None
    for button in MainMenuButtons.objects.all():
        if button.row != current_row:
            keyboard.append([])
            current_row = button.row
        keyboard[len(keyboard) - 1].append({
            'text': button.text
        })
    return keyboard

def get_callback_actions():
    from live_and_dead_bot import actions as actions_module
    actions: List[(str, Callable[[int], (str, dict)])] = list(filter(
        lambda action_tuple: '_callback' in action_tuple[0],
        getmembers(actions_module, isfunction)
    ))
    return list(map(
        lambda action_tuple: (action_tuple[0].replace('_callback', ''), action_tuple[1]),
        actions
    ))

def get_action(text: str):
    from cards.models import MainMenuButtons
    actions = get_callback_actions()
    try:    button: MainMenuButtons = MainMenuButtons.objects.get(text=text)
    except: return None
    for action_name, action in actions :
        if action_name == button.action :
            return action
    return None

def delete_message(chat_id: int, message_id: str) -> (str, dict):
    api_request(
        'post',
        'deleteMessage',
        {
            'chat_id': chat_id,
            'message_id': message_id
        }
    )

def post_message(
        chat_id: int,
        text: Optional[str] = None,
        photo: Optional[str] = None,
        sticker_id: Optional[str] = None,
        reply_markup: Optional[dict] = None
) -> (str, dict):
    from django.conf import settings

    if reply_markup is None :
        reply_markup = {'keyboard': get_main_keyboard()}

    action = None
    data = None

    if sticker_id :
        data = {
            **{
                'chat_id': chat_id,
                'sticker': sticker_id
            },
            **({'reply_markup': json.dumps(reply_markup)} if reply_markup else {})
        }
        action = 'sendSticker'

    elif photo :
        data = {
            **{
                'chat_id': chat_id,
                'caption': text,
                'photo': photo,
                'parse_mode': 'html',
                'caption_entities': ['bold', 'italic', 'strikethrough', 'pre'],
            },
            **({'reply_markup': json.dumps(reply_markup)} if reply_markup else {})
        }
        action = 'sendPhoto'

    else:
        data = {
                **{
                    'chat_id': chat_id,
                    'text': text,
                    'parse_mode': 'html',
                    'caption_entities': ['bold', 'italic', 'strikethrough', 'pre'],
                },
                **({'reply_markup': json.dumps(reply_markup)} if reply_markup else {})
            }
        action = 'sendMessage'

    if settings.DEBUG and action and data :
        debug_data = {
            "action": action,
            "data": data
        }
        api_request(
            'post',
            'sendMessage',
            {
                'chat_id': chat_id,
                'text': f'```\n'
                        f'{json.dumps(debug_data, sort_keys=True, indent=2, separators=(",", ": "))}'
                        f'\n````',
            }
        )

    if action and data :
        return (action, data)