class Device:
    def on(self):
        pass




class TV(Device):
    def on(self):
        return "Телевизор включён"




class Remote:
    def __init__(self, device):
        self.device = device


    def turn_on(self):
        return self.device.on()




if __name__ == "__main__":
    tv = TV()
    remote = Remote(tv)
    print(remote.turn_on())