def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


def main():
    assert calculate_total([10, 20, 30]) == 60
    assert calculate_total([]) == 0
    assert calculate_total([5]) == 5
    print("Total:", calculate_total([10, 20, 30]))
    print("All bug1 tests passed")


main()