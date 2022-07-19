'''We will try to seperate the functionality of the class.'''

import logging
logging.basicConfig(filename='logTask_083_abstract04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Abstraction :- Example - 04')

class Ineuron():
    '''Class with duration in months.'''
    def __init__(self, time):
        self.duration = time

    def suggest(self):
        try:
            if self.duration > 10:
                logging.info('The FSDS course would be suitable for you.')
            elif self.duration > 5 and self.duration <= 10:
                logging.info('The Data Analyst course would be suitable for you.')
            elif self.duration <= 5 and self.duration > 0:
                logging.info('The Web Developer course would be suitable for you.')
            else:
                logging.info('Please enter the number of months available.')

        except:
            logging.error()


a = Ineuron(2)
a.suggest()
b = Ineuron(12)
b.suggest()



