import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import wavfile
    #from huffmancodec import HuffmanCodec
    
    #devolve array com o numero de repeticoes de cada elemento do alfabeto
    
def histograma(P,A):#P-->array com info sobre os bits da imagem/A-> array com o alfabeto
        lista_contagens = np.zeros(257)
       
        for i in P:
                lista_contagens[i]+=1#percorre uma vez o array P e incrementa no array contagens no index correspondente o valor de vezes que o simbolo aparece  
        return lista_contagens
    
    
    
    #calcula a entropia para um dada fonte de info P com o alfabeto A,devolve int com o resultado
def limite_minimo(P,A):
        
        contagens = histograma(P,A)

       
        probabilidades = np.zeros(len(contagens))
        probabilidades = contagens / sum(contagens)
        probabilidades = probabilidades[probabilidades>0]
       
        resultado = -sum(probabilidades*np.log2(probabilidades))
    
        return resultado
    
    
    #cria o grafico de barras com as frequencias de cada simbolo e imprime a entropia correspondente a cada imagem
    
    
def docTexto(name): 
       # alfabeto=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        info=[]
        alfaAscii=[]
       
        
        with open(name,"r") as eng:#ler a informacao do ficheiro e vai guardar no array txt_english com Ascii 
             docenglish=eng.read()
        for i in docenglish:
            info.append(ord(i))
        info=np.asarray(info)
       
        #info é array que so tem letras em ascii
        alfaAscii=np.unique(info)
 
        alfaAscii=np.asarray( alfaAscii)
    
        #contagens = histograma(info,alfaAscii)
        lim_info = limite_minimo(info,alfaAscii)
        print(f"Limite minimo para %s: {lim_info}"%name)
        print("base line de ficheiro %f"%((len(info)*lim_info)/8))

        
        
def main():
        docTexto("bible.txt")
        
        docTexto("random.txt")
        docTexto("jquery-3.6.0.txt")
        docTexto("finance.txt")
if __name__ == "__main__":
        main()