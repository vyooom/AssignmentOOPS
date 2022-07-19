import logging
logging.basicConfig(filename='logTask_133_methodOver04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Method OverRidding :- Example:- 04')

class Ineuron:
    '''Class for overridding examples.'''
    def __init__(self):
        self.intro = 'iNeuron is the parent platform.'

    def show(self):
        logging.info(self.intro)


class FSDS(Ineuron):
    def show(self):
        super().show()
        logging.info('FSDS is a 12 month course.')

a = Ineuron()
a.show()
b = FSDS()
b.show()
