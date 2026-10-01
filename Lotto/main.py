import random
import statistics

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,  36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
lottery_numbers_frequency = {}

def lottery_drawing():
    for i in range(6):
        rnd_index = random.randint(0, len(lottery_numbers) - i - 1)
        lottery_numbers[rnd_index], lottery_numbers[len(lottery_numbers) - i - 1] = lottery_numbers[len(lottery_numbers) - i -1], lottery_numbers[rnd_index]
    return lottery_numbers[-6:]

def print_lottery_numbers(numbers):
    print("Lottery numbers are: ", end="")
    for number in numbers:
        print(number, end=" ")
    print()

def print_lottery_statistics():
    print("Lottery numbers frequency:")
    for number, frequency in sorted(lottery_numbers_frequency.items()):
        print(f"{number}: {frequency}")

def add_frequency_to_dict(numbers):
    for number in numbers:
        if number in lottery_numbers_frequency:
            lottery_numbers_frequency[number] += 1
        else:
            lottery_numbers_frequency[number] = 1

def check_distribution():
    frequencies = list(lottery_numbers_frequency.values())

    average = statistics.mean(frequencies)

    print(f"\nDurchschnitt: {average:.2f}")

def generate_lottery_statistics():
    draws = input("Wie oft soll die Lotterie gezogen werden? ")
    for i in range(int(draws)):
        add_frequency_to_dict(lottery_drawing())
    print_lottery_statistics()
    check_distribution()




print_lottery_numbers(lottery_drawing())
generate_lottery_statistics()

