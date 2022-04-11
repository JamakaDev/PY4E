def computepay(hours, rate):
    try:
        ot_hours = hours-40
        ot_rate = rate*1.5
        if hours > 40:
            pay = (40*rate)+(ot_hours*ot_rate)
        else:
            pay = hours*rate
        print(f'Pay: {pay}')
    except:
        print('Error, please enter numeric format')

computepay(50,15)
