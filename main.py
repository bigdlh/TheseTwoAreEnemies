#!/bin/env python
"""
Discord Bot
A shell for Disney Enemies
"""
import discord, os
from enemies import get_random_enemy
from dotenv import load_dotenv
load_dotenv()

class EnemyClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith('!enemies'):
            if len(message.content) > 9:
                await message.channel.send(get_random_enemy(message.content[9:]))
            else:
                await message.channel.send(get_random_enemy())

client = EnemyClient()
client.run(os.environ['DISCORD_TOKEN'])