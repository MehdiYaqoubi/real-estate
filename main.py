from random import choice

from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent, \
    StoreSell, StoreRent
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
    reg2 = Region(name='Region 2')
    reg3 = Region(name='Region 3')
    reg4 = Region(name='Region 4')
    reg5 = Region(name='Region 5')

    # ApartmentSell
    apartment_sell = ApartmentSell(
        has_elevator=True, has_parking=True, floor=2,
        user=Users.objects_list[0], area=80, room_count=2, built_year=1390,
        region=reg1, address='Some text...', price_per_meter=10,
        discountable=True
    )
    # apartment_sell.show_details()

    # ApartmentRent
    apartment_rent = ApartmentRent(
        has_elevator=False, has_parking=False, floor=1,
        user=Users.objects_list[1], area=70, room_count=1, built_year=1392,
        region=reg1, address='Some text...',
        initial_price=100, monthly_price=3.5, discountable=True,
        convertible=True
    )
    # apartment_rent.show_details()

    # HouseSell
    house_sell = HouseSell(
        has_yard=True, floor_count=3, user=Users.objects_list[2],
        area=400, room_count=4, built_year=1380,
        region=reg1, address='Some text...',
        price_per_meter=20, discountable=True, convertible=True
    )
    # house_sell.show_details()

    # HouseRent
    house_rent = HouseRent(
        has_yard=True, floor_count=2, user=Users.objects_list[3],
        area=200, room_count=2, built_year=1385,
        region=reg1, address='Some text...',
        initial_price=90, monthly_price=2.5, discountable=True,
        convertible=True
    )
    # house_rent.show_details()

    # StoreSell
    store_sell = StoreSell(
        user=Users.objects_list[1], area=30, room_count=0, built_year=1390,
        region=reg1, address='Some text...',
        price_per_meter=20, discountable=True
    )
    # store_sell.show_details()

    # StoreRent
    store_rent = StoreRent(
        user=Users.objects_list[2], area=50, room_count=0, built_year=1399,
        region=reg1, address='Some text...',
        initial_price=500, monthly_price=1.5, discountable=True,
        convertible=True
    )
    # store_rent.show_details()

