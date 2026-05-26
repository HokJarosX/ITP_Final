def detect_overspending(self, budgets):
    actual = {}
    for transaction in self._transactions :
        if transaction.getType() == "expense":
            category = transaction.getCategory()
            amount = transaction.getAmount()
            if category in actual:
                actual[category]+= amount
            else:
                actual[category] = amount

    result = {}

    for category, limit in budgets.items():
        spent = actual.get(category,0)

        if spent > limit:
            result[category] =  {
                "budget": limit,
                "spent" : spent,
                "over_by":spent - limit
            }
    return result

def print_overspending_report(self, result):
    if not result:
        print("no overspending detected")
        return
    for category, info in result.items():
        print(f"{category}: overspent by ${info['over_by']}")

def get_default_budgets(self):
    return {
        "food": 50,
        "transport": 15,
        "shopping": 50,
    }






