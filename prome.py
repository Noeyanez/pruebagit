notas={"matematicas":[6.5,5.8,6.2],"lenguaje":[5.5,6.0,5.8],}
for asignatura, calificaciones in notas.items():
    prom=sum(calificaciones) / len(calificaciones)
    print(f"promedio de {asignatura}: {prom:.2f}")