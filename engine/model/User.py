import json

class User:
    def __init__(self, funcional, racf, fullname):
        self.funcional = funcional
        self.racf = racf.lower()
        self.fullname = fullname.title()
        first_name = fullname.split()[0]
        second_name = fullname.split()[1]
        self.name = (first_name + ' ' + second_name).title()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)