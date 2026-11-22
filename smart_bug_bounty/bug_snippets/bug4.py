def find_maximum(numbers):
    if len(numbers) <= 0:
        return -1

    maximum = numbers[0]

    for i in range(1, len(numbers) + 1):
        if numbers[i] > maximum:
            maximum = numbers[i]

    return maximum


numbers = [12, 45, 23, 67, 34]

print("Maximum:", find_maximum(numbers))