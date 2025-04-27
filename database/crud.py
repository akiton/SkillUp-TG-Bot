from database.enumur import UserToAI

users = {}
messages={}

async def get_or_create_user(user_data: dict):
    user_id = int(user_data.get("id"))

    user = users.get("user_id")

    if not user:
        user_data = [user_data.get('username', ''),user_data.get('first_name', ''),user_data.get('last_name', '')]

        users[user_id] = user_data
    return user


async def save_message(user_id: int, text: str, message_type: UserToAI):
    user_id = int(user_id)
    messages = users.get("user_id")
    if messages:
        messages.append([user_id, text, message_type.value])


    users[user_id] = messages


async def get_user_history(user_id: int) -> list[tuple[UserToAI, str]]:
    msg = messages.get(user_id)
    if msg:
        return [(UserToAI(msg1.message_type), msg1.text) for msg1 in msg]
    else:
        return []