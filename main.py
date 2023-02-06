from dddRepository import DDDRepository
from ddd import DDD
from userInterface import UserInterface

dddrepository = DDDRepository()
dddrepository.AdicionarDDD(DDD(21, "Rio de Janeiro"))
dddrepository.AdicionarDDD(DDD(32, "Juiz de Fora"))
dddrepository.AdicionarDDD(DDD(19, "Campinas"))
dddrepository.AdicionarDDD(DDD(27, "Vitória"))
dddrepository.AdicionarDDD(DDD(31, "Belo Horizonte"))
dddrepository.AdicionarDDD(DDD(61, "Brasília"))
dddrepository.AdicionarDDD(DDD(71, "Salvador"))
dddrepository.AdicionarDDD(DDD(11, "São Paulo"))
print(dddrepository)
UserInterface = UserInterface(dddrepository)

while True:
    result = UserInterface.ddduser()
    if (result == "DDD não encontrado!"):
        print(result)
        break
    else:
        print(result)