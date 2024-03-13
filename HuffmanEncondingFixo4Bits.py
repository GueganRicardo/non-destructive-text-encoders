# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:57:11 2021

@author: emanuel
"""

class HuffmanEncoding4Bits:
    #recebe uma lista com numeros e codifica o conteudo de lista numa string de bits usando os seguites codigos fixos para codificar cada elemento
    #return string de bits 
    def myHuffmanVersion(lista):
        stringDeBits=""
        for i in lista:
            for j in str(i):
                if(j=="0"):
                    stringDeBits+="0000"
                elif(j=="1"):
                    stringDeBits+="0001"
                elif(j=="2"):
                    stringDeBits+="0010"
                elif(j=="3"):
                    stringDeBits+="0011"
                elif(j=="4"):
                    stringDeBits+="0100"
                elif(j=="5"):
                    stringDeBits+="0101"
                elif(j=="6"):
                    stringDeBits+="0110"
                elif(j=="7"):
                    stringDeBits+="0111"
                elif(j=="8"):
                    stringDeBits+="1000"
                elif(j=="9"):
                    stringDeBits+="1001"   
            stringDeBits+="11"#corresponde ao espaco para distinguir 2 elementos da lista
        return stringDeBits
    
    
    #faz o processo inverso de myHuffmanVersion, pega numa string de bits e converte a numa lista de numeros(string) usando codigos fixos 
    def reverteMyHuffmanVersion(stringInicial):
        subcadeia=""
        listaDeindex=[]
        numero=""
        for i in range(len(stringInicial)):
            subcadeia+=stringInicial[i]
        #print(aux)
            if(len(subcadeia)==2 and subcadeia=="11"):#sinal que o proximo numero sera de um index diferente
                listaDeindex.append(numero)
                numero=""   
                subcadeia=""
                
            if(len(subcadeia)==4):
                if(subcadeia=="0000"):
                    numero+="0"
                elif(subcadeia=="0001"):
                    numero+="1"
                elif(subcadeia=="0010"):
                    numero+="2"
                elif(subcadeia=="0011"):
                    numero+="3"
                elif(subcadeia=="0100"):
                    numero+="4"
                elif(subcadeia=="0101"):
                    numero+="5"
                elif(subcadeia=="0110"):
                    numero+="6"
                elif(subcadeia=="0111"):
                    numero+="7"
                elif(subcadeia=="1000"):
                    numero+="8"
                elif(subcadeia=="1001"):
                    numero+="9"
                subcadeia=""
        
        #listaDeindex.append(numero)
        return listaDeindex
    
    
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
 
 
    def converteBits(String):#recebe uma string de bits e converte num numero inteiro
        
        for i in range(0,len(String),8):
            num=0
            if(String[i]=="1"):
                num=num+128
            if(String[i+1]=="1"):
                num=num+64
            if(String[i+2]=="1"):
                num=num+32
            if(String[i+3]=="1"):
                num=num+16
            if(String[i+4]=="1"):
                num=num+8
            if(String[i+5]=="1"):
                num=num+4
            if(String[i+6]=="1"):
                num=num+2
            if(String[i+7]=="1"):
                num=num+1  
            
        return(num)