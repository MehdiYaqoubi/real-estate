from base import BaseClass


class Sell(BaseClass):
    def __init__(
            self, price_per_meter, discountable, convertible, *args, **kwargs
    ):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(
            f"price: {self.price_per_meter}\t"
            f"discountable: {self.discountable}\t"
            f" convertible: {self.convertible}"
        )


class Rent(BaseClass):
    def __init__(
            self, initial_price, monthly_price, convertible, discountable,
            *args, **kwargs
    ):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertible = convertible
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(
            f"initial price: {self.initial_price}\t"
            f"monthly price: {self.monthly_price}"
            f"discountable: {self.discountable}\t"
            f" convertible: {self.convertible}"
        )