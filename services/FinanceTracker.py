from classes.transactions import Transaction

class FinanceTracker:
    def __init__(self, transactions):
        self._transactions = transactions or []

    def monthly_summary(self):
        incomeExpemceConutAndTotal = {"incomeCount": 0,
                                      "expensesCount": 0,
                                      "totalIncome": 0,
                                      "totalExpenses": 0,
                                      "currentBalance": 0}

        for transaction in self._transactions:
            if transaction.getType() == "income":
                incomeExpemceConutAndTotal["incomeCount"] += 1
                incomeExpemceConutAndTotal["totalIncome"] += transaction.getAmount()
                incomeExpemceConutAndTotal["currentBalance"] += transaction.getAmount()


            else:
                incomeExpemceConutAndTotal["expensesCount"] += 1
                incomeExpemceConutAndTotal["totalExpenses"] += transaction.getAmount()
                incomeExpemceConutAndTotal["currentBalance"] -= transaction.getAmount()

        return incomeExpemceConutAndTotal


    def catergories_expenses(self):
        expences = {}
        total_spen = 0
        only_expenses = (tr for tr in self._transactions if tr.getType() == "expense")
        for tr in only_expenses:
            cat = tr.getCategory() or (""
                                       "Other")
            amount = tr.getAmount()
            expences[cat] = expences.get(cat, 0) + amount
            total_spen += amount
        report = {}
        for cat, amount in expences.items():
            parcent = (amount / total_spen) * 100 if amount > 0 else 0
            report[cat] = {
                "spen": amount,
                "parcent %": round(parcent, 1)

            }
        return report


    def detect_overspending(self, budgets):
        actual = {}
        for transaction in self._transactions:
            if transaction.getType() == "expense":
                category = transaction.getCategory()
                amount = transaction.getAmount()
                if category in actual:
                    actual[category] += amount
                else:
                    actual[category] = amount

        result = {}

        for category, limit in budgets.items():
            spent = actual.get(category, 0)

            if spent > limit:
                result[category] = {
                    "budget": limit,
                    "spent": spent,
                    "over_by": spent - limit
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

