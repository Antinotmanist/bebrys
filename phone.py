class Phone(Item):  # наследование класса
       def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super finction yo have acces atr
        super().__init__(
            name, price, quantity
        )
        # assert делает утверждение которое должно выполняться
        
        assert broken_phones >= 0, f'Сломанный телефон {broken_phones} не входит в состояния 0 или 1'

        self.broken_phones = broken_phones