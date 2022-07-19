import logging
logging.basicConfig(filename='logTask_101_polymorph02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Polymorphism :- Example - 02')

class OOPS:
    """This is the first class."""
    def course(self):
        logging.info('OOPS Class.')


class Java:
    """Thi is the second class."""
    def course(self):
        logging.info('Java Class.')



def loger(obj):
    logging.info(obj.course())


a = OOPS()
b = Java()

loger(a)
loger(b)
