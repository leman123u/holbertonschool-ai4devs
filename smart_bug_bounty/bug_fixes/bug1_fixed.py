
def get_last_items(items, n):
    if n <= 0:
        return []

    if n >= len(items):
        return items

    start = len(items) - n

    return items[start:]


numbers = [10, 20, 30, 40, 50]

print(get_last_items(numbers, 3))
print(get_last_items(numbers, 1))
print(get_last_items(numbers, 0))
