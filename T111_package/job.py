class JobIneuron:
    def __init__(self):
        self.job = None

    def updateJob(self, job):
        self.job = job

    def showJob(self):
        return self.job