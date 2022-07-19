import logging
logging.basicConfig(filename='logTask_102_polymorph03',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Polymorphism :- Example - 03')

class Ineuron():
    """Parent class with a method 'intro'."""
    def intro(self):
        logging.info('Ineuron is a e-Education platform.')

class FSDS(Ineuron):
    """Child class with a method 'intro'."""
    def intro(self):
        logging.info('FSDS is a data science bootcamp at Ineuron.')

a = Ineuron()
a.intro()
b = FSDS()
b.intro()
