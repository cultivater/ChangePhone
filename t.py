import numpy as np
from sklearn.utils import resample
from sklearn.model_selection import train_test_split,KFold
from sklearn import tree
from sklearn.externals import joblib
from sklearn.metrics import precision_score, accuracy_score, recall_score, roc_auc_score
from sklearn import ensemble
from sklearn.externals.six import StringIO
import os
training = True
if __name__ == '__main__':
    print('tree,using undersampled data:')
    total_data = np.loadtxt('data/modified_data_070811')
    # 0.8 train 0.2 test
    # x_train, x_test, y_train, y_test = train_test_split(total_data[:, :(total_data.shape[1]-1)],
    #                                                     total_data[:, (total_data.shape[1]-1)],
    #                                                     test_size=0.2)
    kf = KFold(n_splits=5)
    X = total_data[:, :(total_data.shape[1] - 1)]
    y = total_data[:, (total_data.shape[1] - 1)]
    acc, precision, recall, auc = [], [], [], []
    for train_index, test_index in kf.split(X):
        x_train, x_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
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

        print('now negative: ', majority_undersampled.shape[0])
        new_train = np.vstack((xy_train_positive, majority_undersampled))
        new_x_train = new_train[:, :(total_data.shape[1]-1)]
        new_y_train = new_train[:, (total_data.shape[1]-1)]
        if training:
            clf = ensemble.RandomForestClassifier()
            clf.fit(new_x_train, new_y_train)
            # joblib.dump(clf, 'model/undersampling.m')
        else:
            clf = joblib.load('model/undersampling.m')

        y_predict = clf.predict(x_test)
        acc.append(accuracy_score(y_test, y_predict))
        precision.append(precision_score(y_test, y_predict))
        recall.append(recall_score(y_test, y_predict))
        auc.append(roc_auc_score(y_test, y_predict))

    acc = np.asarray(acc)
    precision = np.asarray(precision)
    recall = np.asarray(recall)
    auc = np.asarray(auc)
    print('acc: ', acc.mean())
    print('precision: ', precision.mean())
    print('recall: ', recall.mean())
    print('auc:', auc.mean())


