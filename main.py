from input.parser import load

def main():
    tr = load("data/transaction.json")

    print(tr)

main()