import logging
logging.basicConfig(filename='logTask_015_class06',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 06')

class IneuronToDo:
    '''A class to provide assignments of a student.'''

    def __init__(self, course):
        self.course = course.lower()
        self.fsds = ['affiliates', 'blog', 'internship', 'job']
        self.analytics = ['affiliates', 'blog', 'internship']
        self.javascript = ['blog', 'internship', 'hacking']


    def todoList(self):
        a = self.course
        try:
            if a == 'fsds':
                logging.info('The todo list for FSDS are: %s'%(str(self.fsds)))

            elif a == 'analytics':
                logging.info('The todo list for Analytics are: %s'%(str(self.analytics)))

            elif a == 'javascript':
                logging.info('The todo list for Javascript are: %s'%(str(self.javascript)))

            else:
                logging.info('Todo list not defined yet!')

        except:
            raise Exception


ajay = IneuronToDo('analytics')
ajay.todoList()

sunny = IneuronToDo('fsds')
sunny.todoList()

shekhar = IneuronToDo('python')
shekhar.todoList()

