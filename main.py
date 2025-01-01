import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkcalendar import DateEntry
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
    label_titulo.grid(row=0, column=1)
    entry_nome_conta.grid(row=2, column=0, pady=(0, 1), padx=(15, 0))
    label_valor_conta.grid(row=1, column=1, pady=(15, 1), padx=(1, 0))
    entry_valor_conta.grid(row=2, column=1, pady=(0, 1), padx=(15, 0))
    label_nome_conta.grid(row=1, column=0, pady=(0, 1), padx=(1, 0))
    label_parcelas_conta.grid(row=1, column=2, pady=(15, 1), padx=(1, 0))
    entry_parcelas_conta.grid(row=2, column=2, pady=(0, 1), padx=(15, 0))
    label_prioridade_conta.grid(row=4, column=0, pady=(15, 1), padx=(1, 0))
    entry_prioridade_conta.grid(row=5, column=0, pady=(0, 1), padx=(15, 0))
    label_parcatual_conta.grid(row=4, column=1, pady=(15, 1), padx=(1, 0))
    entry_parcatual_conta.grid(row=5, column=1, pady=(0, 1), padx=(15, 0))
    label_conta_paga.grid(row=4, column=2, pady=(15, 1), padx=(1, 0))
    radio_sim.grid(row=5, column=2)
    radio_nao.grid(row=6, column=2)
    label_opcoes_conta.grid(row=8, column=0, pady=(0, 1), padx=(15, 0))
    combo_opcoes_conta.grid(row=9, column=0, pady=(0, 1), padx=(15, 0))
    label_data_vencimento.grid(row=8, column=1, pady=(0, 1), padx=(15, 0))
    calendario.grid(row=9, column=1, pady=(0, 1), padx=(15, 0))
    botao_voltar.grid(row=10, column=5, pady=(0, 15), padx=(5, 15))
    botao_confirmar.grid(row=10, column=4, pady=(0, 15), padx=(0, 5))


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
    entry_prioridade_conta.grid_forget()
    label_parcatual_conta.grid_forget()
    entry_parcatual_conta.grid_forget()
    label_conta_paga.grid_forget()
    radio_sim.grid_forget()
    radio_nao.grid_forget()
    botao_voltar.grid_forget()
    botao_confirmar.grid_forget()
    calendario.grid_forget()
    label_data_vencimento.grid_forget()
    combo_opcoes_conta.grid_forget()
    label_opcoes_conta.grid_forget()

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
    return all(caracter.isdigit() or caracter in '., ' for caracter in texto)


def validar_numeros(texto):
    return all(caracter.isdigit() for caracter in texto)


def exibir_selecao():
    selecionado = opcao_var.get()
    return selecionado

def confirmar():
    pass


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

label_valor_conta = tk.Label(text='Valor da Conta', bg='#191920', fg='#fafafa')
cmd_validar_valor = (janela.register(validar_valor_conta), "%P")
entry_valor_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                             validatecommand=cmd_validar_valor)

label_parcelas_conta = tk.Label(text='Número de Parcelas', bg='#191920', fg='#fafafa')
cmd_validar_numero = (janela.register(validar_numeros), "%P")
entry_parcelas_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                                validatecommand=cmd_validar_numero)

prioridade_conta = ['Alta', 'Média', 'Baixa']
label_prioridade_conta = tk.Label(text='Prioridade da Conta', bg='#191920', fg='#fafafa')
entry_prioridade_conta = ttk.Combobox(janela, values=prioridade_conta, state='readonly')

label_parcatual_conta = tk.Label(text='Parcela atual da Conta', bg='#191920', fg='#fafafa')
entry_parcatual_conta = tk.Entry(bg='#44444c', fg='#fafafa', insertbackground='#fafafa', validate="key",
                                 validatecommand=cmd_validar_numero)


label_conta_paga = tk.Label(text='A Conta paga', bg='#191920', fg='#fafafa')

opcao_var = tk.StringVar(value='Não')
radio_sim = tk.Radiobutton(text='Sim', variable=opcao_var, value='Sim', command=exibir_selecao,
                           bg='#191920', fg='#fafafa', selectcolor='#191920')
radio_nao = tk.Radiobutton(text='Não', variable=opcao_var, value='Não', command=exibir_selecao,
                           bg='#191920', fg='#fafafa', selectcolor='#191920')

opcao_conta = ['Essenciais', 'Mercado', 'Lazer', 'Educação',
               'Saúde', 'Transporte', 'Imprevistos', 'Cartão de Crédito' ,'Outros']
label_opcoes_conta = tk.Label(text='Tipo da sua Conta', bg='#191920', fg='#fafafa')
combo_opcoes_conta = ttk.Combobox(janela, values=opcao_conta, state='readonly')

label_data_vencimento = tk.Label(text='Vencimento da sua Conta', bg='#191920', fg='#fafafa')
# Widget de calendário (DateEntry)
calendario = DateEntry(
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

botao_voltar = tk.Button(text='Voltar', command=pagina_inicial, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')

botao_confirmar = tk.Button(text='Confirmar', command=confirmar, bg='#393642', fg='#fafafa',
                          relief='flat', bd=6, activebackground='#393642', cursor='hand2')


janela.mainloop()