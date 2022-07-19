import logging
logging.basicConfig(filename='logTask_110_package01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Package Example :- Example - 01')

'''We have made a package and we will call it here, to display its functionalities.'''

from T110_package import name
from T110_package import rollNext
from T110_package import internship

x = name.Name('abhishek')
y = rollNext.RollNext(15)
z = internship.Internship(4)


logging.info(x.intro())
logging.info(z.intern())
logging.info(y.Roll())
