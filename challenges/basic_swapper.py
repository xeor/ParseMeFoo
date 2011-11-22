import random
import string

class Challenge:
    author = 'Lars Solberg'
    description = 'A basic wordswap challenge'

    def generate(self):
        def genWord():
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
        return '%s %s' % (genWord(), genWord())

    def parse(self, line):
        line = line.split(' ')
        return '%s %s' % (line[1], line[0])
