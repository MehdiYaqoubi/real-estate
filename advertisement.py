from base import BaseClass
from estate import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(BaseClass, Apartment, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()

    # def __str__(self):
    #     print(f"Apartment for sell: {self.area}")


class ApartmentRent(BaseClass, Apartment, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseSell(BaseClass, House, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreSell(BaseClass, Store, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()


class StoreRent(BaseClass, Store, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()
