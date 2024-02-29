from api import models

from telethon import TelegramClient


async def init_telegram_clients():
    organizations = models.Organization.objects.exclude(
        tg_api_hash='',
    ).exclude(
        tg_api_id=None,
    )

    clients = []
    async for organization in organizations:
        clients.append(
            TelegramClient(f'bot.{organization.id}', organization.tg_api_id, organization.tg_api_hash)
        )

    return clients
