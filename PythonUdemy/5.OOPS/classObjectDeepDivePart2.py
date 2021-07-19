# Non public and Name Mangling

import datetime
import pytz

# class name should be camel case and no _
class Account:
    """ simple account class """
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name 
        self.__balance = balance
        self._transaction_list = []
        print("Account Created for " + self._name)
        self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print ("Not have enough balance to perform the withdraw")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")
    
    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1 
            print (f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")

if __name__ == '__main__':
    # mark = Account("Mark", 800)
    # mark._balance = 200
    # mark.deposit(100)
    # mark.withdraw(200)
    # mark.show_transaction()
    # mark.show_balance()
    """
    Account Created for Mark
    Balance is 300
    Balance is 100
        800 deposited on 2021-07-19 02:54:06.108984+00:00 (local time was 2021-07-19 08:24:06.108984+05:30)
        100 deposited on 2021-07-19 02:54:06.108984+00:00 (local time was 2021-07-19 08:24:06.108984+05:30)
        200 withdrawn on 2021-07-19 02:54:06.108984+00:00 (local time was 2021-07-19 08:24:06.108984+05:30)
    Balance is 100
    """
    mark = Account("Mark", 800)
    mark.__balance = 200
    mark.deposit(100)
    mark.withdraw(200)
    mark.show_transaction()
    mark.show_balance()
    """
    Balance is 900
    Balance is 700
        800 deposited on 2021-07-19 03:02:25.203073+00:00 (local time was 2021-07-19 08:32:25.203073+05:30)
        100 deposited on 2021-07-19 03:02:25.203073+00:00 (local time was 2021-07-19 08:32:25.203073+05:30)
        200 withdrawn on 2021-07-19 03:02:25.203073+00:00 (local time was 2021-07-19 08:32:25.203073+05:30)
    Balance is 700
    """
    print (mark.__dict__) # check '_Account__balance' - Name mangling 
    # {'_name': 'Mark', '_Account__balance': 700, '_transaction_list': [(datetime.datetime(2021, 7, 19, 3, 3, 59,
    # 743660, tzinfo=<UTC>), 800), (datetime.datetime(2021, 7, 19, 3, 3, 59, 743660, tzinfo=<UTC>), 100), (datetime.datetime(2021, 7, 19, 3, 3, 59, 743660, tzinfo=<UTC>), -200)], '__balance': 200}

    # mess with _Account__balance
    mark._Account__balance = 40
    mark.show_balance() # Balance is 40