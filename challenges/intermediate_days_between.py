import datetime
import random
import re

class Challenge:
    author = 'Lars Solberg'
    description = 'Calculate the how long this event happend on each line.'

    def help(self):
        return 'Calculate the days it took between it happened. The answer should be in days..'

    def generate(self):
        earlier = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(15000,40000))
        later = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(2000,13000))
        earlier = earlier.strftime('%Y-%m-%d %H:%M:%S')
        later = later.strftime('%Y-%m-%d %H:%M:%S')
        return 'Happend between %s and %s' % (earlier, later)

    def parse(self, line):
        (earlierStr, laterStr) = re.findall(r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2} [0-9:]{8}', line)
        diff = datetime.datetime.strptime(laterStr, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(earlierStr, '%Y-%m-%d %H:%M:%S')
        return 'It took %s days' % diff.days
