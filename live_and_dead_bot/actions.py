import json
import random
from live_and_dead_bot.utils import post_message


def start_message(chart_id, message) -> (str, dict):
    from pages.models import Page
    page = Page.objects.get(command='start')
    return post_message(
        chart_id,
        page.text,
        page.image.url if page.image else None
    )


def help_message(chart_id, message) -> (str, dict):
    from pages.models import Page
    page = Page.objects.get(command='help')
    return post_message(
        chart_id,
        page.text,
        page.image.url if page.image else None
    )


def get_link_callback(chat_id, message) -> (str, dict):
    from random_messages.models import LinkRandomMessage, StickerRandomMessage
    try:
        message = LinkRandomMessage.objects.all().order_by('?')[:1].get()
    except:
        return post_message(
            chat_id,
            'Сообщений пока нету'
        )

    try:
        sticker = StickerRandomMessage.objects.all().order_by('?')[:1].get()
    except:
        return post_message(
            chat_id,
            'Стикеров пока нету'
        )

    response = random.choice([
        post_message(
            chat_id,
            message.link
        ),
        post_message(
            chat_id,
            None,
            None,
            sticker.sticker_id
        ),
    ])

    return response


def get_menu_callback(chat_id, message) -> (str, dict):
    from pages.models import Page
    from cards.models import CardButton
    keyboard = []
    current_row = None
    for card in CardButton.objects.all():
        if card.row != current_row:
            keyboard.append([])
            current_row = card.row
        keyboard[len(keyboard) - 1].append({
            'text': card.button_text,
            'callback_data': json.dumps({
                'data': {'card': card.id},
                'action': 'show_card'
            })
        })

    try:    menu_page: Page = Page.objects.get(command='menu')
    except: raise Exception('Не могу найти страницу menu')

    return post_message(
        chat_id,
        menu_page.text,
        menu_page.image.url if menu_page.image else None,
        None,
        {'inline_keyboard': keyboard}
    )


def get_about_callback(chat_id, message) -> (str, dict):
    from pages.models import Page
    from cards.models import AboutButton
    keyboard = []
    current_row = None
    for about in AboutButton.objects.all():
        if about.row != current_row:
            keyboard.append([])
            current_row = about.row
        keyboard[len(keyboard) - 1].append({
            'text': about.button_text,
            'callback_data': json.dumps({
                'data': {'about': about.id},
                'action': 'show_about'
            })
        })

    try:    menu_page: Page = Page.objects.get(command='about')
    except: raise Exception('Не могу найти страницу menu')

    return post_message(
        chat_id,
        menu_page.text,
        menu_page.image.url if menu_page.image else None,
        None,
        {'inline_keyboard': keyboard}
    )


def show_card_callback(chat_id, params: dict) -> (str, dict):
    from cards.models import CardButton
    try:
        card_id = params.get('card', None)
        card: CardButton = CardButton.objects.get(id=card_id)
    except:
        raise Exception('Не могу найти карточку')

    return post_message(
        chat_id,
        card.text,
        card.image.url if card.image else None
    )


def show_about_callback(chat_id, params: dict) -> (str, dict):
    from cards.models import AboutButton
    try:
        about_id = params.get('about', None)
        about: AboutButton = AboutButton.objects.get(id=about_id)
    except:
        raise Exception('Не могу найти страничку')

    return post_message(
        chat_id,
        about.text,
        about.image.url if about.image else None
    )


def get_map_callback(chat_id, params: dict) -> (str, dict):
    from pages.models import Page
    try:
        page: Page = Page.objects.get(command='map')
    except:
        raise Exception('Карты пока нет')

    return post_message(
        chat_id,
        page.text,
        page.image.url if page.image else None
    )
