alunos = [ 
    { 
        "numero": 101, 
        "nome": "Ana", 
        "notas": [("Matemática", 16), ("Programação", 18), ("Inglês", 14)] 
    }, 
    { 
        "numero": 102, 
        "nome": "Bruno", 
        "notas": [("Matemática", 9), ("Programação", 15), ("Inglês", 13)] 
    }, 
    { 
        "numero": 103, 
        "nome": "Carla", 
        "notas": [("Matemática", 17), ("Programação", 16), ("Inglês", 18)] 
    } ,
    
]
mediaDict = {}
listNameMed = []
for aluno in alunos:
    soma = 0
    for nota in aluno["notas"]:
        soma =soma + nota[1]
        media = soma / len(aluno["notas"])
        

    mediaDict[aluno["numero"]] = f"{media:.2f}"
    listNameMed.append((aluno["nome"], f"{media:.2f}"))
ListNameMedSorted = sorted(listNameMed, key=lambda )
print(mediaDict)
print(ListNameMedSorted)
mediaDisciplina = {}
contador = 0

# alunoNeg =()
# for aluno in alunos:
#     if aluno["notas"]< 10:
#         alunoNeg() 









    
        
    
    




