# Класс Магазина
class Shop():
    # Конструктор
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = {}

# Функции
    # Добавление ассортимента и цен
    def add_item(self, goods, price):
        self.items[goods] = price
        print(f"Товар {goods} добавлен в ассортимент. Цена: {price} рублей.")

    # Удаление товара из ассортимента
    def remove_item(self, goods):
        if goods in self.items:
            del self.items[goods]
            print(f"Товар {goods} удален из ассортимента.")
        else:
            print(f"Товар {goods} не найден в ассортименте.")

    # Вывод цены по названию товара
    def get_price(self, goods):
        if goods in self.items:
            print(f"Цена {goods}: {self.items[goods]} рублей.")
        else:
            print(f"Товар {goods} не найден в ассортименте.")

    # Обновление цены по названию товара
    def update_price(self, goods, new_price):
        if goods in self.items:
            self.items[goods] = new_price
            print(f"Цена {goods} обновлена.")
        else:
            print(f"Товар {goods} не найден в ассортименте.")

    # Вывод ассортимента
    def show_items(self):
        print("Ассортимент:")
        for goods, price in self.items.items():
            print(f"{goods}: {price} рублей")

# Тестирование
shop = Shop("Улыбка", "ул. Пушкина, 1", {})
shop.add_item("Кофе", 100)
shop.add_item("Чай", 50)
shop.add_item("Сок", 70)
shop.remove_item("Кофе")
shop.get_price("Кофе")
shop.get_price("Чай")
shop.get_price("Сок")
shop.update_price("Кофе", 120)
shop.show_items()


