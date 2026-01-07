from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass




class Truck(Transport):
    def deliver(self):
        return "Доставка грузовиком"




class Ship(Transport):
    def deliver(self):
        return "Доставка кораблём"




class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == "truck":
            return Truck()
        elif transport_type == "ship":
            return Ship()
        else:
            raise ValueError("Неизвестный тип транспорта")




if __name__ == "__main__":
    factory = TransportFactory()
    transport = factory.create_transport("truck")
    print(transport.deliver())