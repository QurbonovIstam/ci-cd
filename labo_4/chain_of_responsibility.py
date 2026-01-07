class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler


def handle(self, request):
    if self.next:
        return self.next.handle(request)
    return "Запрос не обработан"




class AuthHandler(Handler):
    def handle(self, request):
        if request == "auth":
            return "Авторизация успешна"
        return super().handle(request)




class DataHandler(Handler):
    def handle(self, request):
        if request == "data":
            return "Данные обработаны"
        return super().handle(request)




if __name__ == "__main__":
    chain = AuthHandler(DataHandler())
    print(chain.handle("data"))