class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def decrease_wallet(self, wallet):
        self.wallet -= wallet

    def increase_level(self, level):
        self.drunkeness += level
    