
class Challenge:
    description = 'Easy challenge which wants uppercase input'

    def generate(self):
        return 'uppercaseme'

    def parse(self, line):
        return line.upper()

