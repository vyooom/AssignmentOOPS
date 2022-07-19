import logging
logging.basicConfig(filename='logTask_030_construct01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Constructor :- Example:- 01')
logging.info('Example of a default constructor.')

class Ineuron:
    intro = 'iNeuron is a e-Education platform.'

a = Ineuron()
logging.info(a.intro)


