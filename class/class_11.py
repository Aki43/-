import string


class Alphabet():
    def __init__(self, lang, letters):
        self.lang = lang  # язык
        self.letters = letters  # список букв

    def print(self):
        print(self.letters)
        # return alfovit

    def letters_num(self):
        len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_letters)

    def is_en_letter(self, bykva):
        self.bykva = bykva
        if bykva in string.ascii_letters:
            return True
        else:
            return False

    def letters_num(self):
        aa = self.__letters_num
        return aa  # return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'My name is Slim Shady'


if __name__ == '__main__':
    lp = EngAlphabet()
    lp.print()
    print(lp.letters_num())
    print(lp.is_en_letter('F'))
    print(lp.is_en_letter('щ'))
    print(lp.example())
