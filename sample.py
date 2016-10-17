import sys
import numpy as np
from model import Model

#input: char_to_ix, ix_to_char, vocab_size
#       Wxh, Whh, Why, bh, by, hprev

path = sys.argv[1]

m = Model(path)

# main function
starting_char = sys.argv[2].decode(sys.argv[3])

print m.sample_char(starting_char)