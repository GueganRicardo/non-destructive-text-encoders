
#https://www.pythonpool.com/run-length-encoding-python/
#a seguinte class foi retirada deste site, sugeita a algumas alteracoes
class rle:
    def run_length_encoding(seq):
      compressed = []
      count = 1
      char = seq[0]
      for i in range(1,len(seq)):
        if seq[i] == char:
          count = count + 1
        else :
          compressed.append([char,count])
          char = seq[i]
          count = 1
      compressed.append([char,count])
      return compressed
   
    def run_length_decoding(compressed_seq):
      seq =""
      for i in compressed_seq:
       for j in range(i[1]):
           seq+=i[0]
     
      return(seq)