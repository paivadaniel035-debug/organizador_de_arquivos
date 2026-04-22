# Organizador de Arquivo 
```import os
import shutil

origem = 'C:/Users/Informatica/Desktop/TesteDownloads'

pastas = {
    '.png': 'C:/Users/Informatica/Imagens',
    '.jpg': 'C:/Users/Informatica/Imagens',
    '.mp4': 'C:/Users/Informatica/Vídeos',
    '.mp3': 'C:/Users/Informatica/Músicas'
}

extensoes_ignoradas = ['.db', '.ini', '.te']

def mover_arquivo(origem_arquivo, destino_pasta):
    os.makedirs(destino_pasta, exist_ok=True)
    nome = os.path.basename(origem_arquivo)
    destino = os.path.join(destino_pasta, nome)

    try:
        shutil.move(origem_arquivo, destino)
        print(f'Movido: {nome} → {destino_pasta}')
    except Exception as e:
        print(f'Erro ao mover {nome}: {e}')

for nome_arquivo in os.listdir(origem):
    caminho = os.path.join(origem, nome_arquivo)

    if os.path.isdir(caminho):
        continue

    extensao = os.path.splitext(nome_arquivo)[1].lower()

    if extensao in extensoes_ignoradas:
        continue

    if extensao in pastas:
        mover_arquivo(caminho, pastas[extensao])

print("Arquivos organizados ")```
#fiz esse uns meses atras 
