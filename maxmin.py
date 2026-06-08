numbers = input('Enter numbers separated by a comma:').split(',')
max = int(numbers[0])
min = int(numbers[0])
for num in numbers:
    num = int(num)
    if num > max:
        max = num
    elif num < min:
        min = num
print(f'The minimum value is: {min}')
print(f'The maximum value is: {max}')
