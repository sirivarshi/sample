class capital:
    def __init__(self,string):
        self.string = string
    def convert_to_lowercase_letter(self):
        result = self.string.casefold()
        return "the conversion of string is",result
class model(capital):
    def __init__(self,string):
        super().__init__(string)
    def padding(self):
        return self.string.center(8,"*")

class count(model):
    def __init__(self,string,sub):
        self.sub = sub
        super().__init__(string)
    def count_specified_string(self):
        return self.string.count(self.sub)