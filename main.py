import calendar
from datetime import date
import tkinter as tk
from tkinter import ttk


# Criando o Calendario que não serviu pra krlh nenhum
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
        10: 31,  # outubro
        11: 30,  # novembro
        12: 31,  # dezembro

    }
    data_hoje = date.today()
    mes_cont = switch_case(data_hoje.month)
    return switch.get(month, "Erro: Mês inválido")

# VALORES DOS PLANOS
def plan250():
    return 110 / 30
def plan350():
    return 130 / 30
def plan450():
    return 160 / 30
def plan600():
    return 210 / 30

data_hoje = date.today()  ##PEGANDO LOGO A DATA DE HOJE PRA SAPORRA TODA

# FUNÇÕES DE CACULO DE VENCIMENTO
def Calcularven1(pAtual, pNovo):
    if data_hoje.day != 1:
            Day = data_hoje.day - 1
            DayPlAtual = globals()[f"plan{pAtual}"]() * (data_hoje.day - 1)
            RestanteDayNovo = 31 - data_hoje.day
            DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month, 1)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, Day)
            AteBr = Ate.strftime("%d/%m/%Y")

            # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
            SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
            FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "
            resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
            resultado_text.insert(tk.END, r)
    else:
        RestanteDayNovo = 31 - data_hoje.day
        DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

        # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
        SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} dias totalizando: {DayPlNovo:.2f}.\nO valor final será: {DayPlNovo:.2f}.\nCom 10% será: {DayPlNovo - (DayPlNovo * 0.1):.2f}.\nDesconto de: {DayPlNovo * 0.1:.2f} "
        resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        resultado_text.insert(tk.END, r)

    return "FIM"
def Calcularven2(pAtual, pNovo):
    # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
    if data_hoje.day <= 10:
        Day = data_hoje.day + 19
        DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
        RestanteDayNovo = 31 - (data_hoje.day + 20)
        DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

        ValorTotal = DayPlAtual + DayPlNovo

        IniConsumo = date(date.today().year, date.today().month - 1, 11)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
        Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
        AteBr = Ate.strftime("%d/%m/%Y")

        FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "
        resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        resultado_text.insert(tk.END, r)
        return "FIM"
    # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
    elif data_hoje.day >= 10:
        Day = data_hoje.day - 10
        DayPlAtual = (data_hoje.day - 10) * globals()[f"plan{pAtual}"]()
        RestanteDayNovo = 30 - (data_hoje.day - 10)
        DayPlNovo = (30 - (data_hoje.day - 10)) * globals()[f"plan{pNovo}"]()

        ValorTotal = DayPlAtual + DayPlNovo

        IniConsumo = date(date.today().year, date.today().month, 11)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
        Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
        AteBr = Ate.strftime("%d/%m/%Y")

        ProxAtual = (data_hoje.month % 12) + 1
        FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"
        resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        resultado_text.insert(tk.END, r)
        return "FIM"
def Calcularven3(pAtual, pNovo):
    # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
    if data_hoje.day <= 20:
        Day = data_hoje.day + 9
        DayPlAtual = (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
        RestanteDayNovo = 31 - (data_hoje.day + 10)
        DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

        ValorTotal = DayPlAtual + DayPlNovo

        IniConsumo = date(date.today().year, date.today().month - 1, 21)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
        Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
        AteBr = Ate.strftime("%d/%m/%Y")

        FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "
        resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        resultado_text.insert(tk.END, r)
        return "FIM"


    # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
    elif data_hoje.day >= 20:
        Day = data_hoje.day - 20
        DayPlAtual = (data_hoje.day - 20) * globals()[f"plan{pAtual}"]()
        RestanteDayNovo = 30 - (data_hoje.day - 20)
        DayPlNovo = (30 - (data_hoje.day - 20)) * globals()[f"plan{pNovo}"]()

        ValorTotal = DayPlAtual + DayPlNovo

        IniConsumo = date(date.today().year, date.today().month, 21)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
        Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
        AteBr = Ate.strftime("%d/%m/%Y")

        ProxAtual = (data_hoje.month % 12) + 1
        FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 20)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "
        resultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        resultado_text.insert(tk.END, r)
        return "FIM"
def venc(pVen, pAtual, pNovo):
        if pVen in ["5", "10"]:
            return Calcularven1(pAtual, pNovo)  # VENCIMENTO 5 OU 10
        elif pVen in ["15", "20"]:
            return Calcularven2(pAtual, pNovo)  # VENCIMENTO 15 OU 20
        elif pVen in ["25", "30"]:
            return Calcularven3(pAtual, pNovo)  # VENCIMENTO 25 OU 30
        else:
            return "Opção de vencimento inválida"
