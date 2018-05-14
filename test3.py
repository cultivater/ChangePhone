from sklearn.feature_extraction import DictVectorizer
import numpy as np

if __name__ == '__main__':
    f = open('data/adult.data','r')
    featureList = []
    label = []
    for i, line in enumerate(f):
        dic = {'age': 0, 'work class': '', 'fnlwgt': 0, 'education': '', 'education-num': 0,
               'marital-status': '', 'occupation': '', 'relationship': '', 'race': '',
               'sex': '', 'captital-gain': 0, 'captital-loss': 0, 'hours-per-week': 0,
               'native-country': ''}
        line = line.strip()
        t = line.split(',')
        dic['age'] = int(t[0])
        dic['work class'] = t[1]
        dic['fnlwgt'] = float(t[2])
        dic['education'] = t[3]
        dic['education-num'] = float(t[4])
        dic['marital-status'] = t[5]
        dic['occupation'] = t[6]
        dic['relationship'] = t[7]
        dic['race'] = t[8]
        dic['sex'] = t[9]
        dic['captital-gain'] = float(t[10])
        dic['captital-loss'] = float(t[11])
        dic['hours-per-week'] = float(t[12])
        dic['native-country'] = t[13]
        if t[14] == ' <=50K':
            label.append(0)
        else:
            label.append(1)
        featureList.append(dic)
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    print(dummyX.shape)
    label = np.matrix(label).transpose()
    print(label.shape)
    all = np.hstack((dummyX, label))
    np.savetxt('nptxt', all)
    pass