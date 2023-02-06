from dddRepository import DDDRepository


class UserInterface: 
    def __init__(self, dddrepository: DDDRepository) -> None:
        self.dddrepository = dddrepository

    def userinput(self) -> int:
        result = int(input("Informe o DDD para saber a cidade desejada: "))
        return result

    def ddduser(self) -> str:
        ddd = self.userinput()

        if (self.dddrepository.VerificarDDD(ddd) == False):
            return "DDD NÃO ENCONTRADO!"

        return self.dddrepository.getDDD(ddd)
