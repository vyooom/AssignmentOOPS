import logging
logging.basicConfig(filename='logTask_010_class01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 01')

class ineuron:
    intro = 'I am a student of iNeuron.'


a = ineuron()

t = a.intro

logging.info(t)