import tkinter as tk
import math
cores = {
  'fundo': "#0E0E0E",         # Fundo da janela e botões
    'fundo_visor': "#000000",    # Fundo do visor
    'texto_principal': "#FFFFFF", # Texto branco para os números
    'texto_operador': '#FF9500', # Laranja para operadores
    'botao_clicado': "#000000"
}

# Cria a janela principal
resultado_exibido = False

def limpar_visor():
    """Limpa o visor e reinicia o estado de resultado exibido."""
    global resultado_exibido
    visor.delete(0, tk.END)
    resultado_exibido = False

def clicar_botao(valor):
    """Lida com o clique de botões de número ou operador."""
    global resultado_exibido
    
    # Se um resultado está na tela e o usuário digita um NÚMERO,
    # um novo cálculo vai começar. Limpamos o visor primeiro.
    if resultado_exibido and valor in '0123456789':
        limpar_visor()
    
    # Qualquer clique de botão encerra o "estado de resultado exibido"
    resultado_exibido = False

    # Insere o valor clicado no final do texto atual
    visor.insert(tk.END, valor)

def calcular():
    """Calcula a expressão no visor."""
    global resultado_exibido
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        
        # Correção: Chamar a função com parênteses
        limpar_visor() 
        
        # Correção: Converter o resultado para string
        visor.insert(0, str(resultado))
        
        resultado_exibido = True
    except Exception as e: 
        limpar_visor()
        visor.insert(0, "Erro")
        print(f"Erro: {e}")
def calcular_raiz_quadrada():
    """Calcula a raiz quadrada do número no visor"""
    global resultado_exibido
    try:
        numero = float(visor.get())
        resultado = math.sqrt(numero)
        limpar_visor()
        visor.insert(0, str(resultado))
        resultado_exibido = True
    except ValueError:
        limpar_visor
        visor.insert(0, "Erro")
    except Exception as e:
        limpar_visor()
        visor.insert(0, "Erro")
        print( f"Erro: {e}")


# --------------------------------------------------------------------
# 2. Construção da Interface Gráfica (GUI)
# --------------------------------------------------------------------

# Configuração da Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg=cores['fundo'])
#janela.geometry("320x480") # Ajustei um pouco para os botões caberem melhor
janela.resizable(True, True)
for i in range(4):
    janela.grid_rowconfigure(i, weight=1)
for i in range(5):
    janela.grid_columnconfigure(i, weight=1)
# Visor
visor = tk.Entry(janela, font=("Ubuntu Sans", 24), borderwidth=2, relief="flat", justify="right", bg=cores['fundo_visor'], fg=cores['texto_principal'])
visor.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=10)

# Lista de botões
botoes = [
    '(', ')', 'xⁿ', '√',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '=',
    'C'
]

linha_atual = 1
coluna_atual = 0

for texto_botao in botoes:
    cor_do_texto = cores['texto_operador'] if texto_botao in '+-/*√xⁿ()' else cores['texto_principal']
    # Lógica para atribuir o comando correto para 'C' e '='
    if texto_botao == 'C':
        comando = limpar_visor
    elif texto_botao == '=':
        comando = calcular
    elif texto_botao == '√':
        comando = calcular_raiz_quadrada
    elif texto_botao == 'xⁿ':
        comando = lambda valor = '**':clicar_botao(valor)
    else:
        comando = lambda valor=texto_botao: clicar_botao(valor)
    
    # Criação do botão
    botao = tk.Button(janela, text=texto_botao, font=("Ubuntu Sans", 18, "bold"), padx=20, pady=20, command=comando,
                      bg=cores['fundo'], fg=cores['texto_principal'], activebackground=cores['botao_clicado'],activeforeground=cor_do_texto, relief="groove", borderwidth=0)
    botao.grid(row=linha_atual, column=coluna_atual, padx=5, pady=5)
    
    # Atualiza a posição para o próximo botão
    coluna_atual += 1
    if coluna_atual > 3:
        coluna_atual = 0
        linha_atual += 1

# --------------------------------------------------------------------
# 3. Iniciar a Aplicação
# --------------------------------------------------------------------
janela.mainloop()