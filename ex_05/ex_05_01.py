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
print(f'{sum(numbers)} {len(numbers)} {sum(numbers)/len(numbers):.3} ')
