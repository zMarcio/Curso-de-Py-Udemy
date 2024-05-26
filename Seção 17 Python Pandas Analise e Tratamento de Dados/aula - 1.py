# pip install pandas # Instalação da biblioteca
import numpy as np
import pandas as pd
# # Criando um DataFrame no pandas com dados estáticos
notasAlunos_DataFrame = pd.DataFrame({
    "Nome":["Evanilson","Pedro","João"],
    "Nota 1":[9,7,10],
    "Nota 2":[6,9,8],
    "Nota 3":[7,5,10],
    "Nota 4":[10,10,6],
})

print(notasAlunos_DataFrame)

# # Criando uma nova coluna chamada média e fazendo a soma de todas as notas e dividindo
notasAlunos_DataFrame["Media"] = ((notasAlunos_DataFrame["Nota 1"]
                                   + notasAlunos_DataFrame["Nota 2"] 
                                   + notasAlunos_DataFrame["Nota 3"]
                                   + notasAlunos_DataFrame["Nota 4"])/4)

print(notasAlunos_DataFrame)



notasAlunos_DataFrame["Faltas"] = 5

print(notasAlunos_DataFrame)

# # Criando números aleatórios para colocar dentro de faltas
x, y, w = np.random.randint(1, 11), np.random.randint(1, 11), np.random.randint(1, 11)

fault = []

fault.append(x)

fault.append(y)

fault.append(w)

notasAlunos_DataFrame["Faltas"] = fault

print(notasAlunos_DataFrame)

# # Alterando um dado específico de uma coluna
notasAlunos_DataFrame.loc[1,"Nota 2"] = 10

notasAlunos_DataFrame["Media"] = ((notasAlunos_DataFrame["Nota 1"]+notasAlunos_DataFrame["Nota 2"]+notasAlunos_DataFrame["Nota 3"]+notasAlunos_DataFrame["Nota 4"])/4)
print(notasAlunos_DataFrame)