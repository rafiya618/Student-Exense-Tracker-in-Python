import unittest
from project import Authentication, calculate_total, calculate_saving, Expenses

class TestExpensesFunctions(unittest.TestCase):

    def test_authentication_correct(self):
        # Test authentication with correct username and password
        self.assertTrue(Authentication("python123", "user1"))

    def test_authentication_incorrect(self):
        # Test authentication with incorrect username and password
        self.assertFalse(Authentication("incorrect_password", "user1"))
        self.assertFalse(Authentication("python123", "incorrect_username"))
        self.assertFalse(Authentication("incorrect_password", "incorrect_username"))

    def test_calculate_total(self):
        # Create an Expenses object
        user = Expenses()
        user.hostel_due = 15000.0
        user.transportation = 2000.0
        user.food = 6000.0
        user.university_due = 80000.0
        user.entertainment = 3000.0
        user.medical = 2000.0
        user.personal_stuff = 4000.0

        # Calculate the total expenses
        total_expense = calculate_total(user)

        # Assert that the calculated total matches the expected value
        expected_total = (15000.0 + 2000.0 + 6000.0 + 80000.0 + 3000.0 + 2000.0 + 4000.0)  # Calculate this based on the sample values
        self.assertEqual(total_expense, expected_total)

    def test_calculate_saving(self):
        # Create an Expenses object
        user = Expenses()
        user.hostel_due = 15000.0
        user.transportation = 2000.0
        user.food = 6000.0
        user.university_due = 80000.0
        user.entertainment = 3000.0
        user.medical = 2000.0
        user.personal_stuff = 4000.0

        # Set the my_income attribute
        user.my_income = 200000.0

        # Calculate the savings
        money_saved = calculate_saving(user)

        # Assert that the calculated savings match the expected value
        expected_savings = user.my_income - user.total_expense  # Calculate this based on the sample values
        self.assertEqual(money_saved, expected_savings)

if __name__ == '__main__':
    unittest.main()
