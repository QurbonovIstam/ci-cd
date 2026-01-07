from abc import ABC, abstractmethod


# продукты
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass




class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass




# конкретные продукты
class WindowsButton(Button):
    def paint(self):
        return "Windows Button"




class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Windows Checkbox"




# фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


    @abstractmethod
    def create_checkbox(self):
        pass




class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()


def create_checkbox(self):
    return WindowsCheckbox()




if __name__ == "__main__":
    factory = WindowsFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())