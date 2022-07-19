import logging
logging.basicConfig(filename='logTask_014_class05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 05')

from T013_class04 import Ineuron, Student


abhi = Ineuron('abhishek', 'fsds', 'hpcl')
abhi.intro()

'''The parent super class Student is not called by the Ineuron class.
We only get a reference for the class.'''
