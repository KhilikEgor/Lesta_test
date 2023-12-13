# 2. На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой
# реализации.

# Первая реализация:
class RingBuffer:
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data

# Вторая реализация:
class CircularBuffer(object):
    def __init__(self, size):
        self.index= 0
        self.size= size
        self._data = []

    def record(self, value):
        if len(self._data) == self.size:
            self._data[self.index]= value
        else:
            self._data.append(value)
        self.index= (self.index + 1) % self.size

    def __getitem__(self, key):
        return(self._data[key])

    def __repr__(self):
        return self._data.__repr__() + ' (' + str(len(self._data))+' items)'

    def get_all(self):
        return(self._data)


#Реализация 1:
#Плюсы:

# 1) Легко понять и реализовать
# 2) Работает быстро для маленьких данных
#Минусы:
# 1) Если буфер полный, все данные должны быть скопированы при добавлении новых
# 2) Запрос всех данных буфера требует время, пропорциональное размеру буфера

#Реализация 2:
#Плюсы:
# 1) Быстрый доступ к данным (о(1) операция доступа к любому элементу)
# 2) Удобная работа с данным через реализацию стандартного интерфейса
#Минусы:
# 1) Несколько сложнее по сравнению с первой реализацией
# 2) Требует дополнительного места для хранения индекса