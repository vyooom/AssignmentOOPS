import logging
logging.basicConfig(filename='logTask_011_class02',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Concept Class :- Example - 02')


class ineuron:

    def __init__(self, a):
        self.a = a

    def attributes(self):
        if self.a == "fsds":
            logging.info('I am a %s student & I am learning data science.'%self.a)
        elif self.a == "javascript":
            logging.info('I am a %s student & I am learning web development.'%self.a)
        elif self.a == "data analytics":
            logging.info('I am a %s student & I am interested in analytics.'%self.a)
        else:
            logging.info('I am a %s student.'%self.a)



abhishek = ineuron("fsds")
abhishek.attributes()

suman = ineuron("statistics")
suman.attributes()

jason = ineuron("javascript")
jason.attributes()
