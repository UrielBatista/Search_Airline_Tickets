import re

data = "UPSELLINGPreço por adultoR$6421 Adulto R$642Impostos, taxas e encargos R$144Preço final R$786ComprarPassaporte Decolarvocê acumularia 151 pontosCadastre-se e acumule pontosCom esta compra você poderia acumular pontos para combinar com qualquer forma de pagamento em uma próxima viagem.Em até 10x sem jurosVer meios de pagamento"

value_final = re.findall(r"Preço final R\$+[0-9]{,6}", data)
new_value = re.findall(r"[0-9]{1,6}", str(value_final))

print(str(new_value[0]))