import csv
class Item:
    # class attribute
    pay_rate = 0.8
    all = []  # Storing instances.

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation
        assert price >= 0
        assert quantity >= 0

        # Assigning
        self.__name = name  # cannot access it outside the class without nameangling !
        self.__price = price
        self.quantity = quantity

        # Adding an instance to all list
        Item.all.append(self)

    # Property decorate which helps to control the access to user and serve as a getter.
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, value):
    #     self.name = value

    def calc_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instance_from_data(cls, file:str):
        with open(file, 'r') as data:
            reader = csv.DictReader(data)
            for row in reader:
                # Instantiating Objects
                Item(

                    name = row['name'],
                    price = float(row['price']),
                    quantity= int(row["quantity"])

                )
    # Method to check if the number is integer or not
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Pretty formatting
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}",{self.__price},{self.quantity})'

    def connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
Hello, Sir !"""

    def send(self):
        pass


    def send_email(self):
        self.connect("s")
        self.prepare_body()
        self.send()