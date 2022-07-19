import logging
logging.basicConfig(filename='logTask_111_package02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Package :- Example - 02')

'''We have made a second package and we will call it here, to display its functionalities.'''

from T111_package import blog
from T111_package import job
from T111_package import numberCourse

a = blog.blogIneuron()
b = job.JobIneuron()
c = numberCourse.courseIneuron()

a.updateBlog(5)
k = a.showBlog()
logging.info('Current no of blogs is %s'%k)
a.updateBlog(2)
k = a.showBlog()
logging.info('Current no of blogs is %s'%k)

b.updateJob('Amazon')
n = b.showJob()
logging.info('My job is in %s'%n)

c.updateCourse(2)
l = c.showCourse()
logging.info('The current no. of courses attended is %s'%l)
c.updateCourse(3)
l = c.showCourse()
logging.info('The current no. of courses attended is %s'%l)

