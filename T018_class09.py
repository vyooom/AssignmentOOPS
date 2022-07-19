import logging
logging.basicConfig(filename='logTask_018_class09',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 09')

class Ineuron_2():
    '''An example of implementing public, private & protected in class..'''

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
        logging.info('My name is %s & I am in %s course, as a %s.'%(a, b, c))
        return a, b, c

abhi = Ineuron_2()
abhi.updateData('abhishek', 'fsds', 'student')
abhi.intro()
logging.info(abhi.name)
logging.info(abhi._course)
logging.info(abhi._Ineuron_2__label)

sudh = Ineuron_2()
sudh.updateData('sudh', 'fsds', 'instructor')
sudh.intro()
logging.info(sudh.name)
logging.info(sudh._course)
logging.info(sudh._Ineuron_2__label)


sunny = Ineuron_2()
sunny.updateData('Sunny', 'Python', 'guide')
sunny.intro()
logging.info(sunny.name)
logging.info(sunny._course)
logging.info(sunny._Ineuron_2__label)

