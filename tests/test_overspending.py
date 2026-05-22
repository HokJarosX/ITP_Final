
import os

import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.transactions import Transaction
from  services.overspending import detect_overspending

def make_expense (catagory, amount,):
    return Transaction(type ="expense", category=catagory, amount=amount , date ="2026-05-01")

def test_overspending():

    result = detect_overspending([make_expense("food", 80)],
        {"food": 50} )

    assert result["food"]["over_by"]==30
    print("test 1 passed correctly")



if __name__=="__main__":
    test_overspending()

