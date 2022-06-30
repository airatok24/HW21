from classes import Request, Store, Shop
from utils import order_transfer

proceed_further = True

if __name__ == "__main__":
    store = Store()
    store.items = {"печеньки": 10, "собачки": 5, "коробки": 25, "котики": 20}

    shop = Shop()
    shop.items = {"печеньки": 5, "собачки": 5}

    while proceed_further:

        user_input = input("Введите строку следующего типа: "
                           "'Доставить (количество) (наименование товара) из (место отправки) в (место доставки)'\n")
        if user_input == "stop":
            break

        user_request = Request(user_input)
        print(user_request)

        if user_request.from_value == "склад" and user_request.to_value == "магазин":
            location_one = store
            location_two = shop

            order_transfer(location_one, location_two, user_request)

        if user_request.from_value == "магазин" and user_request.to_value == "склад":
            location_one = shop
            location_two = store

            order_transfer(location_one, location_two, user_request)