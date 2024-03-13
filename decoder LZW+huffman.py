# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:31:57 2021

@author: emanuel
"""
from HuffmanEncondingFixo4Bits import HuffmanEncoding4Bits as HE4B
def main():
    dicionario=[]
    novalista=[]
    nome="jquery-3.6.0"
    with open(nome+"dicionario.txt","rb") as dR:
        dicio=dR.readline()
        texto=dR.read()
    dicio=dicio[:-3]
    dicio=(str(dicio).split("\\"))
    for i in dicio:
        dicionario.append(i[3:])
    dicionario[0]=" "
    dicionario[len(dicionario)-1]=dicionario[len(dicionario)-1][:-1]

    listaDeindex=decodeDicio(texto,dicionario).split(" ")
    

    
    for i in range(len( listaDeindex)):
        if  listaDeindex[i]!="":
            novalista.append(int(listaDeindex[i]))
    descomprimido=decompress(novalista)
    print(descomprimido)
    with open(nome+"descomprimido.txt","w") as de:
        de.write(descomprimido)
        
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

def decodeDicio(textocodificado,listachave):#recebe o texto a descodificar e a string que serve de dicionario
    stringcodigos=""
    for i in range(len(textocodificado)):
        stringcodigos+=HE4B.converteInteiros(textocodificado[i])
   
    texto=""
    aux=""
    for i in stringcodigos:
        aux+=i
        if (aux in listachave and listachave.index(aux)%2==1):
            texto+=listachave[listachave.index(aux)-1]
            aux=""  

   
    return(texto)    

if __name__ == "__main__":
    main()