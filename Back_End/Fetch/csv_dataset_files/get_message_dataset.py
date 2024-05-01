from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import asyncio
import logging
import re
from utils import get_channel_ids 
import csv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('anon', api_id, api_hash)

async def main():

    await client.start()
    
    channel_usernames = ['@gocareers', '@fresheroffcampus', '@goyalarsh', '@job4fresherss', '@opportunitycellofficial', '@offcampusdrive_it', '@placementkit', '@prepflix', '@engineerjobsindia', '@oflatestblog']
    channel_ids = await get_channel_ids(channel_usernames, client=client)
    filename = 'csv_dataset_files/sample_100.csv'
    pattern = '.*(hiring|placement|role|eligibility|training|Internship).*'
    pattern = re.compile(pattern, flags=re.IGNORECASE | re.DOTALL)

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        i = 0
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Channel', 'Message'])
        for channel_id in channel_ids:  
            i = i+1
            j = 1
            async for message in client.iter_messages(channel_id, reverse=True, limit=100):
                if message.text and pattern.search(message.text):
                    print(i, j)
                    j = j+1
                    csv_writer.writerow([channel_id, re.sub(r'[^\x00-\x7F]', '', message.text)])

    await client.run_until_disconnected()


asyncio.run(main())