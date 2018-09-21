import unittest

from account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_newly_opened_account_has_zero_balance(self):
        self.account.open()
        self.assertEqual(self.account.get_balance(), 0)

    def test_can_deposit_money(self):
        self.account.open()
        self.account.deposit(200)
        self.assertEqual(self.account.get_balance(),200)

    def test_can_deposit_money_sequentially(self):
        self.account.open()
        self.account.deposit(200)
        self.account.deposit(100) 
        
        self.assertEqual(self.account.get_balance(),300 )

    def test_can_withdraw_money(self):
        self.account.open()
        self.account.deposit(200)
        self.account.withdraw(100)

        self.assertEqual(self.account.get_balance(),200 )

    def test_can_withdraw_money_sequentially(self):
        self.account.open()
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.withdraw(50)

        self.assertEqual(self.account.get_balance(),50 )

    def test_checking_balance_of_closed_account_throw_error(self):
        self.account.open()
        self.account.close()
        
        with self.assertRaises(ValueError):
             self.account.get_balance()
             self.account.open()
             self.account.close()

    
    def test_can_deposit_into_closed_account(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
             self.account.deposit(50)
             self.account.open()
             self.account.close()


    def test_withdraw_from_closed_account(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
             self.account.withdraw(50)
             self.account.open()
             self.account.close()


    def test_cannot_witdraw_more_than_deposited(self):
        self.account.open()
        self.account.deposit(25)

        with self.assertRaises(ValueError):
             self.account.withdraw(50)
             self.account.open()
             self.account.deposit(25)


    def test_cant_withdraw_negative(self):
        self.account.open()
        self.account.deposit(100)

        with self.assertRaises(ValueError):
             self.account.withdraw(-50)
             self.account.open()
             self.account.deposit(100)

    def test_cant_deposit_negative(self):
        self.account.open()
        

        with self.assertRaises(ValueError):
             self.account.deposit(-50)
             self.account.open()
    if __name__ == '__main__':
        unittest.main()
    

    