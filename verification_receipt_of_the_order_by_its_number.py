import sender_stand_request
import data

def test_get_an_order_by_track():
    # В переменную response_order сохраняется результат запроса о создании нового заказа
    response_order = sender_stand_request.post_creating_order(data.order_body)
    # Проверка, что код ответа равен 201 (создан)
    assert response_order.status_code == 201
    # В переменную track сохраняем тело ответа
    track = response_order.json()["track"]
    # В переменную response сохраняется результат запроса о получении заказа по его номеру
    response = sender_stand_request.get_order_number(track)
    # Проверка, что код ответа равен 200
    assert response.status_code == 200
