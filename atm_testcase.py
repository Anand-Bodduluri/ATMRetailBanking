import unittest

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount to deposit must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

class TestATM(unittest.TestCase):
    def test_initial_balance(self):
        atm = ATM()
        self.assertEqual(atm.balance, 0)

    def test_deposit(self):
        atm = ATM()
        atm.deposit(100)
        self.assertEqual(atm.balance, 100)

    def test_invalid_deposit(self):
        atm = ATM()
        with self.assertRaises(ValueError):
            atm.deposit(-50)

    def test_withdraw(self):
        atm = ATM(200)
        atm.withdraw(50)
        self.assertEqual(atm.balance, 150)

    def test_insufficient_funds(self):
        atm = ATM(50)
        with self.assertRaises(ValueError):
            atm.withdraw(100)

if __name__ == '__main__':
    unittest.main()
