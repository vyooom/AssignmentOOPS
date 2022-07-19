import logging
logging.basicConfig(filename='logTask_041_inherit02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Inheritance :- Example - 02')

class Ineuron:
    '''Second example of inheritance'''
    course = 'Full Stack Data Science'

class OOPS(Ineuron):
    course = 'Object Oriented Programming'

parent = Ineuron()
child = OOPS()

logging.info('This is a test to see conflict inheritance object.')
logging.info('Inheritance for a parent class object parent.course')
logging.info(parent.course)
logging.info('Inheritance for a child class object child.course')
logging.info(child.course)
