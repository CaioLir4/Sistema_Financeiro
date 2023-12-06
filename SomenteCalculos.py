from datetime import date

#Criando o cade de Calendario
def switch_case(month):
    switch = {
        1: 31,  # janeiro
        2: 29 if date.today().year % 4 == 0 else 28,  # fevereiro
        3: 31,  # março
        4: 30,  # abril
        5: 31,  # maio
        6: 30,  # junho
        7: 31,  # julho
        8: 31,  # agosto
        9: 30,  # setembro
        10: 31, # outubro
        11: 30, # novembro
        12: 31, # dezembro
    }
    return switch.get(month, "Erro: Mês inválido")
data_hoje = date.today()
mes_cont = switch_case(data_hoje.month)

#VALORES DOS PLANOS
def plan1 ():
    return 110/30
def plan2 ():
    return 130/30
def plan3 ():
    return 160/30
def plan4 ():
    return 210/30


#FUNÇÕES DE CACULO DE VENCIMENTO
def Calcularven1(pAtual, pNovo):
    #NÃO IMPORTA O MOMENTO EM QUE ENTRA EM CONTATO, É SEMPRE RETIRADO 1 DIA DO PLANO ATUAL
    if (pAtual == 1 and pNovo == 2):
        Day = data_hoje.day - 1
        DayPlAtual = plan1() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan2() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 3):
        Day = data_hoje.day - 1
        DayPlAtual = plan1() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan3() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 4):
        Day = data_hoje.day - 1
        DayPlAtual = plan1() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan4() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 1):
        Day = data_hoje.day - 1
        DayPlAtual = plan2() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan1() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 3):
        Day = data_hoje.day - 1
        DayPlAtual = plan2() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan3() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 4):
        Day = data_hoje.day - 1
        DayPlAtual = plan2() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan4() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 1):
        Day = data_hoje.day - 1
        DayPlAtual = plan3() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan1() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 2):
        Day = data_hoje.day - 1
        DayPlAtual = plan3() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan2() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 4):
        Day = data_hoje.day - 1
        DayPlAtual = plan3() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan4() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 1):
        Day = data_hoje.day - 1
        DayPlAtual = plan4() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan1() * (31 - data_hoje.day)

        return Day,DayPlAtual , DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 2):
        Day = data_hoje.day - 1
        DayPlAtual = plan4() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan2() * (31 - data_hoje.day)

        return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 3):
        Day = data_hoje.day - 1
        DayPlAtual = plan4() * (data_hoje.day - 1)
        DayNovo = 31 - data_hoje.day
        DayPlNovo = plan3() * (31 - data_hoje.day)

        return Day, DayPlAtual, DayNovo, DayPlNovo

def Calcularven2(pAtual, pNovo):
    if (pAtual == 1 and pNovo == 2):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan1()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan1()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan1()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan1()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan1()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan1()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan2()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan2()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan2()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan2()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan2()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan2()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan3()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan3()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 2):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan3()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan3()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan3()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan3()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 2):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo

def Calcularven3(pAtual, pNovo):
    if (pAtual == 1 and pNovo == 2):
         # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual =  (data_hoje.day + 9) * plan1()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan1()
            DayNovo = (30 - (data_hoje.day - 20)) * plan2()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * plan1()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan1()
            DayNovo = (30 - (data_hoje.day - 20)) * plan3()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 1 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan1()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan1()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * plan2()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan2()
            DayNovo = (30 - (data_hoje.day - 20)) * plan1()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * plan2()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan2()
            DayNovo = (30 - (data_hoje.day - 20)) * plan3()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 2 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan2()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan2()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * plan3()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan3()
            DayNovo = (30 - (data_hoje.day - 20)) * plan1()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 2):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual = (data_hoje.day + 9) * plan3()
            DayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo

            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * plan3()
            DayNovo = (30 - (data_hoje.day - 20)) * plan2()
            DayPlNovo = 30 - (data_hoje.day - 20)

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 3 and pNovo == 4):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan3()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan3()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan4()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 1):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan1()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 2):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan2()

            return Day, DayPlAtual, DayNovo, DayPlNovo
    if (pAtual == 4 and pNovo == 3):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * plan4()
            DayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        if data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * plan4()
            DayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * plan3()

            return Day, DayPlAtual, DayNovo, DayPlNovo


#SWITCH PARA VENCIMENTO
def switch_venc(pVen):

    switch = {
        5: Calcularven1(pAtual,pNovo),  # 250
        10: Calcularven1(pAtual, pNovo),  # 250

        15: Calcularven2(pAtual,pNovo),  # 350
        20: Calcularven2(pAtual, pNovo),  # 350

        25: Calcularven3(pAtual,pNovo),  # 450
        30: Calcularven3(pAtual, pNovo),  # 450

    }
    return switch.get(pVen, "Erro: Mês inválido")


#ENTRADA DE DADOS
pAtual = int(input("Qual seu plano Atual?: "))
pNovo = int(input("Qual seu plano Novo?: "))
pVen = int(input("Qual vencimento?(05,10,15,20,25 ou 30): "))

#SAIDA DE DADOS
r = switch_venc(pVen)
print(r)




