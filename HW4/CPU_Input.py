#create the inputs and outputs
#for an unsigned integer divider

def bit_extend(bin_num, num_bits):
  """
  extends the binary number with 0's
  until it is num_bits long
  the 0b should be removed from the binary number
  """
  return '0'* (num_bits - len(bin_num)) + bin_num 

def make_CPU_inputs(outFile):
  """
  create the tests inputs for the parity checker
  """

  encodings = {'halt' : '0000',
               'nop'  : '0001',
               'load' : '0010',
               'move' : '0011',
               'andr' : '0100',
               'andi' : '0101',
               'orr'  : '0110',
               'ori'  : '0111',
               'xorr' : '1000',
               'xori' : '1001',
               'neg'  : '1011',
               'addr' : '1100',
               'addi' : '1101',
               'subr' : '1110',
               'subi' : '1111'}
  
  with open(outFile, 'w') as inputs:
    count = 0
    inputs.write('v2.0 raw\n')
    inputs.write(encode(encodings['load'], 0, 0, 3))  #reg0 = 3
    inputs.write(encode(encodings['load'], 1, 0, 6))  #reg1 = 6
    inputs.write(encode(encodings['nop'],  0, 0, 5))  #no change
    inputs.write(encode(encodings['move'], 2, 1, 0))  #reg2 = reg1 = 6
    inputs.write(encode(encodings['andr'], 3, 0, 1))  #reg3 = reg0 & reg1 = 3 & 6 = 2
    inputs.write(encode(encodings['andi'], 4, 3, 3))  #reg4 = reg3 & 3 = 2 & 3 = 2
    inputs.write(encode(encodings['orr'],  5, 2, 0))  #reg5 = reg2 | reg0 = 6 | 3 = 7
    inputs.write(encode(encodings['ori'],  6, 3, 12)) #reg6 = reg3 | 12 = 2 | 12 = 14
    inputs.write(encode(encodings['xorr'],  7, 2, 0))  #reg7 = reg2 ^ reg0 = 6 | 3 = 5
    inputs.write(encode(encodings['xori'], 8, 6, 15)) #reg8 = reg6 ^ 15 = 14 ^ 15 = 1
    inputs.write(encode(encodings['neg'],  9, 3, 8))  #reg9 = -reg3 = -2
    inputs.write(encode(encodings['addr'], 10, 7, 7)) #reg10 = reg7 + reg7 = 5 + 5 = 10
    inputs.write(encode(encodings['addi'], 11, 1, 3)) #reg11 = reg1 + 3 = 6 + 3 = 9
    inputs.write(encode(encodings['subr'], 12, 6, 2)) #reg12 = reg6 - reg2 = 14 - 6 = 8 
    inputs.write(encode(encodings['subi'], 13, 8, 5)) #reg13 = reg8 - 5 = 1 - 5 = -4
    inputs.write(encode(encodings['halt'], 14, 0, 5)) #halt
def encode(op, dest, reg1, reg2):
  return hex(int(op + bit_extend(bin(dest)[2:], 4) +
             bit_extend(bin(reg1)[2:], 4) +
             bit_extend(bin(reg2)[2:], 4),2))[2:] + '\n'

        
if __name__ == '__main__':
  make_CPU_inputs('CPU_Inputs.txt')
