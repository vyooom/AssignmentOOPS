import logging
logging.basicConfig(filename='logTask_050_private01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Private :- Example - 01')

class Ineuron:
    '''First example of Private Object'''
    def __init__(self,name):
        try:
            if type(name) == str:
                self.__name = name.title()
            else:
                raise Exception

        except:
            logging.error('Initialization needs a string.')


a = Ineuron('abhishek')
logging.info(a._Ineuron__name)
logging.info('My name is %s.'%a._Ineuron__name)



