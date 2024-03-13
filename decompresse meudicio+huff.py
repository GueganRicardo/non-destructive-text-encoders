# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 23:05:45 2021

@author: emanuel
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:27:34 2021

@author: emanuel
"""
from HuffmanEncondingFixo4Bits import HuffmanEncoding4Bits as HE4B
#adicionar possivel decoder para o dicionario metodo
#consideracao o ficheiro tem de acabar com um espaco para apanhar o ultimo carater
def decodeDicio(textocodificado,chave):#recebe o texto a descodificar e a string que serve de dicionario
    stringcodigos=""
    for i in range(len(textocodificado)):
        stringcodigos+=HE4B.converteInteiros(textocodificado[i])

    listachave=chave.split("»")#lista com os simblos e a codificação simbolos em index impar codigo em par     

    texto=""
    aux=""
    for i in stringcodigos:
        aux+=i
        if (aux in listachave and listachave.index(aux)%2==1):
            texto+=listachave[listachave.index(aux)-1]
            aux=""  

   
    return(texto)

def main():
    nomeFicheiro="bible"

    with open(nomeFicheiro+"dicionario.txt","r")as dic:
        chavesinf=dic.read()
        
    with open(nomeFicheiro+"informacao.bin","rb")as RC:
        textocodificadoinf=RC.read() 
    
    listaDeindex=decodeDicio(textocodificadoinf,chavesinf).split(" ")

    listaDeindex=listaDeindex[:-1]

    with open("dicionarioMetodo.txt","r")as dic:
        chaves=dic.read()
        
    with open("DicionarioInformacao.bin","rb")as RC:
        textocodificado=RC.read() 
        
        
    arraydicionario=decodeDicio(textocodificado,chaves).split("´")
    
    textoOriginal=""

    
#!!!!! alterar aqui o carcter para bible espaco para finance meter a virgula (executar finance comentar linha63 e descomentar linha 64)
    for i in range(len(listaDeindex)):#recuperar o texto original
        if(listaDeindex[i]!=""):
            textoOriginal+=arraydicionario[int(listaDeindex[i])]+" " 
            #textoOriginal+=arraydicionario[int(listaDeindex[i])]+","
    

    textoOriginal=textoOriginal[:-1]                        
    print(textoOriginal)
    with open(nomeFicheiro+"descomprimido.txt","w") as FD:
        FD.write(textoOriginal)

if __name__ == "__main__":
    main()
    