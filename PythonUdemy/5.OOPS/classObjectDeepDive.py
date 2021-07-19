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
        self.name = name 
        self.balance = balance
        self.transaction_list = []
        print("Account Created for " + self.name)
        self.transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print ("Not have enough balance to perform the withdraw")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")
    
    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1 
            print (f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")

if __name__ == '__main__':
    tim = Account("Tim",0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(400)
    # tim.show_balance()
    """
    Account Created for Tim
    Balance is 0
    Balance is 1000
    Balance is 600
    """

    tim.withdraw(500)
    # Not have enough balance to perform the withdraw
    # Balance is 1000

    tim.show_transaction()
    #   1000 deposited  2021-07-18 13:54:34.149838+00:00 on (local time was 2021-07-18 19:24:34.149838+05:30)
    tim.deposit(1000)
    tim.show_transaction()
    """
    Balance is 1100
    1000 deposited  2021-07-18 14:20:11.920087+00:00 on (local time was 2021-07-18 19:50:11.920087+05:30)
    -401 withdrawn  2021-07-18 14:20:11.920087+00:00 on (local time was 2021-07-18 19:50:11.920087+05:30)
    -501 withdrawn  2021-07-18 14:20:11.920087+00:00 on (local time was 2021-07-18 19:50:11.920087+05:30)
    1000 deposited  2021-07-18 14:20:11.922081+00:00 on (local time was 2021-07-18 19:50:11.922081+05:30)
    """

    mark = Account("Mark", 800)
    mark.deposit(100)
    mark.withdraw(200)
    mark.show_transaction()
    '''
    Account Created for Mark
    Balance is 900
    Balance is 700
    800 deposited on 2021-07-19 02:37:31.095062+00:00 (local time was 2021-07-19 08:07:31.095062+05:30)
    100 deposited on 2021-07-19 02:37:31.096059+00:00 (local time was 2021-07-19 08:07:31.096059+05:30)
    200 withdrawn on 2021-07-19 02:37:31.096059+00:00 (local time was 2021-07-19 08:07:31.096059+05:30)
    '''
