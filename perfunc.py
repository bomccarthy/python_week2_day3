from math import pi

def sqft(l,w):
    try:
        area = float(l) * float(w)
        print(f'The sqare footage is {str(area)}.')
    except ValueError:
        print('\nThe length and width must both be numbers.')

def circ(r):
    try:
        circum = 2 * float(r) * pi
        print(f'The circumference is {str(round(circum,3))}.')
    except ValueError:
        print('\nThe radius must be a number.')