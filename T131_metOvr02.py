import logging
logging.basicConfig(filename='logTask_131_methodOver02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Method OverRidding :- Example:- 02')

class Ineuron:
    '''Class for overridding examples.'''
    def __init__(self):
        self.intro = 'iNeuron is the parent platform.'

    def show(self):
        logging.info(self.intro)
        logging.info('iNeuron provides job assistance in few courses.')

class FSDS(Ineuron):
    '''Child class for overridding example.'''
    def __init__(self):
        super().__init__()
        self.intro = 'FSDS is a course at iNeuron'

    def show(self):
        super().show()
        logging.info('FSDS is job assistance program.')

a = Ineuron()
b = FSDS()
a.show()
b.show()


