

# class Utilitarios:

#     def __init__(qualquevalorpodeserinformadoaqui):
#         qualquevalorpodeserinformadoaqui.x = 1

# u = Utilitarios()
# print(u.x)



def compararString(a, b):
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
            break
        i += 1
    return True

#
# Seu teste
#
cor1 = "laranja"
cor2 = "amarelo"
print(compararString(cor1, cor2))
assert compararString(cor1, cor1)