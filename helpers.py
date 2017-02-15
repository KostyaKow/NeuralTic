#!/usr/bin/python3

#import impl, helpers
#impl.reload(helpers)

e_ = 2.7182818284590452353602874713

def sigma(z):
   return 1 / (1+e_**(-z))

def repeat_num(num, times):
   ret = []
   for i in range(0, times):
      ret.append(num)
   return ret

class Neuron:
   def __init__(self, weights, bias, inputs=None):
      self.weights = weights
      self.inputs = inputs
      self.bias = bias

   def calculate_perceptron(self, inputs=None):
      if inputs is not None:
         self.inputs = inputs
      ret = 0
      for w, b in zip(self.weights, self.inputs):
         ret += w*b
      ret -= self.bias
      #print('perc:', ret)
      return ret

   def calculate(self, inputs=None):
      if inputs is not None:
         self.inputs = inputs
      ret = sigma(self.calculate_perceptron())
      print('sig:', round(ret, 3))
      return ret


########digit exercise


#input: 0-9, output: 10 neurons representing number
def num_to_input(n):
   ret = []
   for i in range(0, 9):
      if i+1 == n:
         ret.append(1.0)
      else:
         ret.append(0.0)
   return ret

#print(num_to_input(3))

def run(num):
   #num = 2 #0, 1, 2

   input_num = num_to_input(num)
   print('input_num:', input_num)

   #1/0 (lsb)
   weights_a = [20, 0, 20] + repeat_num(0, 7) #+ repeat_num(0, 9)
   neuron_a = Neuron(weights_a, bias=10)

   has_a = neuron_a.calculate(input_num)

   #2/0
   weights_b = [0, 20, 20] + repeat_num(0, 7)
   neuron_b = Neuron(weights_b, bias=10)

   has_b = neuron_b.calculate(input_num)

   #4/0
   weights_c = [20, 20] + repeat_num(0, 8)
   neuron_c = None

   #8/0 (msb)
   neuron_d = None


   print('input: %i \ta1: %f b2: %f' % (num, has_a, has_b))



