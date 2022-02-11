import datetime
import calendar
dia = 12
mes = 2
ano = 2022
hora = 10
minu = 20


data_rec = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

print(data_rec)
print(hoje)

# dia atual
dia_atual = calendar.day_name[data_rec.weekday()]
print(dia_atual)

if dia_atual == 'Saturday' or dia_atual == 'Sunday':
    print("hoje éh sabado")
else:
    print("hoje é dia de semana")


for i in range(8, 12):
    print(i)
