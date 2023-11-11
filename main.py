class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # assert делает утверждение которое должно выполняться
        assert price >= 0, f'Ваша цена {price} не входит в нужные условия'
        assert quantity >= 0, f'идиот'


        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    
item1 = Item('Phone', 100, 5)

item2 = Item('BebraLop', 1000, 3)

print(item1.calculate_total_price())