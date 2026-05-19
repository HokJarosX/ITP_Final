import sys
import os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classess.transactions import Transaction
from services.overspendig import detect_overspending

def make_expense(catagory, amount):
    return Transaction(type="expense",):
def make_income(amount):
    return Transaction(type=)