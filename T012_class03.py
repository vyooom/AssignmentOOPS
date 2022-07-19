import logging
logging.basicConfig(filename='logTask_012_class03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 03')


class ineuron:
    '''A class defined by student id with integer value and a student name with string value.'''
    def __init__(self, id, name):
        if type(id) == int and type(name) == str:
            self.id = id
            self.name = name.title()

    def prevStudent(self):
        alumni = self.id - 1
        return alumni

    def intro(self):
        i = self.prevStudent()
        logging.info('My name is %s. There are %s students having older enrollment than me.'%(self.name, i))


abhishek = ineuron(101, 'abhishek')
suman = ineuron(109, 'suman')

abhishek.intro()

suman.intro()

