import logging
logging.basicConfig(filename='logTask_032_construct03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Constructor :- Example:- 03')
logging.info('Example of a constructor with parameter.')

class Ineuron:
    def __init__(self, a):
        try:
            if type(a) == str:
                self.a = 'iNeuron offers courses in: ' + a
            else:
                raise Exception
        except:
            logging.error('Please enter a valid string.')
            pass

    def show(self):
        logging.info(self.a)

a = Ineuron('Full Stack Data Science')
a.show()
