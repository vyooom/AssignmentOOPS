import logging
logging.basicConfig(filename='logTask_081_abstract02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Abstraction :- Example - 02')

class Ineuron:
    '''Second example of abstraction.'''
    def __init__(self, name, blog, internship):
        self.name = name
        self.blog = blog
        self.internship = internship
        l = []
        self.l = l
        self.l.append(self.internship)

    def showIntro(self):
        a = self.name
        b = self.blog
        c = self.l
        logging.info('My name is %s. I have written %s blogs & I have completed internships in following companies %s.'%(a,b,c))

    def updateBlog(self, num):
        try:
            if type(num) == int:
                logging.info('The initial number of blogs written is %s'%self.blog)
                self.blog += num
                logging.info('The updated number of blogs written is %s'%self.blog)
            else:
                raise ValueError
        except:
            logging.exception('Please enter a valid integer.')

    def updateIntern(self, abc):
        '''To update the internship.'''
        try:
            if type(abc) == str:
                logging.info('The initial list of internship is %s'%self.l)
                self.l.append(abc)
                logging.info('The updated list of internship is %s'%self.l)
            else:
                raise ValueError
        except:
            logging.exception('Please enter a valid string.')

a = Ineuron('abhi', 1, 'amazon')
a.showIntro()
a.updateBlog(8)
a.updateIntern('google')
a.showIntro()

