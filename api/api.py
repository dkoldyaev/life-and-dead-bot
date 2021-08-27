from urllib.parse import urlencode
from django.conf import settings

import requests
from requests import Response

from live_and_dead_bot.models import BotData

def api_request(method: str, action: str, data: dict, ) -> Response:

    try:
        bot_data = BotData.objects.get()
    except BotData.DoesNotExist as e:
        bot_data = BotData()

    url = '{bot_host}{action}'.format(
        bot_host=settings.BOT_URL % bot_data.token,
        action=action
    )
    if method == 'get' :
        url += '?'+urlencode(data)
        return requests.get(url)

    if method == 'post' :
        return requests.post(url, data=data)

    raise Exception('Неправильный метод')
