with open("personas.txt","r",encoding="utf8") as file:
    personas=file.readlines()
for persona in personas:
    datos=persona.split(";")
    print(f"id:{datos[0]}, nombre y apellidos: {datos[1]} {datos[2]}, fecha de nacimiento: {datos[3]}")#,end="")

