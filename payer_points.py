import csv
import sys
from collections import defaultdict

def spend_points(points_to_spend):
    # Initialize the payers' points balance
    payers_points = defaultdict(int)

    # Read the transactions from the CSV file
    with open('transactions.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        transactions = list(reader)

    # Sort the transactions based on the timestamp
    transactions.sort(key=lambda x: x['timestamp'])

    # Spend the points based on the rules
    for transaction in transactions:
        payer = transaction['payer']
        points = int(transaction['points'])
        payers_points[payer] += points
        if points_to_spend > 0:
            if payers_points[payer] >= points_to_spend:
                payers_points[payer] -= points_to_spend
                points_to_spend = 0
            else:
                points_to_spend -= payers_points[payer]
                payers_points[payer] = 0

    # Return the payers' points balance
    return dict(payers_points)

if __name__ == '__main__':
    # Read the argument for the amount of points to spend
    points_to_spend = int(sys.argv[1])
    result = spend_points(points_to_spend)
    print(result)
