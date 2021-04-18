inp = input('Enter score:')
def computegrade():
    A = float(inp)
    if A >= 0.0 and A <=1.0:
        if A >= 0.9:
            print('A')
        elif A >= 0.8:
            print('B')
        elif A >= 0.8:
            print('C')
        elif A >= 0.7:
            print('C')
        elif A >= 0.6:
            print('D')
        else :print('F')
    else :print('Bad score')
computegrade()