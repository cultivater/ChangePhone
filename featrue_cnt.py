from sklearn.feature_extraction import DictVectorizer
import numpy as np

if __name__ == '__main__':
    f = open('data/adult.data','r')
    dic1, dic2 = {}, {}
    for i, line in enumerate(f):
        line = line.strip()
        t = line.split(',')

        if t[1] in dic1.keys():
            dic1[t[1]] += 1
        else:
            dic1[t[1]] = 1
    dict = sorted(dic1.items(), key=lambda d: d[1], reverse=True)
    print(dict)
    pass