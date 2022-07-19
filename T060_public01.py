import logging
logging.basicConfig(filename='logTask_060_public01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Public :- Example - 01')

class Ineuron:
    '''First example of Public Object'''
    def __init__(self,name):
        try:
            if type(name) == str:
                self.name = name.title()
            else:
                raise Exception

        except:
            logging.error('Initialization needs a string.')


a = Ineuron('abhishek')
logging.info(a.name)
logging.info('My name is %s.'%a.name)

b = Ineuron(123)
logging.info(b.name)
logging.info('My name is %s.'%b.name)

