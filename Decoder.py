# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:27:34 2021

@author: emanuel
"""
from HuffmanEncondingFixo4Bits import HuffmanEncoding4Bits as HE4B

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
    nomeFicheiro="jquery-3.6.0"
    stringInicial=""
    with open(nomeFicheiro+"Comprimido.bin","rb") as comprimido:#ler os dados do ficheiro binario 
        informacaoBinaria=comprimido.read()
    
    for i in range(len(informacaoBinaria)):
        stringInicial+=HE4B.converteInteiros(informacaoBinaria[i])#converter a informacao de numeros inteiros numa string de Binario
    
    listaDeindex=HE4B.reverteMyHuffmanVersion(stringInicial)#listaDeIndex tem a informacao do ficheiro original mas codificada com os index do dicionario 

    with open("dicionarioMetodo.txt","r")as dic:
        chaves=dic.read()
        
    with open("DicionarioInformacao.bin","rb")as RC:
        textocodificado=RC.read() 
        
       
    arraydicionario=decodeDicio(textocodificado,chaves).split("´")

    textoOriginal=""

    for i in range(len(listaDeindex)):#recuperar o texto original
        if(listaDeindex[i]!=""):
            textoOriginal+=arraydicionario[int(listaDeindex[i])]+" " 
                            
    print(textoOriginal[:-1])
    with open(nomeFicheiro+"descomprimido.txt","w") as FD:
        FD.write(textoOriginal[:-1])

if __name__ == "__main__":
    main()
    