import logging
logging.basicConfig(filename='logTask_043_inherit04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Inheritance :- Example - 04')

class Ineuron:
    '''Fourth example of inheritance'''
    def __init__(self, course, id):
        self.course = course
        self.id = id

    def nextId(self):
        try:
            r = self.id + 1
            logging.info('The next identification is %s.'%r)
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
        return self.course

    def leftover(self):
        i = self.nextId()
        d = 500 - self.duration
        logging.info('The id for the next course is %s'%i)
        logging.info('The duration for the remaining courses is %s'%d)
        return i, d


child = OOPS('OOPS', 50436, 14)

logging.info('This is a test to see inheritance method call inside a child class.')

logging.info('Inheritance for a child class object child.show()')
logging.info(child.show())

logging.info(child.leftover())


