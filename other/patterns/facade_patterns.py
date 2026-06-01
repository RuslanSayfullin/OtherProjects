# Подсистема 1
class Subsystem1:
    def operation1(self):
        return "subsystem 1 : Operation 1"
    
    def operation2(self):
        return "subsystem 1 : Operation 2"
    

# Подсистема 2
class Subsystem2:
    def operation1(self):
        return "Subsystem 2 : Operation 1"
    
    def operation2(self):
        return "Subsystem 2 : Operation 2"


# Фасад
class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        result = []
        result.append("Facade initializes subsystems: ")
        result.append(self._subsystem1.operation1())
        result.append(self._subsystem2.operation1())
        result.append("Facade orders subsystems to perform actions: ")
        result.append(self._subsystem1.operation2())
        result.append(self._subsystem2.operation2())
        return "\n".join(result)
    
# Клиенткий код
def client_code(facade):
    print(facade.operation())


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)