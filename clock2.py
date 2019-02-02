
# clock2.py -- allows clocks to be created at a specified time
#           -- adds a repr method to ClockDisplay

# The NumberDisplay class represents a digital number display that can hold
# values from zero to a given limit. The limit can be specified when creating
# the display. The values range from zero (inclusive) to limit-1. If used,
# for example, for the seconds on a digital clock, the limit would be 60, 
# resulting in display values from 0 to 59. When incremented, the display 
# automatically rolls over to zero when reaching the limit.

class NumberDisplay(object):

    def __init__(self, rollover_limit):
        self.value = 0
        self.limit = rollover_limit

    def get_value(self):
        return self.value

    # Set the value of the display to the new specified value. If the new
    # value is less than zero or over the limit, do nothing.
    def set_value(self, new):
        if 0 <= new < self.limit:
            self.value = new

    # Increment the display value by one, rolling over to zero if the
    # limit is reached.
    def increment(self):
        self.value = (self.value + 1) % self.limit

    # Return the display value (that is, the current value) as a two-digit
    # string.  Pad values less than ten with a space.
    def get_display(self):
        return '%02d' % self.value


# The ClockDisplay class implements a digital clock display for a
# European-style 24 hour clock. The clock shows hours and minutes. The 
# range of the clock is 00:00 (midnight) to 23:59 (one minute before 
# midnight).
# 
# The clock display receives "ticks" (via the tick method) every minute
# and reacts by incrementing the display. This is done in the usual clock
# fashion: the hour increments when the minutes roll over to zero.

class ClockDisplay(object):

    # Initializer for creating clocks at the specified time.
    def __init__(self, hour=0, minute=0):
        self.hours = NumberDisplay(12)
        self.minutes = NumberDisplay(60)
        self.set_time(hour, minute)

    # Set the time of the display to the specified hour and minute.
    def set_time(self, hour, minute):
        self.hours.set_value(hour)
        self.minutes.set_value(minute)

    # This method should get called once every minute - it makes
    # the clock display go one minute forward.
    def tick(self):
        self.minutes.increment()
        if self.minutes.get_value() == 0:  # it just rolled over!
            self.hours.increment()

    # Return a string that represents the display in the format HH:MM.
    def get_display(self):
        return self.hours.get_display() + ':' + \
            self.minutes.get_display()

    def __repr__(self):
        return 'ClockDisplay(%r, %r)' % \
            (self.hours.get_value(), self.minutes.get_value())

def main():
    x = ClockDisplay(10, 15)
    print(x)

if __name__ == '__main__':
    main()
