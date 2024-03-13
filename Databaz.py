class Exeption():
    def throw_exeption(self, text:str) -> str:
        raise NotImplementedError()
class NoExeption(Exeption):
    def throw_exeption(self, text:str) -> str:
        return text

class ExeptionChain(Exeption):
    next_exeption: Exeption()

    def __init__(self):
        self.next_exeption=NoExeption()

    def set_next(self, next_exe:Exeption):
        self.next_exeption=next_exe

    def throw_exeption(self, text:str) -> str:
        t = self.do_exeption_conc(text)
        return self.next_exeption.throw_exeption(t)

    def do_exeption_conc(self, text:str) -> str:
        raise NotImplementedError()

class AvExeption(ExeptionChain):
    def do_exeption_conc(self, text:str) -> str:
        print("av")
        return "avexeprtion"

class AuExeption(ExeptionChain):
    def do_exeption_conc(self, text:str) -> str:
        print("ai")
        return "auexeption"

class InExeption(ExeptionChain):

    def do_exeption_conc(self, text:str) -> str:
        print("int")
        return "inexeption"

av = AvExeption()
au = AuExeption()
ie = InExeption()

av.set_next(au)
au.set_next(ie)

print(av.throw_exeption('test'))