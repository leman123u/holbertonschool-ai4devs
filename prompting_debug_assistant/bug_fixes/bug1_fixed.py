def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


def main():
    items = [10, 20, 30]
    print("Total:", calculate_total(items))
    print("Empty:", calculate_total([]))


main()