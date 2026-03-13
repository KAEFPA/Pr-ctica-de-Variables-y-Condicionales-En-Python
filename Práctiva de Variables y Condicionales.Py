
PORCENTAJE_TSS = 0.0591  
PORCENTAJE_ISR = 0.15    
PORCENTAJE_BONO = 0.10   

def calcular_nomina():
    print("--- Sistema de Cálculo de Sueldo Neto (RD) ---")
    
    try:
        sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))
        otros_descuentos = float(input("Ingrese otros descuentos (si no hay, ponga 0): "))
        
        if sueldo_bruto <= 0:
            print("Error: El sueldo debe ser un valor positivo.")
            return
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        return

   
    descuento_tss = sueldo_bruto * PORCENTAJE_TSS
    
   
    sueldo_sujeto_isr = sueldo_bruto - descuento_tss
    descuento_isr = sueldo_sujeto_isr * PORCENTAJE_ISR
    
    bonificacion = sueldo_bruto * PORCENTAJE_BONO
    
    
    total_descuentos = descuento_tss + descuento_isr + otros_descuentos
    sueldo_neto = (sueldo_bruto + bonificacion) - total_descuentos

    
    print("\n" + "="*30)
    print(f"RESUMEN DE NÓMINA")
    print("="*30)
    print(f"Sueldo Bruto:          ${sueldo_bruto:,.2f}")
    print(f"Bonificación (+):      ${bonificacion:,.2f}")
    print(f"Descuento TSS (-):     ${descuento_tss:,.2f}")
    print(f"Retención ISR (-):     ${descuento_isr:,.2f}")
    print(f"Otros Descuentos (-):  ${otros_descuentos:,.2f}")
    print("-" * 30)
    print(f"SUELDO NETO RECIBIDO:  ${sueldo_neto:,.2f}")
    print("="*30)

if __name__ == "__main__":
    calcular_nomina()