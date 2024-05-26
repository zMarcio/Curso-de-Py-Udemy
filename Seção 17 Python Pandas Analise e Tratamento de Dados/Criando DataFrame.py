# pip install pandas
# pip install numpy
import pandas as opcoesPandas
import numpy as opcoesNumpy

#periods = quantos dias
#20221201 = Ano / Mês / Dia
dataFrame_Datas = opcoesPandas.date_range("20221201", periods=31)

print(dataFrame_Datas)
import pandas as opcoesPandas
import numpy as opcoesNumpy

#periods = quantos dias
#20221201 = Ano / Mês / Dia
dataFrame_Meses = opcoesPandas.date_range("20221231", periods=12, freq="M")

print(dataFrame_Meses)
import pandas as opcoesPandas
import numpy as opcoesNumpy

#DataFrame de números aleatórios
numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5,1))

print(numerosAleatorios)

import pandas as opcoesPandas
import numpy as opcoesNumpy

#DataFrame de números aleatórios
numeros = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15,10)*100)

print(numeros)
import pandas as opcoesPandas
import numpy as opcoesNumpy

notasAlunos_DF = opcoesPandas.DataFrame({
    
    "Nome": ["Ana", "Pedro", "João"],
    "Média": [9, 7, 10]
    
})

print(notasAlunos_DF)
