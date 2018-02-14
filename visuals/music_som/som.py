import numpy as np
import pandas as pd

chords_ = pd.read_csv('~/Downloads/chords.csv')
chords = chords_.drop('Label', axis=1)
chords = chords.reset_index(drop=True)
chords = chords.values

w = np.zeros((20,20,12))

def som(w):

    for i in np.arange(0,20):
        for j in np.arange(0,20):
            for k in np.arange(0,12):
                t = (i, j, k)
                w.itemset(t, np.random.rand())

    for s in np.arange(1,360):
        for t in np.arange(1,24):
            r = chords[np.random.choice(np.arange(1,24), replace=False)]
            i = get_index(r)
            for k in np.arange(0,20):
                for l in np.arange(0,20):
                    x = (k,l)
                    c = (1/3)*(20-1-(s/20))
                    C = np.exp(-1*(dist(i,x)**2/2*c**2))
                    w[k][l] = w[k][l] + C * (.02*s) * (r - w[k][l])
    return(w)

def get_index(v):
    x = 0
    y = 0
    best_score = 100000
    for i in range(0,20):
        for j in range(0,20):
            match = w[i][j]
            diff = match - v[0:]
            score = np.linalg.norm(diff)
            if(score < best_score):
                x = i
                y = j
                best_score = score
    return(x,y)

def dist(p1, p2):
    dx = (p2[0] - p1[0])
    dy = (p2[1] - p1[1])
    if dx >= 10:
        dx = 20-dx
    if dy >= 10:
        dy = 20-dy
    return np.sqrt(dx ** 2 + dy ** 2)
    #if i-k is higher than 10, 20-dist

w = som(w)

import operator


def get_index_two(v):
    x = 0
    y = 0
    v = v[1:]
    best_score = 100000
    for i in range(0,20):
        for j in range(0,20):
            match = w[i][j]
            diff = match - v
            score = np.linalg.norm(diff)
            if(score < best_score):
                x = i
                y = j
                best_score = score
    return (x, y, v[0])

e = []
for v in chords_:
    e.append(get_index_two(v))

for v in chords_:
    print(v)

chords_[0]
