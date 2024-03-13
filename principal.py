# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:49:37 2021

@author: emanuel
"""

from bwt_encoder import bwt
from RLE import rle

def main():#ideia era meter bwt e depois um rle // muito bom para finance !!!! para descodificar ler 2 a 2
    with open("finance.txt","r") as bible:
        texto=bible.read()
   
    string=""
    for i in range(10000,len(texto),10000):
        bwttry=bwt.bwt(texto[i-10000:i])
        rlecombwt=rle.run_length_encoding(bwttry)
        for i in rlecombwt:
            string+=i[0]+str(i[1])+" "
        string+="/"#mudei de bloco
    with open ("bwtComRle.txt","w") as tst:
        tst.write(string)

if __name__ == "__main__":
    main()