
# tickets.py

# TicketMachine models a ticket machine that issues flat-fare tickets.

# The price of a ticket is specified via the constructor.  Instances
# check to ensure that a user only enters sensible amounts of money,
# and only print a ticket if enough money has been input.

class TicketMachine(object):

    # Create a machine that issues tickets of the given price.
    # Note that the price must be greater than zero, and there
    # are no checks to ensure this.
    def __init__(self, price):
        self.price = price    # price of a ticket from this machine
        self.balance = 0      # amount of money entered by a customer so far
        self.total = 0        # total amount of money collected by this machine

    # Return the price of a ticket
    def get_price(self):
        return self.price

    # Return the amount of money already inserted for the next ticket
    def get_balance(self):
        return self.balance

    # Receive an amount of money in cents from a customer and
    #   check that the amount is sensible
    def insert_money(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Use a positive amount:', amount)

    # Print a ticket if enough money has been inserted, and reduce the
    # current balance by the ticket price. Print an error message if more
    # money is required.
    def print_ticket(self):
        if self.balance >= self.price:
            print('------------------')
            print('- The Python Line')
            print('- Ticket')
            print('- %s cents' % self.price)
            print('------------------')
            self.total += self.price
            self.balance -= self.price
        else:
            print('Insert at least %s more cents.' %
                  (self.price - self.balance))

    # Return the money in the balance and clear the balance
    def refund_balance(self):
        amount_to_refund = self.balance
        self.balance = 0
        return amount_to_refund

if __name__ == '__main__':
    ab = TicketMachine(10)
    print(ab.get_price())