from sklearn.feature_extraction import DictVectorizer
import numpy as np

if __name__ == '__main__':
    f = open('data/adult.data','r')
    featureList = []
    for i, line in enumerate(f):
        dic = {'age': 0, 'sex': '', 'group number': 0, 'net mode': 0,
               'brand': '', 'type': '', 'used_time': 0, 'avg_time': 0,
               'var_time': 0}
        line = line.strip()
        t = line.split('\t')
        try:
            dic['age'] = int(t[0])
        except:
            dic['age'] = 0
        dic['sex'] = t[1]
        try:
            dic['group number'] = int(t[2])
        except:
            dic['group number'] = 0
        try:
            dic['net mode'] = int(t[3])
        except:
            dic['net mode'] = 0
        dic['brand'] = t[4]
        dic['type'] = t[5]
        try:
            dic['used_time'] = float(t[6])
        except:
            dic['used_time'] = 0
        try:
            dic['avg_time'] = float(t[7])
        except:
            dic['avg_time'] = 0
        try:
            dic['var_time'] = float(t[8])
        except:
            dic['var_time'] = 0
        featureList.append(dic)
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    np.savetxt('nptxt', dummyX)
    print(dummyX)
    pass