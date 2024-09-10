import os # os permite interagir com sistema operacional 
from tkinter.filedialog import askdirectory  # importa a função askdirectory da biblioteca tkinter para selecionar pastas

caminho = askdirectory(title="Selecione uma pasta") # abre a janela para o usuário selecionar a pasta
#print(caminho)

lista_arquivos = os.listdir(caminho) # lista todos os arquivos da pasta selecionada
#print(lista_arquivos)

# define as categorias(nome das pastas) e as extensões dos aruivos
locais = {
    "imagens": [".png", ".jpeg", ".jpg",".svg"],
    "planilhas": [ ".xlsx"],
    "pdfs": [".pdf"],
    "executaveis": [ ".exe"],
    "zips": [".zip"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos: # intera sobre cada arquivo na lista de arquivos
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}") # separa o nome do arquivo de sua extensão
    for pasta in locais: # intera sobre cada categoria em locais
        #print(pasta)
        if extensao in locais[pasta]: # verifica se a extensão do arquivo corresponde a categoria 
            if not os.path.exists(f"{caminho}/{pasta}"): # verifica se a pasta existe
                os.mkdir(f"{caminho}/{pasta}") # cria a pasta para categoria que não existe
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") # move os arquivos para as pasta