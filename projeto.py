from google.colab import drive
drive.mount('/content/drive')

!pip install pandas

def conversaoMB(tamanhoBytes):
  tamanhoBytes = float(tamanhoBytes)
  return (float(tamanhoBytes/(1024*1024)))
   
def percentualUsuario(lista, total):
  percentual = (lista[3]/total)*100
  lista.insert((len(usuario)),percentual)

def espacoMedio(lista, total):
  media = 0
  elementos = len(lista)
  media = (total)/(elementos+1)
  return media

usuarios = []
posicao = 1
total = media = 0
with open ("/content/drive/MyDrive/usuarios.txt","r") as arquivo:
  valor = 0
  for linha in arquivo:
    usuarios.append(linha.split()) 

  for usuario in usuarios:
    usuario.insert(0,posicao)
    valor = conversaoMB(float(usuario[2]))
    total += valor
    usuario.insert((len(usuario)),valor)
    posicao+=1

  for usuario in usuarios:
    percentualUsuario(usuario, total)

media = espacoMedio(usuario,total)

with open ("relatorio.txt","w") as arquivo:
  arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
  arquivo.write("--------------------------------------------------------------\n")
  arquivo.write("Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n\n")

  for usuario in usuarios:
    percentagem="{0:.2f}".format(round(usuario[3],2))
    arquivo.write(str(usuario[0])+'\t'+"{:<15}".format(usuario[1])+'\t'+"{:<16}".format(percentagem)+'MB'+'\t'+"{0:.2f}".format(usuario[4])+'%'+'\n')

  arquivo.write('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
  arquivo.write('\n\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
  arquivo.close()

with open ("relatorio.txt","r") as arquivo:
  print(arquivo.read())
