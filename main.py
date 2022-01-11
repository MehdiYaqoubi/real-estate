from random import choice

from advertisement import ApartmentSell
from estate import Apartment, House, Store
from user import Users
from region import Region

FIRST_NAME = ['Ali', 'Mehdi', 'Sarah']
LAST_NAME = ['Alavi', 'Yaqoubi', 'Mohammadi']
MOBILES = ['09171111111', '09172222222', '09173333333', '09174444444']

if __name__ == "__main__":
    for mobile in MOBILES:
        Users(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in Users.objects_list:
        print(f"{user.id}\t {user.fullname}")

    reg1 = Region(name='Region 1')

    apt1 = Apartment(
        has_elevator=True, has_parking=True, floor=2,
        user=Users.objects_list[0], area=80, room_count=2, built_year=1390,
        region=reg1, address='Some text...'
    )
    apt1.show_description()

    house = House(
        has_yard=True, floor_count=3, user=Users.objects_list[1],
        area=400, room_count=4, built_year=1380,
        region=reg1, address='Some text...'
    )
    house.show_description()

    store = Store(
        user=Users.objects_list[2], area=30, room_count=0, built_year=1390,
        region=reg1, address='Some text...'
    )
    store.show_description()

    apartment_sell = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2,
        user=Users.objects_list[0], area=80, room_count=2, built_year=1390,
        region=reg1, address='Some text...',
        price_per_meter=10, discountable=True, convertible=False
    )
    apartment_sell.show_details()
