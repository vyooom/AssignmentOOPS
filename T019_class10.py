import logging
logging.basicConfig(filename='logTask_019_class10',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 10')

class Ineuron3():
    '''An example of implementing public, private & protected in class..'''

    def __init__(self):
        self.name = 'jon doe'
        self._course = 'programming'
        self.__label = 'student'
        self.__blog = 0
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

    def blog(self):
        logging.info('I have to write blogs.')

    def blogPost(self, n):
        self.__blog = n
        logging.info('I have written %s blogs'%self.__blog)



abhi = Ineuron3()
abhi.updateData('abhishek', 'fsds', 'student')
abhi.intro()
logging.info(abhi.name)
logging.info(abhi._course)
logging.info(abhi._Ineuron3__label)
abhi.blog()
abhi.blogPost(3)

sudh = Ineuron3()
sudh.updateData('sudh', 'fsds', 'instructor')
sudh.intro()
logging.info(sudh.name)
logging.info(sudh._course)
logging.info(sudh._Ineuron3__label)
sudh.blog()
sudh.blogPost(100)

sunny = Ineuron3()
sunny.updateData('Sunny', 'Python', 'guide')
sunny.intro()
logging.info(sunny.name)
logging.info(sunny._course)
logging.info(sunny._Ineuron3__label)
sunny.blog()
sunny.blogPost(26)
