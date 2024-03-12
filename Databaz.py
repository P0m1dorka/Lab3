class Exeption():
    def throw_exeption(self):
        print("somthing exeption")

class NoExeption(Exeption):
    def throw_exeption(self):
        print("no exeption")

class NextExeption(Exeption):
    next_exeption: Exeption()

    def __init__(self):
        self.next_exeption = NoExeption()

    def set_net_exeption(self, next_exe: Exeption):
        self.next_exeption = next_exe

    def throw_exeption(self):
        t = self.do_throw_exeption()
        return self.next_exeption.throw_exeption()
    def do_throw_exeption(self):
        raise NotImplementedError()
class AuthExepe(NextExeption):
    def throw_exeption(self):
        print("Authexepe")
class AvtorExepe(NextExeption):
    def throw_exeption(self):
        print("Avtexepe")
class InpExepe(NextExeption):
    def throw_exeption(self):
        print("Inpexepe")

ex_au = AuthExepe()
ex_av=AvtorExepe()
ex_in=InpExepe()

ex_in.set_net_exeption(ex_au)
ex_au.set_net_exeption(ex_av)

print(ex_in.throw_exeption())

