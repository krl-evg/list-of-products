name = input("Введите имя пользователя: ")
print(" ")
print("-" * 30)
print(f"Привет, {name}!")
print("-" * 30)
print(" ")

purchases = []

while True:
    item_name = input("Введите название товара, или напишите 'стоп' для завершения: ")
    if item_name == "стоп":
        break

    item_price = int(input("Введите цену товара: "))
    purchases.append({"name": item_name, "price": item_price})
    print(f"{item_name} добавлен в список")

    if not purchases:
        print("Список пуст")
    else:
        total = 0
        for item in purchases:
            total += item['price']

        m_exp = purchases[0]
        for item in purchases:
            if item ["price"] > m_exp["price"]:
                m_exp = item

        m_che = purchases[0]
        for item in purchases:
             if item ["price"] < m_che["price"]:
              m_che = item

        count = len(purchases)

        print("-" * 30)
        print("Ваши покупки: ")
        for item in purchases:
            print(f"{item['name']} — {item['price']} руб.")
        print("-" * 30)

        if total > 1000:
            disc = total * 0.1
            fin_tot = total - disc
            print("-" * 30)
            print("Итоговая сумма больше 1000! Применена скида 10%.")
            print(f"Итоговая сумма: {fin_tot:.0f}")
            print("-" * 30)
        else:
            print(" ")
            print("-" * 30)
            print(f"Итоговая сумма {total}, скидки нету.")
            print("-" * 30)
            print(" ")

        print("-" * 30)
        print("Статистика:")
        print(f"Всего покупок: {count}")
        print(f"Самый дорогой товар: {m_exp['name']} ({m_exp['price']} руб.)")
        print(f"Самый дешевый товар: {m_che['name']} ({m_che['price']} руб.)")
        print("-" * 30)
        print(" ")