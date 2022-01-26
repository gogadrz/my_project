from gardener import Gardener
from garden import PotatoGarden


def main():
    gardener_serafim = Gardener('Серафим Евлампьевич', PotatoGarden(5))
    gardener_serafim.show_info()
    print()

    while True:
        print('Садовник полил грядку.')
        gardener_serafim.service_garden_line()
        if gardener_serafim.show_info():
            break

    gardener_serafim.harvest_all_potatoes()
    gardener_serafim.show_info()


main()
