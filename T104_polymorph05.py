import logging
logging.basicConfig(filename='logTask_104_polymorph05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Polymorphism :- Example - 05')

class Ineuron:
    def intro(self, duration = 1):
        '''Class with duration in months.'''
        try:
            if duration >= 10:
                logging.info('The duration of FSDS course at Ineuron is %s months.'%duration)

            elif duration >= 5 and duration < 10:
                logging.info('The duration of Javascript course at Ineuron is %s months.'%duration)

            elif duration >=2 and duration < 5:
                d = duration * 30
                logging.info('The duration of Web developer course at Ineuron is %s days.'%d)

            else:
                logging.info('The courses can be followed at Youtube as per users choice!')
        except:
            logging.error()

a = Ineuron()
b = Ineuron()
c = Ineuron()
d = Ineuron()

counter = 1
for i in (a,b,c,d):
    i.intro(counter)
    counter += 3

"""Polymorphism with a common method call."""

