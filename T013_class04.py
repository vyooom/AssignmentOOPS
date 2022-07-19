import logging
logging.basicConfig(filename='logTask_013_class04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 04')

class Student:
    ''' A universal student class with name and courses in string.'''

    def __init__(self, name, course):
        try:
            if type(name) == str and type(course) == str:
                self.name = name.title()
                self.course = course.title
        except:
            raise ValueError

    def intro(self):
        logging.info('My name is %s & I am an student of %s.'%(self.name, self.course))
        return 'My name is %s & I am an student of %s.'%(self.name, self.course)

class Ineuron(Student):
    '''A subclass of class Student. The inputs are name, course attended & internship'''

    def __init__(self, name, course, internship):
        super().__init__(name, course)
        try:
            if type(internship) == str:
                self.internship = internship.title()

        except:
            raise ValueError

    def intern(self):
        logging.info('I am doing an internship in %s.'%self.internship)
        return 'I am doing an internship in %s.'%self.internship



abhishek = Student('abhishek', 'data science')
abhishek.intro()

suman = Ineuron('suman', 'data science', 'meta')
suman.intro()
suman.intern()

