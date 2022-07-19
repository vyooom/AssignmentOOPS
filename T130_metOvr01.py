import logging
logging.basicConfig(filename='logTask_130_methodOver01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Method OverRidding :- Example:- 01')

class Ineuron:
    '''Class for overridding examples.'''
    def __init__(self):
        self.intro = 'iNeuron is the parent platform.'

    def show(self):
        logging.info(self.intro)

class FSDS(Ineuron):
    '''Child class for overridding example.'''
    def __init__(self):
        super().__init__()
        self.intro = 'FSDS is a course at iNeuron'


a = Ineuron()
b = FSDS()
a.show()
b.show()

