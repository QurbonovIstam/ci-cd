class PaymentStrategy:
    def pay(self, amount):
        pass




class CardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата картой: {amount}"




class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата наличными: {amount}"




class Shop:
    def __init__(self, strategy):
        self.strategy = strategy


    def checkout(self, amount):
        return self.strategy.pay(amount)




if __name__ == "__main__":
    shop = Shop(CardPayment())
    print(shop.checkout(1000))