import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import pandas as pd

# funções janelas
def criar_conta():
    janela.option_add("*Font", "Courier 12")

    # ocultando os widgets da pagina
    mensagem_inicial.grid_forget()
    botao_criar.grid_forget()
    botao_editar.grid_forget()
    botao_excluir.grid_forget()
    botao_arquivo.grid_forget()
    botao_relatorio.grid_forget()
    botao_info.grid_forget()

    #mostrando os widgets da página
    entry_nome_conta.focus_set()
    label_titulo.grid(row=0, column=1)
    entry_nome_conta.grid(row=2, column=0, pady=(0, 1), padx=(15, 0))
    label_valor_conta.grid(row=1, column=1, pady=(15, 1), padx=(1, 0))
    entry_valor_conta.grid(row=2, column=1, pady=(0, 1), padx=(15, 0))
    label_nome_conta.grid(row=1, column=0, pady=(0, 1), padx=(1, 0))
    label_parcelas_conta.grid(row=1, column=2, pady=(15, 1), padx=(1, 0))
    entry_parcelas_conta.grid(row=2, column=2, pady=(0, 1), padx=(15, 0))
    label_prioridade_conta.grid(row=4, column=0, pady=(15, 1), padx=(1, 0))
    combo_prioridade_conta.grid(row=5, column=0, pady=(0, 1), padx=(15, 0))
    label_parcatual_conta.grid(row=4, column=1, pady=(15, 1), padx=(1, 0))
    entry_parcatual_conta.grid(row=5, column=1, pady=(0, 1), padx=(15, 0))
    label_conta_paga.grid(row=4, column=2, pady=(15, 1), padx=(1, 0))
    radio_sim.grid(row=5, column=2)
    radio_nao.grid(row=6, column=2)
    label_opcoes_conta.grid(row=8, column=0, pady=(0, 1), padx=(15, 0))
    combo_opcoes_conta.grid(row=9, column=0, pady=(0, 1), padx=(15, 0))
    label_data_vencimento.grid(row=8, column=1, pady=(0, 1), padx=(15, 0))
    vencimento_conta.grid(row=9, column=1, pady=(0, 1), padx=(15, 0))
    botao_voltar.grid(row=10, column=5, pady=(0, 15), padx=(5, 15))
    botao_confirmar_criacao.grid(row=10, column=4, pady=(0, 15), padx=(0, 5))


def editar_conta():
    pass


def excluir_conta():
    pass


def selecionar_arquivo():
    caminho = askopenfilename(title='Selecione o arquivo')
    return caminho


def pagina_inicial():
    janela.option_add("*Font", "Courier 10")

    # ocultando os widgets da pagina
    label_titulo.grid_forget()
    entry_nome_conta.grid_forget()
    label_valor_conta.grid_forget()
    entry_valor_conta.grid_forget()
    label_nome_conta.grid_forget()
    label_parcelas_conta.grid_forget()
    entry_parcelas_conta.grid_forget()
    label_prioridade_conta.grid_forget()
    combo_prioridade_conta.grid_forget()
    label_parcatual_conta.grid_forget()
    entry_parcatual_conta.grid_forget()
    label_conta_paga.grid_forget()
    radio_sim.grid_forget()
    radio_nao.grid_forget()
    botao_voltar.grid_forget()
    botao_confirmar_criacao.grid_forget()
    vencimento_conta.grid_forget()
    label_data_vencimento.grid_forget()
    combo_opcoes_conta.grid_forget()
    label_opcoes_conta.grid_forget()
    entry_nome_conta.delete(0, tk.END)
    entry_valor_conta.delete(0, tk.END)
    label_erro_parcela.grid_forget()
    label_erro_prioridade.grid_forget()
    label_erro_nome.grid_forget()
    label_erro_opcoes.grid_forget()
    label_erro_valor.grid_forget()
    label_erro_opcoes.grid_forget()
    label_erro_parcatual.grid_forget()
    var_p.set('')
    var_o.set('')
    vencimento_conta.set_date(datetime.now())
    opcao_var.set('Não')
    entry_parcatual_conta.delete(0, 'end')
    entry_parcelas_conta.delete(0, 'end')
    entry_valor_conta.delete(0, 'end')
    entry_nome_conta.delete(0, 'end')


    # mostrando os widgets da página
    mensagem_inicial.grid(row=0, column=0, pady=(0, 15), padx=(15, 0))
    botao_criar.grid(row=1, column=0, pady=(0, 15), padx=(15, 0))
    botao_editar.grid(row=1, column=1, pady=(0, 15), padx=(0, 0))
    botao_excluir.grid(row=2, column=0, pady=(0, 15), padx=(15, 0))
    botao_arquivo.grid(row=2, column=1, pady=(0, 15), padx=(0, 15))
    botao_relatorio.grid(row=3, column=0, pady=(0, 15), padx=(0, 0))
    botao_info.grid(row=3, column=1, pady=(0, 15), padx=(0, 0))


