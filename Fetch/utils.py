async def get_channel_ids(usernames, client):
    channel_ids = []
    for username in usernames:
        try:
            entity = await client.get_entity(username)
            channel_id = int('-100' + str(entity.id))
            channel_ids.append(channel_id)
        except Exception as e:
            print(f"An error occurred for username '{username}': {e}")
    return channel_ids