class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = 1

    def increase_cash(self, cash):
        self.till += cash

    def decrease_drink(self, drink):
        self.drinks -= drink

    def legal_age(self, customer):
        if customer.age >= 18:
            return "Come on in Jim!"
        else: 
            return "Not today Jim!"
    
    def drunk_limit(self, customer):
        if customer.drunkeness > 7:
            return "Go home Jim"
        else:
            return "Here's another one on the house Jim"