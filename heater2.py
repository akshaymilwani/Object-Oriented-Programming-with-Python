
# heater2.py

class Heater2(object):

    def __init__(self, min, max, increment=5, temperature=15):
        if not max > min:
            raise ValueError('Heater2: requires that max > min.')
        if not min <= temperature <= max:
            raise ValueError('Heater2: requires that min <= temp <= max.')
        if not increment > 0:
            raise ValueError('Heater2: requires that increment > 0.')
        self.min = min
        self.max = max
        self.increment = increment
        self.temperature = temperature

    def warmer(self):
        if self.temperature + self.increment <= self.max:
            self.temperature += self.increment

    def cooler(self):
        if self.temperature - self.increment >= self.min:
            self.temperature -= self.increment

    def set_increment(self, new_value):
        if new_value > 0:
            self.increment = new_value

    def get_temperature(self):
        return self.temperature

    def __repr__(self):
        return 'Heater2(%r, %r, %r, %r)' % \
            (self.min, self.max, self.increment, self.temperature)

if __name__ == '__main__':
    x = Heater2(10, 30)
    print(x)
    x.warmer()
    print(x)
    x.cooler()
    print(x)
    x.set_increment(2)
    x.cooler()
    print(x)
    x.cooler()
    print(x)
    x.cooler()
    print(x)
