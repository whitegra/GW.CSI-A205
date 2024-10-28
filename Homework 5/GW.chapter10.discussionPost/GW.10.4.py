import random

class Coin:
    # init innitializes the sideup data with 'Heads':
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup


def main():
    my_coin = Coin()
    print('This side is up:', my_coin.get_sideup())

    # toss the coin
    print('Tossing the coin 10 times ... ')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

if __name__ == '__main__':
    main()
