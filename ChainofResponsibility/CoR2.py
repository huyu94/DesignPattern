class Handler:
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("ConcreteHandlerA 处理请求:", request)
            return True
        else:
            return super().handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("ConcreteHandlerB 处理请求:", request)
            return True
        else:
            return super().handle(request)


if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_successor(handler_b)

    handler_a.handle("A")
    handler_a.handle("B")
    handler_a.handle("C")

