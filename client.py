import requests


URL= 'http://127.0.0.1:5000'


# # Проверка POST-запроса(Заполнение таблицы обьявлениями)
# response_0 = requests.post(f'{URL}/post/', json={'id': '1', 'heading': 'GET', 'description': 'Метод GET запрашивает представление ресурса.', 'user_name':'test1'})
# response_1 = requests.post(f'{URL}/post/', json={'id': '2', 'heading': 'HEAD', 'description': 'HEAD запрашивает ресурс так же, как и метод GET, но без тела ответа.', 'user_name':'test2'})
# response_2 = requests.post(f'{URL}/post/', json={'id': '3', 'heading': 'DELETE', 'description': 'DELETE удаляет указанный ресурс.', 'user_name':'test3'})
# response_3 = requests.post(f'{URL}/post/', json={'id': '4', 'heading': 'PATCH', 'description': 'PATCH используется для частичного изменения ресурса.', 'user_name':'test4'})
# response_4 = requests.post(f'{URL}/post/', json={'i': '5', 'heading': 'ошибка', 'description': 'Преднамеренная ошибка в id','user_name': 'test'})
#
# print(f'{response_0.json()},\n{response_1.json()},\n{response_2.json()},\n{response_3.json()},\n {response_4.json()}')



# Проверка GET-запроса
# response_5 = requests.get(f'{URL}/get?param=0')
# response_6 = requests.get(f'{URL}/get?param=2')
# response_7 = requests.get(f'{URL}/get?param=3')
# response_8 = requests.get(f'{URL}/get?param=4')
#
# print(f'{response_5.json()},\n{response_6.json()},\n{response_7.json()},\n{response_8.json()}')


# # Проверка DELETE-запроса
# response_9 = requests.delete(f'{URL}/delete?param=0')
# print(response_9.json())
