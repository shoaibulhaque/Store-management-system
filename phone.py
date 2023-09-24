from item import Item

class Phone(Item):
    # Defining Child's class constructor
    def __init__(self, name, phone, quantity, broken_phones):
        # Calling parent's class constructor
        super().__init__(name, phone, quantity)

        # Validation
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero!"

        self.broken_phones = broken_phones

    def display_broken_phones(self):
        return f"Broken phones: {self.broken_phones}"