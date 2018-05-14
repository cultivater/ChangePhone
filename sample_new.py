'''
    sample raw_data2_deleted and feature extraction
'''
import numpy as np
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn.externals import joblib
from sklearn.metrics import precision_score, accuracy_score, recall_score, roc_auc_score
from sklearn import ensemble
from sklearn.externals.six import StringIO

import os
training = True
sampling_num = 10000000
sampling_percent = 0.5
if __name__ == '__main__':
    print('sample raw_data2_deleted and feature extraction; tree,using undersampled data:')
    total_data = open('data/raw_data2_deleted').readlines()
    total_list, X, y = [], [], []
    for line in total_data:
        line = line.strip().split(' ')
        total_list.append(line)
    total_resampled = resample(total_list,
                               replace=False,  # sample without replacement
                               n_samples=int(len(total_list)*sampling_percent),
                               random_state=123)  # seed
    featureList = []
    for i, t in enumerate(total_resampled):

        dic = {'age': 0, 'sex': '', 'group number': 0, 'net mode': 0,
               'brand': '', 'used_time': 0, 'avg_time': 0,
               'var_time': 0, 'calling_len_avr': 0.0, 'calling_qty_avr': 0.0,
               'calling_number_qty_avr': 0.0, 'calling_len_var': 0.0,
               'calling_qty_var': 0.0, 'calling_number_qty_var': 0.0,
               'called_len_avr': 0.0, 'called_qty_avr': 0.0,
               'called_number_qty_avr': 0.0, 'called_len_var': 0.0,
               'called_qty_var': 0.0, 'called_number_qty_var': 0.0,
               'flow_avr': 0.0, 'fee_avr': 0.0, 'owe_fee': 0.0,
               'flow_var': 0.0, 'fee_var': 0.0, 'owe_var': 0.0,
               }

        dic['age'] = int(t[0])
        dic['sex'] = t[1]
        dic['group number'] = int(t[2])
        dic['net mode'] = int(t[3])
        if brand_dict[t[4]] > 50000:
            dic['brand'] = t[4]
        else:
            dic['brand'] = 'too small'

        dic['used_time'] = float(t[6])
        dic['avg_time'] = float(t[7])
        dic['var_time'] = float(t[8])

        dic['calling_len_avr'] = float(t[9])
        dic['calling_qty_avr'] = float(t[10])
        dic['calling_number_qty_avr'] = float(t[11])

        dic['calling_len_var'] = float(t[12])
        dic['calling_qty_var'] = float(t[13])
        dic['calling_number_qty_var'] = float(t[14])

        dic['called_len_avr'] = float(t[15])
        dic['called_qty_avr'] = float(t[16])
        dic['called_number_qty_avr'] = float(t[17])

        dic['called_len_var'] = float(t[18])
        dic['called_qty_var'] = float(t[19])
        dic['called_number_qty_var'] = float(t[20])

        dic['flow_avr'] = float(t[21])
        dic['fee_avr'] = float(t[22])
        dic['owe_fee'] = float(t[23])
        dic['flow_var'] = float(t[24])
        dic['fee_var'] = float(t[25])
        dic['owe_var'] = float(t[26])

        y.append(int(t[27]))
        featureList.append(dic)
    vec = DictVectorizer()
    dummyX = vec.fit_transform(featureList).toarray()
    y = np.asarray(y)
    # 0.8 train 0.2 test
    x_train, x_test, y_train, y_test = train_test_split(dummyX, y, test_size=0.2)
    xy_train = np.hstack((x_train, np.matrix(y_train).transpose()))
    # split 0/1 rows
    xy_train_positive = xy_train[y_train[:] == 1, :]
    xy_train_negative = xy_train[y_train[:] == 0, :]

    print('positive: ', xy_train_positive.shape[0],' negative: ', xy_train_negative.shape[0])
    # undersampling majority
    majority_undersampled = resample(xy_train_negative,
                                     replace=True,  # sample with replacement
                                     n_samples=xy_train_positive.shape[0],  # num of majority
                                     random_state=123)  # seed

    print('now positive: ', majority_undersampled.shape[0])
    new_train = np.vstack((xy_train_positive, majority_undersampled))
    new_x_train = new_train[:, :(new_train.shape[1]-1)]
    new_y_train = new_train[:, (new_train.shape[1]-1)]
    if training:
        clf = tree.DecisionTreeClassifier()
        # clf = ensemble.RandomForestClassifier()
        clf.fit(new_x_train, new_y_train)
        joblib.dump(clf, 'model/undersampling.m')
    else:
        clf = joblib.load('model/undersampling.m')

    y_predict = clf.predict(x_test)

    print('acc: ', clf.score(x_test, y_test))
    print('precision: ', precision_score(y_test, y_predict))
    print('recall: ', recall_score(y_test, y_predict))
    print('auc:', roc_auc_score(y_test, y_predict))
    # with open("adult.dot", 'w') as f:
    #     f = tree.export_graphviz(clf, out_file=f)
    # # os.unlink('adult.dot')
