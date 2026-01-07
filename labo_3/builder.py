class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None


def show(self):
    return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"




class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()


    def build_cpu(self):
        self.computer.cpu = "Intel i7"


    def build_ram(self):
        self.computer.ram = "16GB"


    def build_storage(self):
        self.computer.storage = "512GB SSD"


    def get_result(self):
        return self.computer




if __name__ == "__main__":
    builder = ComputerBuilder()
    builder.build_cpu()
    builder.build_ram()
    builder.build_storage()
    pc = builder.get_result()
    print(pc.show())