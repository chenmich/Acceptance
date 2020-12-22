import collections
import itertools

#argments for sample

alpha_x = {0.05:-1.645, 0.10:-1.282,
           0.15:-1.036, 0.20:-0.842,
           0.30:-0.524, 0.40:-0.253,
           0.50: 0.0,   0.60: 0.253,
           0.80: 0.842, 0.95: 1.645}
alpha_x = collections.OrderedDict(alpha_x)

sample_num = [3, 8, 12, 18, 22, 30, 50]
f_cu0 = [20, 25, 30, 35, 40, 45, 50, 55, 60]
sigma = [2.5, 3.5, 4.0, 5.0, 6.0, 8.0, 10.0]
sample = [(x, y) for x in f_cu0 for y in sigma]
all_samples = [(x, y) for x in sample for y in sample_num]

#argments for model
a = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 
     1.00, 1.05, 1.10, 1.15, 1.20]
b = [1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 
    1.70, 1.75, 1.80, 1.85, 1.90]
c = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 
     1.00, 1.05, 1.10, 1.15, 1.20]
d = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 
     1.00, 1.05, 1.10, 1.15, 1.20]
e = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]


__mode1_arg = [(x, y) for x in a for y in b]
__model2_arg = [(x, y) for x in c for y in b]
__combined_arg = itertools.zip_longest(__model2_arg, e, fillvalue=None)
__com = [(x[0][0], x[0][1], x[1]) for x in __combined_arg]
all_arg = [(a, b, c, d, e) for a, b in __mode1_arg 
                            for c, d, e in __com]

