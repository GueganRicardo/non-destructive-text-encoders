# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:40:24 2021

@author: emanuel
"""

import numpy as np
import huff as HF
#https://titanwolf.org/Network/Articles/Article?AID=f23d21ef-679b-4b3e-b86a-34eba1c736ce
def main():
    nome="jquery-3.6.0"
    with open(nome+".txt","r") as bible:
        texto=bible.read()
   
    result=compress(texto)

    string=""
    for i in range(len(result)):
        string+=str(result[i])+" "
    huffman_code,freq=HF.CriaCodigoHuffman(string)

   
    stringBin,letras=HF.Codifica(huffman_code,freq,string)

    with open(nome+"dicionario.txt","w") as dR:
        for i in letras:       
            dR.write(str(i)+"»"+str(huffman_code[letras.index(i)])+"»")
        dR.write("\n")
    
    with open(nome+"dicionario.txt","ab") as RC:
        RC.write(stringBin)
    
def varianteCompress(uncompressed,numVezes,Tamanho):
    #objetivo e codificar palavras com mais de n letras usando apenas o numero do index do dicionario as restantes letras ficam iguais
    listaDePalavras=uncompressed.split(" ")
    listanp=np.asarray(listaDePalavras)
       
    dic=[]
    ocor=[]#tem as ocorrencias das palavras do dic no mesmo index
    dicionarioFinal=[]
    for i in listaDePalavras:
        if(not(i in dic)):#se a palavra nao esta ja no dicionario
            if (Tamanho<len(i)):#ver se o tamanho da palavra e superior a n
                if(numVezes<len(listanp[listanp==i])):#ver se o numero de ocorrencias daquela palavra e superior a x
                    dic.append(i)
                    ocor.append(len(listanp[listanp==i]))
    ocornp=np.asarray(ocor)
    index=np.argmax(ocornp)
    #faz um sort cria o dicionario que tem as palavras mais frequentes nos index mais baixos 
    while(ocornp[index]!=0):#enquanto o valor mais alto for diferente de zero
        if(len(str(index))<len(dic[index])):#so se o tamanho da palavra for menor que o index e que a coloco no dicionario
            dicionarioFinal.append(dic[index])
        ocornp[index]=0
        index=np.argmax(ocornp)#index e o index do argumento com maior numero de repeticoes
        
    #codifica as palavras com os indexs

    dicionarioFinal=np.asarray(dicionarioFinal)
    for i in range(len(listaDePalavras)):
        if(listaDePalavras[i] in dicionarioFinal):          
                                 
                listaDePalavras[i]=(np.where(dicionarioFinal==listaDePalavras[i])[0][0])#substitui na lista de palavras a palavra pelo index no dicionario
    
    
    print(listaDePalavras)
    with open("tryNewMetodo.txt","w")as met:
        for i in dicionarioFinal:
            met.write(i+"/")
        met.write("@")#so para poder delimitar o dicionario
        for i in listaDePalavras:
            met.write(str(i)+" ")
#https://titanwolf.org/Network/Articles/Article?AID=f23d21ef-679b-4b3e-b86a-34eba1c736ce
#a seguinte função foi retirada deste link 
def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    #baseia-se na tabelas ASCII
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            if len(wc)<8:#tamanho max dos sÃ­mbolos
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c            
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
#https://titanwolf.org/Network/Articles/Article?AID=f23d21ef-679b-4b3e-b86a-34eba1c736ce
#a seguinte função foi retirada deste link
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
if __name__ == "__main__":
    main()