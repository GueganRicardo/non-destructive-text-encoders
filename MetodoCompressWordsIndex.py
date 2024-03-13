
import numpy as np
from Huffman import HuffmanCode as HC
from HuffmanEncondingFixo4Bits import HuffmanEncoding4Bits as HE4B

class CompressWords:
    #a funçao codifica as palavras de um texto atraves do seu index num dicionarioFinal
    #o dicionario final esta organizado de tal forma que palavras com maior numero de repetiçoes sejam codificadas por index menores 
    #uncompressed-> string que quero comprimir 
    #numVezes-> numero de vezes que a palavra tem de aparecer na string para que esta seja adicionada ao dicionario
    #tamanho-> tamanho da palavra para que esta seja adicionada ao dicionario 
    #return 
    #lista de palavras->texto inicial substituindo as palavras pelos indexs no dicionario final
    def CodificaDicio(huffman_code,freq,string):#substitui cada caracter pelo codigo de huffman correspondente
        letras=[]
        stringBits=""
       # print(freq)
        for i in freq:
            letras.append(i[0])
            
        for i in string:
            index=letras.index(i)
            stringBits+=huffman_code[index]

        lista=[]

        for i in range(8,len(stringBits),8):#separa numa lista em que cada elemento tem 8 bits
            lista.append(HE4B.converteBits(stringBits[i-8:i]))
            
        binary_format = bytearray(lista)    
        return(binary_format,letras)
    
    
#!!!!! alterar aqui o caracter para codificar finance ou bible(para o finance comenantar linha 41 e descomentar 42) 
    def varianteCompress(uncompressed,numVezes,Tamanho):
        listaDePalavras=uncompressed.split(" ")
       # listaDePalavras=uncompressed.split(",") 
        listanp=np.asarray(listaDePalavras)

        dic=[]
       

        dic,ocornp=np.unique(listaDePalavras,return_counts=True)
        
        index=np.argmax(ocornp)
        string=""
        contador=0
        listanpf=listanp.copy()
        #faz um sort, cria o dicionario que tem as palavras mais frequentes nos index mais baixos 
        while(ocornp[index]!=0):#enquanto o valor mais alto for diferente de zero
            
            listanpf[listanp==dic[index]]=str(contador)
            string+=str(dic[index])+"´"
            ocornp[index]=0
            contador+=1
            index=np.argmax(ocornp)#index e o index do argumento com maior numero de repeticoes
        
        huffman_code,freq=HC.CriaCodigoHuffman(string)

        stringBin,letras=CompressWords.CodificaDicio(huffman_code,freq,string)
        
        with open("dicionarioMetodo.txt","w")as met:#escrever o dicionario no ficheiro dicionarioMetodo, separador de cada elemento da lista "´"
              for i in letras:       
                  met.write(i+"»"+huffman_code[letras.index(i)]+"»")

        with open("DicionarioInformacao.bin","wb") as DI:
            DI.write(stringBin)
            
        return listanpf