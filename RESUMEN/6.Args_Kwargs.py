#ARGS
def mostrar_estudios(nombre, *asignaturas):
    print(f"{nombre} ha estudiado las siguientes asignaturas:")
    for asignatura in asignaturas:
        print(f"- {asignatura}")

# Llamamos a la función con diferentes cantidades de asignaturas
mostrar_estudios("Alice", "Matemáticas", "Física", "Química")
print("\n")
mostrar_estudios("Bob", "Historia", "Literatura")

def lista(nombre,*comida):
    print(f"esta es la lista de {nombre}: ")
    for comidas in comida:
        print(f"-{comidas}")

lista("giancarlo","arroz","pollo")

 
