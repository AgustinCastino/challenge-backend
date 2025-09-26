from model import reportModel
import pandas as pd

def createReport():
    empleados = list(reportModel.obtener_empleados())

    df = pd.DataFrame(empleados)

    total_empleados = len(df)
    suma_sueldos = df['salario'].sum()
    promedio_sueldos = df['salario'].mean()
    empleados_por_puesto = df['puesto'].value_counts()
    suma_sueldos_por_puesto = df.groupby('puesto')['salario'].sum()
    promedio_sueldos_por_puesto = df.groupby('puesto')['salario'].mean()

    resumen = {
        "Total de Empleados": [total_empleados],
        "Suma de todos los Sueldos": [suma_sueldos],
        "Promedio de todos los Sueldos": [promedio_sueldos]
    }
    resumen_df = pd.DataFrame(resumen)
    
    with pd.ExcelWriter("reporte_empleados.xlsx", engine="xlsxwriter") as writer:
        # Creo cada una de las hojas de Excel
        resumen_df.to_excel(writer, sheet_name="Resumen", index=False)
        empleados_por_puesto.to_frame("Cantidad de empleadoss").to_excel(writer, sheet_name="Empleados por Posición")
        suma_sueldos_por_puesto.to_frame("Sumatoria de sueldos de la posición").to_excel(writer, sheet_name="Sueldos por Posición")
        promedio_sueldos_por_puesto.to_frame("Promedio de los sueldos de la posición").to_excel(writer, sheet_name="Promedio por Posición")
    
    return "Reporte generado: reporte_empleados.xlsx"