
def importacao01():
    print("Importacao 01")
    import utilitarios.matematica
    resultado = utilitarios.matematica.somar(1, 2)
    print(resultado)

def importacao02():
    print("Importacao 02")
    import utilitarios.matematica as utilmat
    resultado = utilmat.somar(1, 2)
    print(resultado)

def importacao03():
    print("Importacao 03")
    from utilitarios.matematica import somar
    resultado = somar(1, 2)
    print(resultado)


if __name__ == "__main__":
    importacao01()
    importacao02()
    importacao03()