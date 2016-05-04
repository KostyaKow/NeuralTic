#board 0..8
#0, 1, 2
#3, 4, 5
#6, 7, 8

#e/x/o = 1, 2, 3

#pass string, first char being current player, rest being board
def get_training_raw():
   return {
      '2111111111' : 4, #x first go in center
      '3111111111' : 4, #o first go in center
      '2221111111' : 2, #x got top two, make row
      '3331111111' : 2, #o got top two, make row
      '2211211111' : 6, #o got vert two, make col
      '3211211111' : 6, #x opponent got vert two, block
   }

#converts entry from get_training_raw()
#player = 2|3
#lst_in = lst of characters in input string
#lst_out = lst with all 0 except needed output
class TrainingEntry:
   def __init__(entry, out):
      self.player = entry[0]

      self.lst_in = []
      for x in entry:
         self.lst_in.append(x)

      self.lst_out = []

      for x in range(0, len(entry)-1):
         if x == out:
            self.lst_out.append(1)
         else:
            self.lst_out.append(0)

def get_training():
   raw_entries = get_training_raw()
   entries = []
   for (key, entry) in raw_entries:
      entries.append(TrainingEntry(key, entry))
   return entries

class Neuron:
   def __init__(length):
      self.weights = repeat(length, 0)
      self.thres = 0
   def set_weight(i, n):
      self.weights[i] = n
   def set_weights(weights):
      self.weights = weights
   def set_thres(n):
      self.thres = n
   def eval(input):
      return sig(dot(input, self.weights) + self.thres)

#x = neuron([0, 1], [2, 4], 5)

def main():
   neurons = repeat(Neuron, 10)
   entries = get_training()

   num_iter = 100
   for i in range(0, num_iter):
      pass

#give color and current board, return move
def make_move(color, board):
   return 1

#def cost(weights, thres, desired, actual, n_inputs, desired):
#   return 1/(2*n_inputs)*((desired - actual)^2)


#rand funcs
def repeat(x, n):
   ret = []
   for i in range(0, n):
      ret.append(x)
   ret

#math crap
def sig(z):
   return 1/(1+z^(-z))

def dot(v1, v2):
   sum = 0
   assert(len(v1) == len(v2))
   for i in range(0, len(v1)):
      sum += v1[i] * v2[i]
   return sum

