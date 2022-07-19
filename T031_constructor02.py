import logging
logging.basicConfig(filename='logTask_031_construct02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Constructor :- Example:- 02')
logging.info('Example of a constructor without parameter.')

class Ineuron:
    def __init__(self):
        self.intro = 'iNeuron has many courses.'

    def show(self):
        logging.info(self.intro)

a = Ineuron()
a.show()
