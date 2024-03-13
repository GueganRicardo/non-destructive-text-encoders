# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:06:40 2021

@author: emanuel
"""
from MetodoCompressWordsIndex import CompressWords as CW
from HuffmanEncondingFixo4Bits import HuffmanEncoding4Bits as HE4B

def main():#usar virgula no metodo do lzw para o finance melhora a compressao porque as palavras entre vigulas se repetem mais do que as que estao entre espacos, mas para bible da mais jeito usar espacos      
  
    nomeFicheiro="jquery-3.6.0"
    with open(nomeFicheiro+".txt","r") as informacao:
            texto=informacao.read()
    #listaDePalavras-> lista que contem a informacao do ficheiro codificada usando os indexs do dicionarioFinal  
    texto+=" "      
    listaDePalavras=CW.varianteCompress(texto,0,0)#codifcar todas as palavras com comprimento 1 e pelo menos 1 ocorrencia pelos seus indexs

    stringBits=HE4B.myHuffmanVersion(listaDePalavras)#cria a string de bits de toda a informacao que estava na ListaDePalavras

    lista=[]
    for i in range(8,len(stringBits),8):#separa numa lista em que cada elemento tem 8 bits
        lista.append(HE4B.converteBits(stringBits[i-8:i]))#vai converter os elementos da lista novamente em inteiros(para posteriormente codificar em bynary format)
        
    binary_format = bytearray(lista)

    with open(nomeFicheiro+"Comprimido.bin","wb") as comprimido:#escrever os dados no ficheiro binario 
           comprimido.write(binary_format)



if __name__ == "__main__":
    main()
    
    
    
