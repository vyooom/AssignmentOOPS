import logging
logging.basicConfig(filename='logTask_042_inherit03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Inheritance :- Example - 03')

class Ineuron:
    '''Third example of inheritance'''
    def __init__(self, course):
        self.course = course

class OOPS(Ineuron):
    '''This is a chid class inheriting from a parent class.'''
    def __init__(self, course, id):
        super().__init__(course)
        self.id = id

    def show(self):
        logging.info('This course is %s with an identification number %s.'%(self.course, self.id))


child = OOPS('OOPS', '2022/05/07')

logging.info('This is a test to see inheritance in child class.')

logging.info('Inheritance for a child class object child.show()')
logging.info(child.show())
