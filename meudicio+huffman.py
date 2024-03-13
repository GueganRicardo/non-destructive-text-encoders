
from MetodoCompressWordsIndex import CompressWords as CW
import huff as HF
def main():
    nomefich="bible"
    
    with open(nomefich+".txt","r") as file:
        texto=file.read()
    info=""
    listaDePalavras=CW.varianteCompress(texto,0,0)

    for i in listaDePalavras:
        info+=i+" "

    huffman_code,freq=HF.CriaCodigoHuffman(info)

   
    stringBin,letras=HF.Codifica(huffman_code,freq,info)

   
    with open(nomefich+"dicionario.txt","w") as dR:
        for i in letras:       
            dR.write(i+"»"+huffman_code[letras.index(i)]+"»")
    
    with open(nomefich+"informacao.bin","wb") as RC:
        RC.write(stringBin)
    
    
if __name__ == "__main__":
    main()
    