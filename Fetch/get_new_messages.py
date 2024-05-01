# import os
# import asyncio
# import logging
# from telethon import TelegramClient, events
# from dotenv import load_dotenv
# from utils import get_channel_ids 
# from entity_handler import extract_entities, insert_entities, connect_to_database, create_entities_table, extract_batches
# from telethon import functions, types
# import re

# # Function to extract "APPLY LINK" using regex
# def extract_apply_link(text):
#     # Regular expression pattern to match URLs
#     url_pattern = r'(https?://\S+)'
#     matches = re.findall(url_pattern, text)
#     if matches:
#         return matches[0]  # Return the first URL found in the text
#     else:
#         return None  # Return None if no URL is found
    
# async def main():
#     load_dotenv()
#     mydb = connect_to_database()
#     print("DB ID: ", mydb.connection_id)
#     create_entities_table(mydb)

#     async with TelegramClient('fetch-updated-messages-v1', os.getenv('API_ID'), os.getenv('API_HASH'), loop=asyncio.get_event_loop()) as client:
#         await client.start()
#         channel_usernames = ['@hello56576', '@gocareers', '@fresheroffcampus', '@goyalarsh', '@job4fresherss', '@opportunitycellofficial', '@offcampusdrive_it', '@placementkit', '@prepflix', '@engineerjobsindia', '@oflatestblog']
#         channel_ids = await get_channel_ids(channel_usernames, client=client)

#         @client.on(events.NewMessage(from_users=channel_ids))
#         async def handle_hiring(event):
#             if event.message.text:
#                 text_message = event.message.text.replace('\xa0', ' ').strip()
                
#                 entities = extract_entities(text_message)
#                 if 'APPLY LINK' in entities:
#                     # If "APPLY LINK" is found in entities, use it directly
#                     apply_link = entities['APPLY LINK']
#                 else:
#                     # If "APPLY LINK" is not found, extract it using regex
#                     apply_link = extract_apply_link(text_message)
                
#                 if apply_link:
#                     if 'BATCH' in entities:
#                         batches = extract_batches(entities['BATCH'])
#                         # print("Extracted Batches: ", batches)
#                         if batches:
#                             for batch in batches:
#                                 batch_entities = entities.copy()
#                                 batch_entities['BATCH'] = batch
#                                 if apply_link:
#                                     insert_entities(batch_entities, mydb)
#                                     print(batch_entities)
#                         else:
#                             insert_entities(entities, mydb)
#                     else:
#                         batch = 'N/A'
#                         entities['BATCH'] = batch
#                         insert_entities(entities, mydb)
                        
                    
#         await client.run_until_disconnected()
        
        

# if __name__ == "__main__":
#     logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
#                         level=logging.WARNING)
#     asyncio.run(main())



import os
import asyncio
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv
from utils import get_channel_ids 
from entity_handler import extract_entities, insert_entities, connect_to_database, create_entities_table, extract_batches
from telethon import functions, types
import re

# Function to extract "APPLY LINK" using regex
def extract_apply_link(text):
    # Regular expression pattern to match URLs
    url_pattern = r'(https?://\S+)'
    matches = re.findall(url_pattern, text)
    if matches:
        return matches[0]  # Return the first URL found in the text
    else:
        return None  # Return None if no URL is found
    
async def main():
    load_dotenv()
    mydb = connect_to_database()
    print("DB ID: ", mydb.connection_id)
    create_entities_table(mydb)

    async with TelegramClient('fetch-updated-messages-v1', os.getenv('API_ID'), os.getenv('API_HASH'), loop=asyncio.get_event_loop()) as client:
        await client.start()
        channel_usernames = ['@hello56576', '@gocareers', '@fresheroffcampus', '@goyalarsh', '@job4fresherss', '@opportunitycellofficial', '@offcampusdrive_it', '@placementkit', '@prepflix', '@engineerjobsindia', '@oflatestblog']
        channel_ids = await get_channel_ids(channel_usernames, client=client)

        @client.on(events.NewMessage(from_users=channel_ids))
        async def handle_hiring(event):
            if event.message.text:
                text_message = event.message.text.replace('\xa0', ' ').strip()
                
                entities = extract_entities(text_message)
                if 'APPLY LINK' in entities:
                    # If "APPLY LINK" is found in entities, use it directly
                    apply_link = entities['APPLY LINK']
                else:
                    # If "APPLY LINK" is not found, extract it using regex
                    apply_link = extract_apply_link(text_message)
                
                if apply_link:
                    print(apply_link)
                    if 'BATCH' in entities:
                        batches = extract_batches(entities['BATCH'])
                        if batches:
                            print('We have batches')
                            for batch in batches:
                                batch_entities = entities.copy()
                                batch_entities['BATCH'] = batch
                                batch_entities['APPLY LINK'] = apply_link
                                if apply_link:
                                    insert_entities(batch_entities, mydb)
                                    print(batch_entities)
                        else:
                            batch_entities['APPLY LINK'] = apply_link
                            insert_entities(batch_entities, mydb)
                    else:
                        batch = 'N/A'
                        entities['BATCH'] = batch
                        entities['APPLY LINK'] = apply_link
                        insert_entities(entities, mydb)
                        
                    
        await client.run_until_disconnected()
        
        

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                        level=logging.WARNING)
    asyncio.run(main())
