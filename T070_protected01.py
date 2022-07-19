import logging
logging.basicConfig(filename='logTask_070_protected01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Protected :- Example - 01')

class Ineuron:
    '''First example of Protected Object'''
    def __init__(self,name):
        try:
            if type(name) == str:
                self._name = name.title()
            else:
                raise Exception

        except:
            logging.error('Initialization needs a string.')


a = Ineuron('abhishek')
logging.info(a._name)
logging.info('My name is %s.'%a._name)


b = Ineuron(123)
logging.info(b._name)
logging.info('My name is %s.'%b._name)

