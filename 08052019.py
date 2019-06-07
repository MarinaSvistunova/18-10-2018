# from collections import deque  # queue LIFO & FIFO
#
#
# # LIFO - Last in first out
#
# # FIFO - First in first out
#
# class MemorizingDict(dict):
#     history = deque(maxlen=10)
#
#     def set(self, key, value):
#         self.history.append(key)  # MemorizingDict.history
#         self[key] = value  # memDict = dict() memDict[key] = value
#
#     def get_history(self):
#         return self.history
#
#
# # print(MemorizingDict.__bases__)
# d = MemorizingDict()
# d.set("boo", 500100)  # 1
# print(d.get_history())
#
# d1 = MemorizingDict()
# d1.set("baz", 100500)  # 2
# print(d1.get_history())


# import functools
#
#
# def singleton(cls):
#     instance = None
#
#     @functools.wraps(cls)
#     def inner(*args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = cls(*args, **kwargs)
#         return instance
#
#     return inner
#
#
# @singleton
# class Connection:
#     pass
#
#
# print(Connection())
# print(id(Connection()))


# import warnings
# import functools
#
# def deprecated(cls):
#     orig_init = cls.__init__
#
#     @functools.wraps(cls.__init__)
#     def new_init(self, *args, **kwargs):
#         warnings.warn(cls.__name__ + " is deprecated", category=DeprecationWarning)
#         orig_init(self, *args, **kwargs)
#
#     cls.__init__ = new_init
#     return cls
#
#
# @deprecated
# class Counter:
#     def __init__(self, initial=0):
#         self.value = initial
#         print(initial)
#
#
# c = Counter(10)

# import requests  # основную работу выполняет библиотека requests
# import json  # модуль json необходим для парсинга данных, пришедших от веб-ресурса
# import pprint  # модуль, позволяющий организовывать форматирование в более визуально-приятном виде.
#
#
# def HarvardArtMuseumsAPI(req):  # создадим функцию с параметром запроса
#
#     try:
#         request_api = requests.get(req)  # поскольку в процессе схемы запрос-ответ могут произойти непредвиденные
#         # события, заключаем отправку запроса GET модуля requests в блок try..except
#         pprint.pprint(request_api.json())  # с помощью библиотеки pprint выводим полученный ответ в формате json
#         # ознакомьтесь со списком ошибок, которые могут возникнуть
#         # https://2.python-requests.org/en/master/user/quickstart/#errors-and-exceptions
#     except requests.ConnectionError:  # 1
#         print('SSL: CERTIFICATE_VERIFY_FAILED')
#
#     except requests.HTTPError:  # 2
#         print('An HTTP error occurred')
#
#     except requests.ConnectTimeout:  # 3
#         print('The request timed out while trying to connect to the remote server')
#
#     except json.decoder.JSONDecodeError:  # 4
#         print('Probably you are unauthorized')
#
#
# def response_get(req):
#     """
#     Gets server's response
#     req:  string, the request started with https://api...
#     """
#
#     return requests.request('GET', req)  # альтернативный способ отправки запроса GET
#
#
# request = "https://api.harvardartmuseums.org/color/34838440?apikey=ff686a00-e16c-11e7-a6c9-1fecfde3d500"
# print('Final request: {}\n'.format(request))
# HarvardArtMuseumsAPI(request)
# response_get(request)


# class Today:
#     req = 'https://datazen.katren.ru/calendar/day/'
#
#     def __init__(self):
#         import requests
#         import pprint
#
#         date = input('yyyy-mm-dd: ')
#
#         req_result = requests.request('GET', Today.req + date + '/')
#
#         pprint.pprint(req_result.json())
#
# Today()

# https://pixabay.com/api/?key=12560268-c732fd49e9389bca6ac445641&q=yellow+flowers&image_type=photo

# class Picture:
#     MyKey = '12560268-c732fd49e9389bca6ac445641'
#     req = 'https://pixabay.com/api/'
#
#     def __init__(self):
#         import requests
#         import pprint
#
#         typePicture = 'q=yellow+flowers'
#         image_type = 'image_type=photo'
#         req_result = requests.request('GET', Picture.req + '?key=' + Picture.MyKey + '&' + typePicture + '&' + image_type + '/')
#         pprint.pprint(req_result.json())
#
# Picture()

# class bk:
#     req = 'https://fs1.e.lanbook.com/api/book/118648/page/2/img'
#
#     def __init__(self):
#         import requests
#         import pprint
#         req_result = requests.request('GET', bk.req)
#         url = "https://pp.vk.me/c540104/c624218/v624218602/3321/uYVa4FQv_q0.jpg"
#         out = open("img.jpg", "wb")
#         req_result = requests.request('GET', url)
#         out.write(url)
#         out.close
#         # print(type(req_result))
#         # pprint.pprint(req_result.json())
#
# bk()

class marvel():
    import hashlib
    m = hashlib.md5()
    publicKey = '60a83a7286b86efc49fbf8a37e44dcc4'
    privateKey = '207b0ba73f7abc39af366c8c6ec59a7e40494ea3'
    ts = '123'
    m.update((str(ts) + str(privateKey) + str(publicKey)).encode('utf-8'))
    myApi = m.hexdigest()

    req = 'https://gateway.marvel.com/v1/public/comics?ts=' + ts + '&apikey=' + publicKey + '&hash=' + myApi

    def __init__(self):
        import requests
        import pprint
        req_result = requests.request('GET', marvel.req)
        # print(type(req_result))
        pprint.pprint(req_result.json())

marvel()