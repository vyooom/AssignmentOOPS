import logging
logging.basicConfig(filename='logTask_132_methodOver03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Method OverRidding :- Example:- 03')

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

    def show(self, job = 1):
        super().show()
        try:
            if type(job) == str:
                logging.info('FSDS provides job assistance for job in %s.'%job)
            elif type(job) == int:
                logging.info('FSDS provides job assistance in %s companies.'%job)
            else:
                raise ValueError
        except:
            logging.error('Please enter a string or an integer.')
            pass

a = Ineuron()
b = FSDS()
a.show()
b.show('ABC')
b.show(3)
b.show()
b.show(2.5)
