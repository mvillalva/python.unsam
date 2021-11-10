# hipoteca.py
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
total_pagado = 0.0
mes = 0

while saldo > 0:
    if saldo < pago_mensual:
        pago_mensual = saldo * (1+tasa/12)

    if mes+1 >= pago_extra_mes_comienzo and mes+1 <= pago_extra_mes_fin:
        mes = mes + 1
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        print(mes, round(total_pagado,2), round(saldo,2))
    else:
        mes = mes + 1
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        print(mes, round(total_pagado,2), round(saldo,2))

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes)
