numbers = []
while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        elif num.isdigit():
            numbers.append(int(num))
        else:
            print('Invalid input')

    except:
        print('Invalid input')
print(f'Maximum number is: {max(numbers)} \nMinimum number is: {min(numbers)}')
