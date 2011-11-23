
class Challenge:
    description = 'Dummy challenge which outputs the solution'

    def help(self):
        return 'This is just a dummy challenge which does nothing. The stdout stream is the solution..'

    def generate(self):
        return 'dummy'

    def parse(self, line):
        return line

