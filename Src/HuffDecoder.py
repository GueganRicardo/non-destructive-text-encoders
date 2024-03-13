def main():
    nomefich="random"
    with open(nomefich+"huffmandicio.txt","r")as dic:
            chaves=dic.read()
            
    with open(nomefich+"codificadoHuffman.bin","rb")as RC:
            textocodificado=RC.read() 
    arraydicionario=decodeDicio(textocodificado,chaves)

    with open(nomefich+"descodificadoHuffman.txt","w")as DH:
        DH.write(arraydicionario)
    print(arraydicionario)
    
def decodeDicio(textocodificado,chave):#recebe o texto a descodificar e a string que serve de dicionario
    stringcodigos=""
    for i in range(len(textocodificado)):
        stringcodigos+=converteInteiros(textocodificado[i])

    listachave=chave.split("»")#lista com os simblos e a codificação simbolos em index impar codigo em par     

    texto=""
    aux=""
    
    
    for i in stringcodigos:
        aux+=i
       
        if (aux in listachave and listachave.index(aux)%2==1):
            texto+=listachave[listachave.index(aux)-1]
            aux=""  
    print(aux)
    
    return(texto)

def converteInteiros(num):#recebe um numero inteiro e transforma numa string de binarios
     binario=""
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
if __name__ == "__main__":
    main()