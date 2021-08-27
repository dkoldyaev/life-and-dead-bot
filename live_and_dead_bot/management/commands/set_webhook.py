from django.core.management.base import BaseCommand, CommandError

from api.api import api_request
from live_and_dead_bot.models import BotData


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser\
            .add_argument(
                '--host',
                action='store',
                required=False,
                help='Хост для бота'
            )

        parser\
            .add_argument(
                '--token',
                action='store',
                required=False,
                help='Токен'
            )

    def handle(self, *args, **options):

        try:
            boot_data = BotData.objects.get()
        except BotData.DoesNotExist as e:
            boot_data = BotData()

        if options.get('host', None) :
            boot_data.host = options.get('host')

        if options.get('token', None) :
            boot_data.token = options.get('token')

        if not boot_data.host or not boot_data.token :
            raise CommandError('Укажите домен для бота и токен')

        boot_data.save()

        api_request(
            'get',
            'setWebhook',
            {
                'url': boot_data.host
            }
        )




