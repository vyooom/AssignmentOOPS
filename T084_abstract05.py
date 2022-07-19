import logging
logging.basicConfig(filename='logTask_084_abstract05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Abstraction :- Example - 05')

class Ineuron:
    '''Initialization of class'''
    def __init__(self):
        self.intro = 'This is a iNeuron platform.'
        logging.info('This is a iNeuron platform.')

    def shout(self):
        logging.info('Please select a course.')

class FSDS(Ineuron):
    def shout(self):
        logging.info('This course is of 12 months duration.')

class JavaS(Ineuron):
    def shout(self):
        logging.info('This course is of 6 months course.')

a = Ineuron()
b = FSDS()
c = JavaS()

for i in (a,b,c):
    i.shout()




















