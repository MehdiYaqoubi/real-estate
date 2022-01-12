from sample import create_sample
from advertisement import ApartmentSell, ApartmentRent, HouseSell, HouseRent, \
    StoreSell, StoreRent


class Handler:
    ADVERTISEMENT_TYPES = {
        1: ApartmentSell, 2: ApartmentRent,
        3: HouseSell, 4: HouseRent,
        5: StoreSell, 6: StoreRent
    }

    SWITCHES = {
        'r': "get_report",
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            # print(adv, adv.manager.count())
            for obj in adv.objects_list:
                print(obj.show_details())

    def run(self):
        print("Welcome to Mehdi's Real Estate")
        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")
        user_input = input('Enter your choice: ')
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print("Invalid Input")
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == "__main__":
    create_sample()
    handler = Handler()
    handler.run()
