import os.path
import shutil
from time import sleep
def mostrar_caminho():
    print(f'Arquivo: {nome_arquivo} | Extensão: {extensão} | Iria para: {destino}')

origem = 'C:/Users/Informatica/Desktop/TesteDownloads'
destino = ''
extensões_ignoradas = ['.db', '.ini', '.te']
def mover_arquivo(origem,destino):
    shutil.move(origem,destino)
# Ver todos os arquivos da pasta a ser modificada, nesse caso a de Downloads
print(os.listdir(origem))
# Aqui vai analisar quais são as extensões de cada arquivo
for nome_arquivo in os.listdir(origem):
    caminho_completo = os.path.join(origem, nome_arquivo)
    if os.path.isdir(caminho_completo):
        continue
    extensão = os.path.splitext(nome_arquivo)[1].lower()
    #print(extensão)
    if extensão == '.png':
        destino = 'C:/Users/Informatica/Imagens'
        mostrar_caminho()
        novo_caminho = os.path.join(destino, nome_arquivo)
        mover_arquivo(caminho_completo,novo_caminho)
    elif extensão == '.mp4':
        destino = 'C:/Users/Informatica/Vídeos'
        mostrar_caminho()
        novo_caminho = os.path.join(destino, nome_arquivo)
        mover_arquivo(caminho_completo,novo_caminho)
    elif extensão == '.mp3':
        destino = 'C:/Users/Informatica/Músicas'
        mostrar_caminho()
        novo_caminho = os.path.join(destino, nome_arquivo)
        mover_arquivo(caminho_completo,novo_caminho)
    elif extensão in extensões_ignoradas:
        continue
    print()
sleep(1.5)
print('OS SEUS ARQUIVOS FORAM MOVIDOS COM SUCESSO!')
