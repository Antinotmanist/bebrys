class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # assert делает утверждение которое должно выполняться
        assert price >= 0, f'Ваша цена {price} не входит в нужные условия'
        assert quantity >= 0, f'идиот'


        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'