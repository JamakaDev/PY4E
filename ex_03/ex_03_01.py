#EX_03_01

hours = int(input('Enter hours worked: '))
rate = int(input('Enter rate: '))
ot_hours = hours-40
ot_rate = rate*1.5
if hours > 40:
    pay = (40*rate)+(ot_hours*ot_rate)
else:
    pay = hours*rate
print(f'Your paycheck this week is {pay}')

#EX_03_02

try:
    hours = float(input('Enter hours worked: '))
    rate = float(input('Enter rate: '))
    ot_hours = hours-40
    ot_rate = rate*1.5
    if hours > 40:
        pay = (40*rate)+(ot_hours*ot_rate)
    else:
        pay = hours*rate
    print(f'Your paycheck this week is {pay}')
except ValueError:
    print('Error, please enter numeric format')
