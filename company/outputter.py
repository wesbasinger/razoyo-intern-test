import os

class Outputter(object):

    def __init__(self, load):

        self.load = load

    def write(self, path):

        f = open(path, 'w')

        f.write(self.load)

        f.close()
