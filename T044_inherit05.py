import logging
logging.basicConfig(filename='logTask_044_inherit05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Inheritance :- Example - 05')

class Ineuron:
    '''Fifth example of inheritance'''

    def __init__(self, course, id):
        self.course = course
        self.id = id

    def nextId(self):
        try:
            r = self.id + 1
            logging.info('The next identification is %s.' % r)
            return r
        except Exception:
            logging.error()


class OOPS(Ineuron):
    '''This is a chid class inheriting from a parent class.'''
    def __init__(self, course, id, duration):
        '''Course name its identification number and the duration of classes in days.'''
        super().__init__(course, id)
        self.duration = duration

    def show(self):
        logging.info('This course is %s with an identification number %s & its duration is %s.'%(self.course, self.id, self.duration))
        return self.course, self.duration

    def nextId(self):
        '''Overridding the parent class method.'''
        try:
            r = self.id * 10
            logging.info('This change is in child class. The next identification is %s.'%r)
            return r
        except Exception:
            logging.error()


logging.info('Initializing the parent class.')
parent = Ineuron('fsds', 125)

logging.info('Initializing the child class.')
child = OOPS('oops', 150, 14)

logging.info('Accessing the parent class method:')
logging.info(parent.nextId())


logging.info('Accessing the child class method:')
logging.info(child.nextId())
