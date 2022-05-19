dicionario = {'W':1, 'H':1/2, 'Q':1/4, 'E': 1/8, 'S':1/16, 'T':1/32, 'X':1/64}
composicao = str(input('Digite sua composição \n'))

compasso = ''
errados = []
valor = 0
corretos = 0
for i in composicao:
    if i !='/':
        valor = valor + dicionario[i]
        compasso = compasso+i
    if i =='/' and valor != 1 :
        errados.append(compasso)
        compasso=''
        valor = 0
    if i == '/' and valor == 1:
        corretos = corretos + 1
        valor = 0
        compasso = ''

errados.pop(0)
print("Qtd. de corretos: ", corretos)
if len(errados) !=0:
    print("Incorretos: ", errados)