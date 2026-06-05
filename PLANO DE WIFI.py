## PLANO DE WIFI

print( 204 * "=")
print("WITECH")
print( 204 * "=")

print("ola, seja bem vindo a WITECH!")
PRECO_MB = 25
nomeUsuario = input("Qual o seu nome?: ")
mbQuantidade = int(input(f"Quantos megabytes voce pretende assinar? preco do megabyte = {(PRECO_MB) }: "))
preco_total = PRECO_MB * mbQuantidade
CONSTANTE_DO_SIM = "sim"

if mbQuantidade >= 500:
    preco_total = (PRECO_MB + 0,15) * mbQuantidade

preco_total_em_reais =  preco_total / 100

print(f" voce precira de {preco_total_em_reais} para assinar o plano")

dinheiroQuantidade = float(input("Quantos reais voce tem para assinar o plano?: "))

if dinheiroQuantidade >= preco_total_em_reais:
    PagamentoEfetuacao = input("Tudo certo, efetuar o pagamento? (responda apenas com sim ou nao):" )
    if PagamentoEfetuacao == CONSTANTE_DO_SIM:
        print("Parabens! voce assinou o plano da WITECH!")
    else:
        print("okay, tenha um otimo dia!")
else:
    if dinheiroQuantidade < preco_total_em_reais:
        print("okay, voce e um pobre tristinho adeus!")

print( 204 * "=")
print("WITECH")
print( 204 * "=")