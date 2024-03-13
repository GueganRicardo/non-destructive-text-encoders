
from typing import List, Tuple, Union
common_dictionary=[";","0","1","2","3","4","5","6","7","8","9"]


def main ():
    with open("random.txt","r")as jq:
        texto=jq.read()

    stringBWT=""
    for i in range(5000,len(texto),5000):
        stringBWT+=bwt(texto[i-5000:i])
    
    stringBWT+=bwt(texto[i:])
    stringDeLZW=compress(stringBWT)
   
    huffman_code,freq=CriaCodigoHuffman(stringDeLZW)
    huffman_code[0]="00"
    stringBin,letras=Codifica(huffman_code,freq,stringDeLZW)
  

    with open("LZW+MOVE+HUFF.txt","w") as RC:
        for i in letras:       
            RC.write(i+" "+huffman_code[letras.index(i)]+" ")
        RC.write("\n")
    
    with open("LZW+MOVE+HUFF.txt","ab+") as RC:
        RC.write(stringBin)
#https://titanwolf.org/Network/Articles/Article?AID=f23d21ef-679b-4b3e-b86a-34eba1c736ce
#a seguinte função foi retirada deste link
def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    #baseia-se na tabelas ASCII
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    
    w = ""
    result = ""#separador do result vai ser;
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            if len(wc)<8:#tamanho max dos sÃ­mbolos
                w = wc
            else:
                result+=str(dictionary[w])+";"
                dictionary[wc] = dict_size
                dict_size += 1
                w = c            
        else:
            result+=str(dictionary[w])+";"
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    # Output the code for w.
    if w:
        result+=str(dictionary[w])+";"
    return result[:-1]
#https://en.wikipedia.org/wiki/Move-to-front_transform
#a seguinte funçao foi retirada deste site, sugeita a algumas alteracoes
def encode(plain_text):
        # Change to bytes for 256.
       # plain_text = plain_text.encode('utf-8')
        # Changing the common dictionary is a bad idea. Make a copy.
        dictionary = common_dictionary.copy()
        # Transformation
        compressed_text = ""          # Regular array
        rank = 0
        # Read in each character
        for c in plain_text:
            rank = dictionary.index(c)    # Find the rank of the character in the dictionary [O(k)]
            compressed_text+=str(rank)+"," # Update the encoded text
    
            # Update the dictionary [O(k)]
            dictionary.pop(rank)
            dictionary.insert(0, c)
    
        return compressed_text[:-1]   
    
#inspirado no codigo retirado do huffman    

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
    for i in range(len(lista)):
        lista[i]=converteBits(lista[i])
    binary_format = bytearray(lista)    
    return(binary_format,letras)
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
        return final_code


def converteBits(String):
    num=0
    for i in String:
        if(i=="1"):
            num=num*2+1
        else:
            num=num*2        
    return num


def converteInteiros(string):#Converte bytearray para string
    binario=""
    for i in range(len(string)):
        num=string[i] 
        binario +=str(int(num/128))
        num=num%128
        binario +=str(int(num/64))
        num=num%64
        binario +=str(int(num/32))
        num=num%32
        binario +=str(int(num/16))
        num=num%16
        binario +=str(int(num/8))
        num=num%8
        binario +=str(int(num/4))
        num=num%4
        binario +=str(int(num/2))
        num=num%2
        binario +=str(int(num/1))
    return(binario)
#https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
#funçao foi retirada deste site
def bwt(s: str) -> str:
        """Apply Burrows–Wheeler transform to input string."""
        assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
        s = "\002" + s + "\003"  # Add start and end of text marker
        table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
        last_column = [row[-1:] for row in table]  # Last characters of each row
        return "".join(last_column)  # Convert list of characters into string
if __name__ == "__main__":
    main()