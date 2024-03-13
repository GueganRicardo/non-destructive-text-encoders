import math
import sys
global probabilities

probabilities = []
#https://www.codegrepper.com/code-examples/python/huffman+coding+python
#retirado deste link, foram feitas algumas alteracoes
class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1

    def compute_code(self):
        num = len(self.probability)
        huffman_code = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman_code[num-i-1] != '' and huffman_code[num-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[num-i-1] != ''):
                huffman_code[num-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[num-i-2] != ''):
                huffman_code[num-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num-i-1] = '1'
                huffman_code[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[num-i-2], list) and isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + huffman_code[num-i-2]
            elif(isinstance(huffman_code[num-i-2], list)):
                complete_code = huffman_code[num-i-2] + [huffman_code[num-i-1]]
            elif(isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + [huffman_code[num-i-2]]
            else:
                complete_code = [huffman_code[num-i-2], huffman_code[num-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        if(huffman_code[0]==[]):
            final_code[0]="0"#funcionava tendo 2 00 ver se funciona so com 1 zero # ver quando so uso huffman, ver quando uso outro algoritmo e depois huffman 

        return final_code


def converteBits(String):
    num=0
    for i in String:
        if(i=="1"):
            num=num*2+1
        else:
            num=num*2        
    return num

def CriaCodigoHuffman(string):
    #calcula a frequência de cada símbolo no alfabeto
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1  
    
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)#ordena a freq por ordem decrescente   
 
    probabilities = [float("{:.2f}".format(frequency[1]/len(string))) for frequency in freq]#Calcula a prorbabilidade de cada símbolo do alfabeto
    probabilities = sorted(probabilities, reverse=True)

    huffmanClassObject = HuffmanCode(probabilities)
   
    huffman_code = huffmanClassObject.compute_code()#Faz uma lista com a codificação de cada símbolo

    return(huffman_code,freq)
    
def Codifica(huffman_code,freq,string):#substitui cada caracter pelo codigo de huffman correspondente
    listadeBits=[]
    letras=[]
    for i in freq:
        letras.append(i[0])
    for i in string:
        index=letras.index(i)
        listadeBits.append(huffman_code[index])
    stringBits=""
    lista=[]
    for i in listadeBits:
        stringBits+=i
    for i in range(8,len(stringBits),8):#separa numa lista em que cada elemento tem 8 bits
        lista.append(stringBits[i-8:i])
    lista.append(stringBits[i:]+('0'*(8-len(stringBits[i:]))))
    
    for i in range(len(lista)):
        lista[i]=converteBits(lista[i])
    binary_format = bytearray(lista)    
    return(binary_format,letras)



def main():
    nomefich="random"
    with open(nomefich+".txt","r")as r:
        string=r.read()

    huffman_code,freq=CriaCodigoHuffman(string)

   
    stringBin,letras=Codifica(huffman_code,freq,string)
    
   
    with open(nomefich+"huffmandicio.txt","w") as dR:
        for i in letras:       
            dR.write(i+"»"+huffman_code[letras.index(i)]+"»")
    
    with open(nomefich+"codificadoHuffman.bin","wb") as RC:
        RC.write(stringBin)
    
          
if __name__ == "__main__":
    main()