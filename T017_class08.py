import logging
logging.basicConfig(filename='logTask_017_class08',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 08')

class Ineuron():
    '''An example having abstractions.'''

    def __init__(self):
        self.name = 'jon doe'
        self._course = 'programming'
        self.__label = 'student'
        logging.info('The class has been initialized.')

    def updateData(self, name, course, label):
        self.name = name
        self._course = course
        self.__label = label
        logging.info('The data was updated with update method.')

    def intro(self):
        a = self.name
        b = self._course
        c = self.__label
        logging.info('My name is %s & I am in %s course, as a %s'%(a, b, c))
        return a, b, c

abhi = Ineuron()
abhi.updateData('abhishek', 'fsds', 'student')
abhi.intro()

sudh = Ineuron()
sudh.updateData('sudh', 'fsds', 'instructor')
sudh.intro()