def gerar_relatorio():
    pass


def pagina_ajuda():
    # precisa ter um sistema de barra de rolagem
    pass


# funções de validação de entrada de dados
def validar_valor_conta(texto):
    # Permitir apenas números, um único ponto ou uma única vírgula
    if texto.count('.') > 1 or texto.count(',') > 1:
        return False  # Mais de um ponto ou vírgula não é permitido
    if '.' in texto and ',' in texto:
        return False  # Não pode ter ponto e vírgula ao mesmo tempo
    return all(caracter.isdigit() or caracter in '.,' for caracter in texto)


def validar_numeros(texto):
    return all(caracter.isdigit() for caracter in texto)


def exibir_selecao():
    selecionado = opcao_var.get()
    return selecionado

def confirmar_criacao():
    global df_contas

    # validando o campo do nome da conta
    passou_nome, texto_nome = validar_texto(entry_nome_conta)
    if passou_nome:
        label_erro_nome.grid_forget()
    else:
        label_erro_nome.grid(row=3, column=0)

    # validando o campo de valor da conta
    passou_valor, valor = validar_decimal(entry_valor_conta)
    if passou_valor:
        label_erro_valor.grid_forget()
    else:
        label_erro_valor.grid(row=3, column=1)

    # validando o campo de qtde de parcelas
    passou_parcela, parcelas = validar_parcela(entry_parcelas_conta)
    if passou_parcela:
        label_erro_parcela.grid_forget()
    else:
        label_erro_parcela.grid(row=3, column=2)

    # validando o campo de prioridade
    passou_prioridade, prioridade = validar_drop(combo_prioridade_conta)
    if passou_prioridade:
        label_erro_prioridade.grid_forget()
    else:
        label_erro_prioridade.grid(row=6 , column=0)

    # validando o campo de opções
    passou_opcao, opcao = validar_drop(combo_opcoes_conta)
    if passou_opcao:
        label_erro_opcoes.grid_forget()
    else:
        label_erro_opcoes.grid(row=10, column=0)

    # validando o campo de parcela atual
    passou_paratual, parcatual = validar_parcela_atual(entry_parcatual_conta)
    if passou_paratual:
        label_erro_parcatual.grid_forget()
    else:
        label_erro_parcatual.grid(row=6, column=1)

    # pegando as datas
    data = pegar_data(vencimento_conta)

    # pegando o valor do radio button
    resposta_radio = pegar_pago(opcao_var)


    # limpando tudo quando está tudo certo
    if passou_nome and passou_valor and passou_parcela and passou_prioridade and passou_opcao and passou_paratual:
        entry_nome_conta.focus_set()
        entry_parcatual_conta.delete(0, 'end')
        entry_parcelas_conta.delete(0, 'end')
        entry_valor_conta.delete(0, 'end')
        entry_nome_conta.delete(0, 'end')
        var_p.set('')
        var_o.set('')
        vencimento_conta.set_date(datetime.now())
        opcao_var.set('Não')

        dicionario_contas = {'Nome Conta': texto_nome,
                             'Valor Conta': valor,
                             'Total Parcelas': parcelas,
                             'Prioridade': prioridade,
                             'Parcela Atual': parcatual,
                             'Paga': resposta_radio,
                             'Tipo da Conta': opcao,
                             'Vencimento da Conta': data}

        print(dicionario_contas)

        #adicionando a conta no df
        df_auxiliar = pd.DataFrame([dicionario_contas])
        df_contas = pd.concat([df_contas, df_auxiliar], ignore_index=True)

def validar_texto(widget):
    texto = widget.get()
    if texto:
        texto = texto.strip()
        texto = texto.capitalize()
        passou_t = True
    else:
        passou_t = False
    return passou_t, texto


def validar_decimal(widget):
    num = widget.get()
    if num:
        if ',' in num:
            num = num.replace(',','.')
        try:
            num = float(num)
            passou_n = True
        except:
            passou_n = False
    else:
        passou_n = False

    return passou_n, num


def validar_parcela(widget):
    num = widget.get()
    if num:
        passou_p = True
    else:
        passou_p = False

    return passou_p, num


def validar_drop(widget):
    opcao = widget.get()
    if opcao:
        passou_d = True
    else:
        passou_d = False

    return passou_d, opcao


def validar_parcela_atual(widget):
    parc_atual = widget.get()
    num = entry_parcelas_conta.get()
    if parc_atual > num:
        passou_pa = False
    else:
        passou_pa = True

    return passou_pa, parc_atual


def pegar_data(widget):
    data = widget.get_date()
    return data


def pegar_pago(widget):
    sim_nao = widget.get()
    return sim_nao

janela = tk.Tk()
janela.option_add("*Font", "Courier 10")
janela.configure(bg='#191920')
janela.title('Análise de Contas')
janela.iconbitmap('imagem_titulo.ico')

