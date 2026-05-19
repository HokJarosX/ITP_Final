def monthlySummary(transactions):
    incomeExpemceConutAndTotal = {"incomeCount": 0,
                      "expensesCount": 0,
                      "totalIncome": 0,
                      "totalExpenses": 0}


    for transaction in transactions:
        if transaction.type == "income":
            monthlySummary["incomeCount"] += 1
            monthlySummary["totalIncome"] += transaction.amount

        else:
            monthlySummary["expensesCount"] += 1
            monthlySummary["totalExpenses"] += transaction.amount