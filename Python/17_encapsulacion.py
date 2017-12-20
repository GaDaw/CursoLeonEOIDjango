# __variable la hace privada, no es accesible desde fuera
class MyCounter:
    __secretCount = 0
    def count (self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = MyCounter()
counter.count()
counter.count()
counter.count()
print(counter.__secretCount)