# pagina inicial
mensagem_inicial = tk.Label(text='Selecione o que deseja fazer', bg='#191920', fg='#fafafa')
mensagem_inicial.grid(row=0, column=0, pady=(0, 15), padx=(15,0))

botao_criar = tk.Button(text='Criar conta', command=criar_conta, bg='#393642', fg='#fafafa', relief='flat', bd=6,
                        activebackground='#393642', cursor='hand2')
botao_criar.grid(row=1, column=0, pady=(0, 15), padx=(15,0))

botao_editar = tk.Button(text='Editar conta', command=editar_conta, bg='#393642', fg='#fafafa', relief='flat', bd=6,
                        activebackground='#393642', cursor='hand2')
botao_editar.grid(row=1, column=1, pady=(0, 15), padx=(0,0))

botao_excluir = tk.Button(text='Excluir conta', command=excluir_conta, bg='#393642', fg='#fafafa', relief='flat',
                          bd=6, activebackground='#393642', cursor='hand2')
botao_excluir.grid(row=2, column=0, pady=(0,15), padx=(15,0))

botao_arquivo = tk.Button(text='Selecionar Arquivo', command=selecionar_arquivo, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')
botao_arquivo.grid(row=2, column=1, pady=(0,15), padx=(0,15))

botao_relatorio = tk.Button(text='Gerar Relatório', command=gerar_relatorio, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')
botao_relatorio.grid(row=3, column=0, pady=(0, 15), padx=(0, 0))

botao_info = tk.Button(text='Ajuda', command=pagina_ajuda, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')
botao_info.grid(row=3, column=1, pady=(0, 15), padx=(0, 0))

# pagina de criação da conta
label_titulo = tk.Label(text='Criar Conta', font=('Courier', 42), bg='#191920', fg='#fafafa')

label_nome_conta = tk.Label(text='Nome da Conta', bg='#191920', fg='#fafafa')
entry_nome_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa')
label_erro_nome = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')

label_valor_conta = tk.Label(text='Valor da Conta', bg='#191920', fg='#fafafa')
cmd_validar_valor = (janela.register(validar_valor_conta), "%P")
entry_valor_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                             validatecommand=cmd_validar_valor)
label_erro_valor = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')

label_parcelas_conta = tk.Label(text='Número de Parcelas', bg='#191920', fg='#fafafa')
cmd_validar_numero = (janela.register(validar_numeros), "%P")
entry_parcelas_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                                validatecommand=cmd_validar_numero)
label_erro_parcela = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')

prioridade_conta = ['Alta', 'Média', 'Baixa']
var_p = tk.StringVar()
label_prioridade_conta = tk.Label(text='Prioridade da Conta', bg='#191920', fg='#fafafa')
combo_prioridade_conta = ttk.Combobox(janela, values=prioridade_conta, state='readonly', textvariable=var_p)
label_erro_prioridade = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')

label_parcatual_conta = tk.Label(text='Parcela atual da Conta', bg='#191920', fg='#fafafa')
entry_parcatual_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                                 validatecommand=cmd_validar_numero)
label_erro_parcatual = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')


label_conta_paga = tk.Label(text='A Conta paga', bg='#191920', fg='#fafafa')

opcao_var = tk.StringVar(value='Não')
radio_sim = tk.Radiobutton(text='Sim', variable=opcao_var, value='Sim', command=exibir_selecao,
                           bg='#191920', fg='#fafafa', selectcolor='#191920')
radio_nao = tk.Radiobutton(text='Não', variable=opcao_var, value='Não', command=exibir_selecao,
                           bg='#191920', fg='#fafafa', selectcolor='#191920')

opcao_conta = ['Essenciais', 'Mercado', 'Lazer', 'Educação',
               'Saúde', 'Transporte', 'Imprevistos', 'Cartão de Crédito' ,'Outros']
var_o = tk.StringVar()
label_opcoes_conta = tk.Label(text='Tipo da sua Conta', bg='#191920', fg='#fafafa')
combo_opcoes_conta = ttk.Combobox(janela, values=opcao_conta, state='readonly', textvariable=var_o)
label_erro_opcoes = tk.Label(text='Valor inválido.', bg='#191920', fg='red', font='Courier 7')

label_data_vencimento = tk.Label(text='Vencimento da sua Conta', bg='#191920', fg='#fafafa')
# Widget de calendário (DateEntry)
vencimento_conta = DateEntry(
    janela,
    width=12,
    background='#191920',
    foreground='#fafafa',
    borderwidth=2,
    date_pattern='dd/mm/yyyy',  # Formato da data
    locale='pt_BR',
    selectbackground = '#44444c',
    state ='readonly'
)

botao_voltar = tk.Button(text='Cancelar', command=pagina_inicial, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')

botao_confirmar_criacao = tk.Button(text='Criar Conta', command=confirmar_criacao, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')


# criando o df
df_contas = pd.DataFrame()

janela.mainloop()