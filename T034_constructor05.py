import logging
logging.basicConfig(filename='logTask_034_construct05',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Constructor :- Example:- 05')
logging.info('Example of an extra constructor.')

class Ineuron:
    def __init__(self):
        self.intro = 'This is the first constructor.'

    def __init__(self):
        self.intro = 'This is the second constructor.'


    def show(self):
        logging.info(self.intro)

a = Ineuron()
a.show()
