from base import BaseClass
from estate import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(BaseClass, Apartment, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"Apartment for sell:"


class ApartmentRent(BaseClass, Apartment, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"Apartment for rent:"


class HouseSell(BaseClass, House, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"House for sell:"


class HouseRent(BaseClass, House, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"House for rent:"


class StoreSell(BaseClass, Store, Sell):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"Store for sell:"


class StoreRent(BaseClass, Store, Rent):
    def show_details(self):
        self.show_description()
        self.show_price()

    def __str__(self):
        return f"Store for sell:"
