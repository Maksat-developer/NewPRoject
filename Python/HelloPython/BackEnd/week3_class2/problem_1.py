class Factory:
    def engine(self):
        return 'Двигатель готов, Сэр!'
    def bridge(self):
        return 'Ходовая часть готова!'

q = Factory()
print(q.engine())
print(q.bridge())

class Toyota(Factory):
    def weels(self):
        return 'Колеса готовы!'
    def window(self):
        return 'стекло готовы'

w = Toyota()
print(w.weels())
print(w.window())

x = [q.engine(), q.bridge(), w.weels(), w.window()]
print(x)
