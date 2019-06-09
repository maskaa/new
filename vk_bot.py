import bs4 as bs4
import requests
import json
from download_img import download_image_func, download_image_func_1
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from face_compare import open_files

class VkBot:
    def __init__(self, user_id):
        print("Bot created")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "РЕГИСТРАЦИЯ", "НАЙТИ ЧЕЛОВЕКА", "СПРАВКА"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, event):
        message = event.text
        
        if message.upper() == self._COMMANDS[0]:
            return {"find": False, "text": f"Привет, {self._USERNAME}!" + '\n' +  "Мои команды: " + '\n' +  "'Регистрация', " + '\n' +  "'Найти человека', " + '\n' +  "'Справка'", "keyboard": None}

        elif message.upper() == self._COMMANDS[1]:
            try:
                download_image_func(event.attachments['attach1'])
                return {"find": False, "text": "Спасибо)", "keyboard": None}
            except KeyError:
                return {"find": False, "text": "Нет фотографии", "keyboard": None}
            except ValueError:
                return {"find": False, "text": "Не могу получить доступ к фотографии", "keyboard": None}
            except IndexError:
                return {"find": False, "text": "Не могу найти лицо на фотографии", "keyboard": None}

        elif message.upper() == self._COMMANDS[2]:
            try:
                file = download_image_func_1(event.attachments['attach1'])
                url = open_files(file)
                id_user = url[17:]

                return {"find": True, "id":id_user, "text":'Мне кажется, это {}'.format(url), "keyboard": None}
            except KeyError:
                return {"find": False, "text": "Нет фотографии", "keyboard": None}
            except ValueError:
                return {"find": False, "text": "Не могу получить доступ к фотографии", "keyboard": None}
            except IndexError:
                return {"find": False, "text": "Не могу найти лицо на фотографии", "keyboard": None}

        elif message.upper() == self._COMMANDS[3]:
            return {"find": False, "text": "Для регистрации пришлите свою фотографию с командой 'Регистрация', фотография должна быть загружена в ВКонтакте, в любом альбоме кроме Сохраненных фотографий и приватных альбомов" + '\n' + "Для поиска фотографии пришлите фотографию человека, которого хотите найти и команду 'Найти человека'", "keyboard": None}


        else:
            return {"find": False, "text": "??????", "keyboard": None}

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
