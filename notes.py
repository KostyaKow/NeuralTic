
#board 0..8
#x/o/e = 1, 2, 3

#give color and current board, return move
def play(color, board):
   return 1

def sig(z):
   return 1/(1+z^(-z))

def dot(v1, v2):
   sum = 0
   assert(len(v1) == len(v2))
   for i in range(0, len(v1)):
      sum += v1[i] * v2[i]
   return sum

def neuron(input, weights, thres):
   return sig(dot(input, weights) + thres)

x = neuron([0, 1], [2, 4], 5)

