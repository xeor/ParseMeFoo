import random
import re

class Challenge:
    author = 'Lars Solberg'
    description = 'A challenge where you need to print numbers that matches an expression'

    def help(self):
        return \
            'Match every number that matches something like "1234.44", 4 numbers first (between 1000 and 4999), then a dot, and then two numbers from 00 to 99\n' \
            'The matching entries should be returned with a space-separated list..\n' \
            'Lines that doesnt match at all should be sent back as empty lines'

    def generate(self):
        def getOutput(correct=False):
            if correct:
                return '%s.%s' % (str(random.randint(1000, 4999)), str(random.randint(00,99)))

            nonCorrectType = random.randint(0,4)

            if nonCorrectType == 0: return '%s.%s' % (str(random.randint(0,999)), str(random.randint(00,99)))
            if nonCorrectType == 1: return '%s' % str(random.randint(1000,4999))
            if nonCorrectType == 2: return '%s,%s' % (str(random.randint(1000, 4999)), str(random.randint(00,99)))
            if nonCorrectType == 3: return '%s.%s' % (str(random.randint(5000, 9999)), str(random.randint(00,99)))
            return 'a string'

        output = []
        for i in range(8):
            genCorrect = True if random.randint(0,3) == 1 else False
            output.append(getOutput(genCorrect))


        return ' '.join(output)

    def parse(self, line):
        matching = re.findall(r'[1-4][0-9]{3}\.[0-9]{2}', line)
        return ' '.join(matching)
