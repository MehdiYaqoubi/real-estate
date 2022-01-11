from base import BaseClass


class Sell(BaseClass):
    def __init__(
            self, price_per_meter, discountable, convertible, *args, **kwargs
    ):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertible = convertible
        super().__init__(*args, **kwargs)


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
