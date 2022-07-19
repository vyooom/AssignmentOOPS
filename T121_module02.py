import logging
logging.basicConfig(filename='logTask_121_module02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Module:- Example - 02')

import T120_module01 as mod1

a = mod1.internIneuron(6)
b = mod1.internIneuron(2)
c = mod1.internIneuron(-6)
d = mod1.internIneuron('gh')

logging.info(a)
logging.info(b)
logging.info(c)
logging.exception(d)


