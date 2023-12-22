def calculadoraRankeada(vitoria, derrota):
    saldoVitorias = vitoria - derrota

    if saldoVitorias <= 10:
        nivel = 'Ferro'
    elif saldoVitorias <= 20:
        nivel = 'Bronze'
    elif saldoVitorias <= 50:
        nivel = 'Prata'
    elif saldoVitorias <= 80:
        nivel = 'Ouro'
    elif saldoVitorias <= 90:
        nivel = 'Diamante'
    elif saldoVitorias <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Imortal'
    return saldoVitorias, nivel

vitorias = int(input("Informe seu numero de vitorias: "))
derrotas = int(input("Informe seu numero de derrotas: "))

saldoVitorias, nivel = calculadoraRankeada(vitorias, derrotas)

print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")
