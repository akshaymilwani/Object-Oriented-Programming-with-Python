
# mail.py

# A class to model a simple mail item. The item has sender and recipient
# addresses and a message string.

class MailItem(object):

    # creates a mail item from sender to the given recipient, containing
    # the given message
    def __init__(self, xfrom: str, to: str, message: str) -> None:
        self.xfrom = xfrom      # sender of the item
        self.to = to            # the intended recipient
        self.message = message  # text of the message

    # returns the sender of this message
    def get_from(self) -> str:
        return self.xfrom

    # returns the intended recipient of this message
    def get_to(self) -> str:
        return self.to

    # returns the text of the message
    def get_message(self) -> str:
        return self.message

    # prints this mail message to the terminal
    def print(self) -> None:
        print('From: ' + self.xfrom)
        print('To: ' + self.to)
        print('Message: ' + self.message)


# A simple model of a mail server. The server is able to receive
# mail items for storage, and deliver them to clients on demand.

class MailServer(object):

    # constructs a mail server
    def __init__(self) -> None:
        self.items = []         # type: List[MailItem]

    # returns the number of mail items waiting for a user
    def how_many_mail_items(self, who: str) -> int:
        count = 0
        for item in self.items:
            if item.get_to() == who:
                count += 1
        return count

    # returns the next mail item for a user, or None if there aren't any
    def find_next_mail_item(self, who: str) -> MailItem:
        for item in self.items:
            if item.get_to() == who:
                return item
        return None

    # returns and removes the next mail item for a user if one exists
    def next_mail_item(self, who: str) -> MailItem:
        item = self.find_next_mail_item(who)
        if item != None:
            self.items.remove(item)
        return item

    # adds the given mail item to the message list
    def post(self, item: MailItem) -> None:
        self.items.append(item)


# A class to model a simple email client. The client is run by a
# particular user, and sends and retrieves mail via a particular server.

class MailClient(object):

    # creates a mail client for a user that's attached to the given server
    def __init__(self, server: MailServer, user: str) -> None:
        self.server = server   # server used for sending and receiving
        self.user = user       # user running this client
    
    # returns the next mail item (if any) for this user
    def next_mail_item(self) -> MailItem:
        return self.server.next_mail_item(self.user)

    # prints the next mail item (if any) for this user to the terminal
    def print_next_mail_item(self) -> None:
        item = self.server.next_mail_item(self.user)
        if item == None:
            print('No new mail.')
        else:
            item.print()

    # sends a message to the given recipient via the attached mail server
    def send_mail_item(self, to: str, message: str) -> None:
        item = MailItem(self.user, to, message)
        self.server.post(item)
