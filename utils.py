def show_delivery_progress(item, quantity, location_one, location_two):

    return f"Курьер забрал {quantity} {item} с {location_one}.\n" \
           f"Курьер везет {quantity} {item} с {location_one} в {location_two}.\n" \
           f"Курьер доставил {quantity} {item} в {location_two}."


def show_items(location_one, location_two):

    return f"В {location_one} хранится:\n{location_one.get_items()}\n" \
           f"Свободных слотов: {location_one.get_free_space()}\n" \
           f"В {location_two} хранится:\n{location_two.get_items()}\n" \
           f"Свободных слотов: {location_two.get_free_space()}"


def order_transfer(location_one, location_two, user_request):

    location_one_result = location_one.remove(user_request.product, user_request.amount)
    if True in location_one_result:
        print("Нужное количество товара есть в наличии.")
        location_two_result = location_two.add(user_request.product, user_request.amount)
        if True in location_two_result:
            print("Нужное количество товара будет добавлено.")
            print(show_delivery_progress(user_request.product, user_request.amount, location_one, location_two))
            print(show_items(location_one, location_two))
        else:
            print("Недостаточно места для добавления товара. Советуем изменить заказ.")
            location_one_result = location_one.add(user_request.product, user_request.amount)
            print("Возвращаем товар в точку отправления.")
            print(show_items(location_one, location_two))
    else:
        print("Не хватает товара в наличии. Советуем изменить заказ.")