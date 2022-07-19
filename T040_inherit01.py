import logging
logging.basicConfig(filename='logTask_040_inherit01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Inheritance :- Example - 01')

class Ineuron:
    course = 'Full Stack Data Science'

class OOPS(Ineuron):
    pass

a = OOPS()
logging.info('This is a test to see the most basic inheritance example.')
logging.info(a.course)
