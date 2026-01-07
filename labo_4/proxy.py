class Service:
    def request(self):
        return "Доступ к сервису"




class Proxy:
    def __init__(self, service):
        self.service = service


    def request(self):
        print("Проверка доступа")
        return self.service.request()




if __name__ == "__main__":
    service = Service()
    proxy = Proxy(service)
    print(proxy.request())