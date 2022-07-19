import logging
logging.basicConfig(filename='logTask_033_construct04',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Constructor :- Example:- 04')
logging.info('Example of a constructor with inheritance.')

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

class FSDS(Ineuron):
    def __init__(self, a):
        super().__init__(a)

a = FSDS('Full Stack Data Science')
a.show()