def MudarVen(vAtual, vNovo,vPlano):

    # QUANTIDADE DE DIAS NO MÊS

    quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]

    # PROXIMO MÊS

    ProxAtual = (data_hoje.month % 12) + 1

    # CICLO DE 01 ATÉ 30

    IniVenc01 = date(date.today().year, date.today().month, 1)
    IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
    FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, date.today().month, quantidade_dias)
    FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

    # CICLO DE 11 ATÉ 10

    IniVenc11 = date(date.today().year, date.today().month, 11)
    IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
    FinalVenc10 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 10)
    FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

    # CICLO DE 21 ATÉ 20

    IniVenc21 = date(date.today().year, date.today().month, 21)
    IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
    FinalVenc20 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 20)
    FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

    # CONDIÇÕES DE TROCA DE VENCIMENTO

    if (vAtual == '5' or vAtual == '10') and (vNovo == '5' or vNovo == '10'):
        r = f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    if (vAtual == '5' or vAtual == '10') and (vNovo == '15' or vNovo == '20'):
        QtdDias = FinalVenc10 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc01Br} -- {FinalVenc10Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,10).strftime('%d/%m/%Y')}. São {QtdDias.days-30} dias -- totalizando: {(QtdDias.days-30) * globals()[f'plan{vPlano}']():.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    elif (vAtual == '5' or vAtual == '10') and (vNovo == '25' or vNovo == '30'):
        QtdDias = FinalVenc20 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc01Br} -- {FinalVenc20Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {QtdDias.days-30} dias -- totalizando: {(QtdDias.days-30) * globals()[f'plan{vPlano}']():.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    # VENCIMENTO 15 OU 20

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '15' or vNovo == '20'):
        r = f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '25' or vNovo == '30'):
        Qtd = 40
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nVencimento mais proximo:\n{IniVenc11Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- totalizando:  {(Qtd-30) * globals()[f'plan{vPlano}']():.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    elif (vAtual == '15' or vAtual == '20') and (vNovo == '5' or vNovo == '10'):
        Qtd = 20
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc11Br} -- {FinalVenc30Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    # VENCIMENTO 25 OU 30

    elif (vAtual == '25' or vAtual == '30') and (vNovo == '25' or vNovo == '30'):
        r = f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    elif (vAtual == '25' or vAtual == '30') and (vNovo == '15' or vNovo == '20'):
        Qtd = 20
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc21Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)


    elif (vAtual == '25' or vAtual == '30') and (vNovo == '5' or vNovo == '10'):
        Qtd = 10
        Valor = Qtd * globals()[f"plan{vPlano}"]()
        r = f"{IniVenc21Br} -- {FinalVenc30Br}. São {Qtd} dias -- totalizando: {Valor:.2f}"
        vresultado_text.delete(1.0, tk.END)  # Limpar o conteúdo atual
        vresultado_text.insert(tk.END, r)

    return "FIM"


'''
Escolha = int(input("Deseja mudar de vencimento?:1(SIM) 2(NÃO)"))
if Escolha == 1:
    while True:
        pVenNovo = int(input("Qual Novo vencimento?(05, 10, 15, 20, 25 ou 30): "))
        if pVenNovo in {5, 10, 15, 20, 25, 30}:
            print(MudarVen(pVen, pVenNovo))
            break
        else:
            print("Por favor, insira um vencimento válido.")
else:print("FIM")'''
# ENTRADA DE DADOS
Janela = tk.Tk()
Janela.title("SISTEMA FINANCEIRO")
Janela.geometry("550x600")

pAtual = tk.StringVar()
pNovo = tk.StringVar()
pVen = tk.StringVar()

pAtualop = ['250', '350', '450', '600']
pNovoop = ['250', '350', '450', '600']
pVenop = ['5', '10', '15', '20', '25', '30']

Frame1 = tk.Frame(Janela, borderwidth=2, relief="solid")
Frame1.pack(side="left", padx=10, pady=10)

Op1 = ttk.Combobox(Frame1,textvariable=pAtual, values=pAtualop, width=35)
Op1.set(pAtualop[0])
Op1.pack(pady=10)
Op2 = ttk.Combobox( Frame1,textvariable=pNovo, values=pNovoop, width=35)
Op2.set(pNovoop[0])
Op2.pack(pady=10)
Op3 = ttk.Combobox(Frame1, textvariable=pVen, values=pVenop, width=35)
Op3.set(pVenop[0])
Op3.pack(pady=10)

resultado_text = tk.Text(Frame1, wrap=tk.WORD, width=30, height=20)
resultado_text.pack(pady=10)
calcular_botao = tk.Button(Frame1, text="Calcular", command=lambda: venc(pVen.get(), pAtual.get(),pNovo.get()))
calcular_botao.pack(pady=10)
#====================================================================================================================

Frame2 = tk.Frame(Janela, borderwidth=2, relief="solid")
Frame2.pack(side="left", padx=10, pady=10)

vAtual = tk.StringVar()
vNovo = tk.StringVar()
vPlano = tk.StringVar()

Plano = ['250', '350', '450', '600']
vNovoop = ['5', '10', '15', '20', '25', '30']
vAtualop= ['5', '10', '15', '20', '25', '30']

OpV1 = ttk.Combobox(Frame2,textvariable=vAtual, values=vAtualop, width=35)
OpV1.set(vAtualop[0])
OpV1.pack(pady=10)
OpV2 = ttk.Combobox( Frame2,textvariable=vNovo, values=vNovoop, width=35)
OpV2.set(vNovoop[0])
OpV2.pack(pady=10)
OpV3 = ttk.Combobox(Frame2, textvariable=vPlano, values=Plano, width=35)
OpV3.set(Plano[0])
OpV3.pack(pady=10)

vresultado_text = tk.Text(Frame2, wrap=tk.WORD, width=30, height=20)
vresultado_text.pack(pady=10)

vcalcular_botao = tk.Button(Frame2, text="Calcular", command=lambda: MudarVen(vAtual.get(),vNovo.get(),vPlano.get()))
vcalcular_botao.pack(pady=10)


Janela.mainloop()



