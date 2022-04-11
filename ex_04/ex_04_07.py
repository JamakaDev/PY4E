def computegrade(score):
    try:
        if 0.0 > score or score > 1.0:
            print('Bad score')
        elif score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    except:
        print('Bad score')
computegrade('perfect')
computegrade(0.89)
computegrade(0.75)
computegrade(0.95)
computegrade(10.0)
computegrade(0.5)
computegrade(0.69)
