'''This module would be the cointainer of the python module'''

def internIneuron(n):
    try:
        if type(n) == int:
            if n < 3 and n>0:
                return 'You need to do more internship.'
            elif n >= 3:
                return 'You have completed the minimum number of internship required.'
            else:
                raise ArithmeticError
        else:
            raise ValueError
    except:
        return 'Please enter a valid positive integer.'

