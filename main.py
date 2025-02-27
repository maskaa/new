import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
from vk_api.utils import get_random_id

def write_msg(user_id, message):
    try:
        vk.method('messages.send', {'user_id': user_id, 'message': message['text'], 'keyboard': message['keyboard'], 'random_id': get_random_id()})
        user_url = "https://vk.com/id" + str(user_id)
        if 'find' in message:
            vk.method('messages.send', {'user_id': message['id'], 'message': 'Вас нашел этот человек '+'{}'.format(user_url), 'keyboard': None, 'random_id': get_random_id()})
    except:
        print('Some problems with server')
        return 0

token = ""

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

print("Server started")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}')
            print(event)
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event))
