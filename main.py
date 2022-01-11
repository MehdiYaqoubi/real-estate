from random import choice
from user import Users

FIRST_NAME = ['Ali', 'Mehdi', 'Sarah']
LAST_NAME = ['Alavi', 'Yaqoubi', 'Mohammadi']
MOBILES = ['09171111111', '09172222222', '09173333333', '09174444444']


if __name__ == "__main__":
    for mobile in MOBILES:
        Users(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in Users.objects_list:
        print(f"{user.id}\t {user.fullname}")

