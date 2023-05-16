print("""[1, 2, 3, 4] VOTO NO RESPECTIVO CANDIDATO
[5] VOTO NULO 
[6] VOTO EM BRANCO
[0] FECHAR""")

voto = 0
c1, c2, c3, c4, nulo, branco = 0, 0, 0, 0, 0, 0

while voto != '0':
    voto = input('INSIRA SEU VOTO: ')
    if voto == '1':
        c1 += 1
    elif voto == '2':
        c2 += 1
    elif voto == '3':
        c3 += 1
    elif voto == '4':
        c4 += 1
    elif voto == '5':
        nulo += 1
    elif voto == '6':
        branco += 1
    else:
        break
print(f"""
RESUMO DOS VOTOS
C1    : {c1}
C2    : {c2}
C3    : {c3}
C4    : {c4}
NULO  : {nulo}
BRANCO: {branco}""")