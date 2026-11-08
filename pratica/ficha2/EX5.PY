dict = { 
  'Physics': 82, 
  'Math': 65, 
  'history': 35
} 
# menor = 0

# for key in dict.keys():
#     if menor == 0:
#         menor = dict.get(key)
#     elif dict.get(key) < menor:
#         menor = dict.get(key)

# print("O valor mais baixo e :", menor)

chave_min= min(dict, key=dict.get)
print("A chave do valor mais baixo e :", chave_min)