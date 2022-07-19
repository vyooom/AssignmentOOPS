import logging
logging.basicConfig(filename='logTask_100_polymorph01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Polymorphism :- Example - 01')

class IneuronOOPS:
    """Using initialization function."""

    def __init__(self):
        self.course = 'This is OOPS course.'
        logging.info('This is a initialization function with course IneuronOOPS.')

class IneuronJS:
    """Using initialization function."""

    def __init__(self):
        self.course = 'This is Javascript course.'
        logging.info('This is a initialization function with course IneuronJS.')

a = IneuronOOPS()
b = IneuronJS()

logging.info(a.course)
logging.info(b.course)
