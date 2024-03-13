import sys


class Databaze:
    log_and_pass = {
        'root': 'root777',
        'user': 'user_dva',
        'nothing': 'nothing_pass'
    }
    commands_root = ['DROP', 'FORCE', 'CHECK', 'TEST']
    commands_user = ['CHECK', 'TEST']
    try_user: str
    try_pass: str

    def __init__(self, tryp: str, tryu: str):
        self.try_pass = tryp
        self.try_user = tryu


class Exeption:
    def throw_exeption(self, baza: Databaze) -> Databaze:
        raise NotImplementedError()


class NoExeption(Exeption):
    def throw_exeption(self, baza: Databaze) -> Databaze:
        return baza


class ExeptionChain(Exeption):
    next_exeption: Exeption()

    def __init__(self):
        self.next_exeption = NoExeption()

    def set_next(self, next_exe: Exeption):
        self.next_exeption = next_exe

    def throw_exeption(self, baza: Databaze):
        test = self.do_exeption_conc(baza)
        return self.next_exeption.throw_exeption(test)

    def do_exeption_conc(self, baza: Databaze) -> Databaze:
        raise NotImplementedError()


class AvtorizationExeption(ExeptionChain):
    def do_exeption_conc(self, baza: Databaze):
        return baza


class AuthenticateExeption(ExeptionChain):
    def do_exeption_conc(self, baza: Databaze):
        if baza.log_and_pass.get(baza.try_user) is None:
            print("AUTHENTICATE FAILED")
            return sys.exit()
        else:
            password = baza.log_and_pass.get(baza.try_user)
            if password != baza.try_pass:
                print("WRONG PASSWORD")
                return sys.exit()
        return baza


class InputExeption(ExeptionChain):
    def do_exeption_conc(self, baza: Databaze):
        try_command = input("Type your command")
        if baza.try_user == 'root':
            if try_command in baza.commands_root:
                return baza
            else:
                print("INCORRECT INPUT")
                return sys.exit()
        elif baza.try_user == 'user':
            if try_command in baza.commands_user:
                return baza
            else:
                print("INCORRECT INPUT")
                return sys.exit()
        else:
            return baza
