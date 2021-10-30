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

#5. Quantos alienígenas são homens e quantos são mulheres?
alien_condicao = personagens['species'] == 'Alien'
alien_df = personagens.loc[alien_condicao]
numero_aliens, coluna = alien_df.shape

alien_homem_condicao = alien_df['gender'] == 'Male'
alien_homem_df = alien_df.loc[alien_homem_condicao]
numero_homem_aliens, coluna = alien_homem_df.shape

alien_mulher_condicao = alien_df['gender'] == 'Female'
alien_mulher_df = alien_df.loc[alien_mulher_condicao]
numero_mulher_aliens, coluna = alien_mulher_df.shape

print(f'5. Existem {numero_homem_aliens} homens e {numero_mulher_aliens} mulheres alienígenas.\n')

#6. Qual o nome do episódio em que o personagem Crocubot aparece?
crocubot_condicao = personagens['name'] == 'Crocubot'
crocubot = personagens.loc[crocubot_condicao]
episodio = crocubot['episode']
episodio = episodio[80][0]
episodio = episodio.split('/')
episodio = int(episodio[-1])

print(f'6. O personagem Crocubot aparece no episódio {episodio}.\n')
