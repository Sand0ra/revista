import os
import asyncio

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'revista.settings'

django.setup()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "revista.settings"
)

django.setup()

from bot.bots_init import init_telegram_clients

async def work(client):
    async with client:
        me = await client.get_me()
        print(me)


async def main():
    clients = await init_telegram_clients()
    client_coros = [work(client) for client in clients]

    await asyncio.gather(
        *client_coros
    )

asyncio.run(main())
