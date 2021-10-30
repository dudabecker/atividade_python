from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

personagens = pd.read_json('/content/drive/MyDrive/character.json')
episodios = pd.read_json('/content/drive/MyDrive/episode.json')

#1. Quantos personagens existe nessa lista?
qnt_personagens = personagens['id'].count()
print("1. Existem", qnt_personagens, "personagens nessa lista.\n")

#2. Quantos personagens são humanos?
qnt_humanos = personagens['species'] == 'Human'
print(f'2. Existem {len(personagens[qnt_humanos])} personagens humanos.\n')

#3. Quantos personagens são alienígenas?
qnt_aliens = personagens['species'] == 'Alien'
print(f'3. Existem {len(personagens[qnt_aliens])} personagens alienigenas.\n')

#4. Há quantos tipos de alienígenas diferentes?
alien_condicao = personagens['species'] == 'Alien'
alien_qnt = personagens.loc[alien_condicao]
x = alien_qnt['type'].value_counts()
numero_tipos_alienigena = x.shape
print(f'4. Existem {numero_tipos_alienigena[0]} tipos de alienígenas diferentes.\n')
