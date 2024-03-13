class Databaze:
    log_and_pass = {
        'root': 'root777',
        'user': 'user_dva',
        'nothing': 'nothing_pass'
    }
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
        if baza.log_and_pass.get(baza.try_user) == None:
            print("AUTHENTICATE FAILED")
            return 0
        return baza


class InputExeption(ExeptionChain):
    def do_exeption_conc(self, baza: Databaze):
        return baza
