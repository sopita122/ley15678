
# ============================================================
# Materia: Laboratorio de Programación - 5° 3°
# EEST N.º 1 "Eduardo Ader" - Vicente López
#
# ACTIVIDAD 10: Simulador de Normativa de Celulares en el Aula
# Ley 15.678
#
# DOCENTE: Mansilla Muñoz York Elías
# ESTUDIANTE: Sofia Salaberry
# REPOSITORIO: ley15678
# ============================================================

print("==================================================")
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("==================================================\n")

# Variables que representan las condiciones del aula
autorizacion_docente = True
emergencia_familiar = True

# Mostrar el estado de las variables
print(f"Estado de Autorización Docente: {autorizacion_docente}")
print(f"Estado de Emergencia Validada: {emergencia_familiar}\n")

# Estructura condicional para evaluar cada situación
if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo puede utilizarse para estudiar y aprender (fines pedagógicos).")

elif emergencia_familiar == True:
    print("[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente a través de preceptoría y/o dirección.")

else:
    print("[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("==================================================")
