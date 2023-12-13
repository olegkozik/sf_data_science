import random

def guess_number():
    low = 1
    high = 100
    tries = 0

    # Загадываем число
    number_to_guess = random.randint(low, high)
    
    while True:
        tries += 1
        guess = (low + high) // 2  # делаем предположение посредине диапазона
        if guess < number_to_guess:
            low = guess + 1  # сдвигаем нижнюю границу
        elif guess > number_to_guess:
            high = guess - 1  # сдвигаем верхнюю границу
        else:
            return guess, tries  # число угадано


    
#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for game_core_v2: ', end='')
print(guess_number())
