from ddd import DDD

class DDDRepository:

    def __init__(self) -> None:
        self.lista_cidades: DDD = []

    def AdicionarDDD(self, ddd: DDD) -> None:
        self.lista_cidades.append(ddd)


    def getDDD(self, ddd: int) -> str:
        for ddd in self.lista_cidades:
            if (ddd == ddd.ddd):
                return ddd.cidade
        

    def VerificarDDD(self, ddd: int) -> bool:
        for ddd in self.lista_cidades:
            if (ddd == ddd.ddd):
                return True

        return False
    def __str__(self) -> str:
        formatText = "{0:<10}-{1:<10}\n"
        menu = formatText.format("DDD", "nome da cidade")

        for ddd in self.lista_cidades:
            menu += formatText.format(ddd.ddd, ddd.cidade)

        return menu