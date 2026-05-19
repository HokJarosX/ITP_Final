def monthlySummary(transactions):
    incomeExpemceConutAndTotal = {"incomeCount": 0,
                      "expensesCount": 0,
                      "totalIncome": 0,
                      "totalExpenses": 0}


    for transaction in transactions:
        if transaction.type == "income":
            incomeExpemceConutAndTotal["incomeCount"] += 1
            incomeExpemceConutAndTotal["totalIncome"] += transaction.amount

        else:
            incomeExpemceConutAndTotal["expensesCount"] += 1
            incomeExpemceConutAndTotal["totalExpenses"] += transaction.amount

    return incomeExpemceConutAndTotal