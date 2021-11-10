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
    mes += 1
    pago_mensual_total = pago_mensual
    
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
        pago_mensual_total += pago_extra
        
    saldo = saldo * (1+tasa/12)    
    
    if saldo < pago_mensual_total:                
        pago_mensual_total = saldo        
        
    saldo -= pago_mensual_total
    total_pagado = total_pagado + pago_mensual_total
        
    print(f"{mes} {total_pagado:.2f} {saldo:.2f}")

print(f'Total pagado: {total_pagado:.2f}')
print(f'Meses: {mes}')
