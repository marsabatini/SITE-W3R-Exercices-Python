
# The program shows the current date and time

import datetime

dataHora = datetime.datetime.now()

print("The date and time in the Brazilian version are:\n")
print(dataHora.strftime("\t%H horas, %M minutos e %S segundos de %d/%m/%Y."))