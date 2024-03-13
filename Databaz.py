class Databaze():
    user = ["root", "user_dva", "nothing"]
    password = ["root777", "users", "ayanami"]
    type = ["admin", "VIP", "classic"]
    try_user: str
    try_pass: str

    def __init__(self, _pass: str, _user: str):
        self.try_pass=_pass
        self.try_user=_user


class Exeption():
    def throw_exeption(self, text: str) -> str:
        raise NotImplementedError()


class NoExeption(Exeption):
    def throw_exeption(self, text: str) -> str:
        return text


class ExeptionChain(Exeption):
    next_exeption: Exeption()

    def __init__(self):
        self.next_exeption = NoExeption()

    def set_next(self, next_exe: Exeption):
        self.next_exeption = next_exe

    def throw_exeption(self, text: str) -> str:
        t = self.do_exeption_conc(text)
        return self.next_exeption.throw_exeption(t)

    def do_exeption_conc(self, text: str) -> str:
        raise NotImplementedError()


class AvtorizationExeption(ExeptionChain):
    def do_exeption_conc(self, text: str) -> str:

        return "avexeprtion"


class AuthenticateExeption(ExeptionChain):
    def do_exeption_conc(self, text: str) -> str:
        print("ai")
        return "auexeption"


class InputExeption(ExeptionChain):

    def do_exeption_conc(self, text: str) -> str:
        print("int")
        return "inexeption"

#
#av = AvtorizationExeption()
##au = AuthenticateExeption()
#ie = InputExeption()

#av.set_next(au)
#au.set_next(ie)

#print(av.throw_exeption('test'))
