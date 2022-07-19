import logging
logging.basicConfig(filename='logTask_080_abstract01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Abstraction :- Example - 01')

class Ineuron:
    '''First example of abstraction.'''

    def __init__(self, course):
        try:
            if type(course) == str:
                self.course = course.lower()
            else:
                raise Exception
        except:
            logging.error('Please enter a valid string.')

    def duration(self):
        '''Returns the duration of the course in months.'''
        a = self.course.upper()
        if a == 'FSDS':
            logging.info('%s : Duration = 12 months'%a)
            return 12

        elif a == 'JAVASCRIPT':
            logging.info('%s : Duration = 5 months'%a)
            return 5

        elif a == 'PYTHON':
            logging.info('%s : Duration = 2 months'%a)
            return 2

        else:
            logging.info('Duration not defined for this course.')
            return None


a = Ineuron('FSDS')
a.duration()

b = Ineuron('python')
b.duration()



