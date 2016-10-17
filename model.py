import numpy as np

class Model:
	def __init__(self, path):
		self.char_to_ix = self._load_matrix(path, "char_to_ix")
		self.ix_to_char = self._load_matrix(path, "ix_to_char")
		self.vocab_size = len(self.char_to_ix)
		self.Wxh = self._load_matrix(path, "Wxh")
		self.Whh = self._load_matrix(path, "Whh")
		self.Why = self._load_matrix(path, "Why")
		self.bh = self._load_matrix(path, "bh")
		self.by = self._load_matrix(path, "by")
		self.hprev = self._load_matrix(path, "hprev")

	def _load_matrix(self, path, filename):
		import pickle
		outfile = open(path + "/" + filename, "r");
		data = pickle.loads(outfile.read())
		outfile.close()
		return data

	def sample(self, h, seed_ix):
		x = np.zeros((self.vocab_size, 1))
		x[seed_ix] = 1
		ixes = []
		while True:
			h = np.tanh(np.dot(self.Wxh, x) + np.dot(self.Whh, h) + self.bh)
			y = np.dot(self.Why, h) + self.by
			p = np.exp(y) / np.sum(np.exp(y))
			ix = np.random.choice(range(self.vocab_size), p=p.ravel())
			if self.ix_to_char[ix] == "\n":
				break;
			x = np.zeros((self.vocab_size, 1))
			x[ix] = 1
			ixes.append(ix)
		return ixes

	def sample_char(self, first_char):
		index = self.char_to_ix.get(first_char)
		if index == None:
			print "No such char:" + first_char
			return False

		index_seq = self.sample(self.hprev, index)
		txt = ''.join(self.ix_to_char[ix] for ix in index_seq)
		return '----\n %s \n----' % (txt, )
