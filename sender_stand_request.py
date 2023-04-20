import configuration
import requests

# фун-ия создания нового заказа
def post_creating_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_ORDER,
                         json=order_body)

#Фун-ия получения заказа по его номеру
def get_order_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER + f"{track}") # f"{track}" привели значение track к строчному формату
