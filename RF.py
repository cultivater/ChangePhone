import numpy as np
from sklearn.utils import resample
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn import tree
from sklearn.externals import joblib
from sklearn.metrics import precision_score, accuracy_score, recall_score, roc_auc_score
from sklearn import ensemble

training = True
if __name__ == '__main__':
    print('simply use RF:')
    total_data = np.loadtxt('data/newtrain.data')
    # 0.8 train 0.2 test
    # x_train, x_test, y_train, y_test = train_test_split(total_data[:, :(total_data.shape[1]-1)],
    #                                                     total_data[:, (total_data.shape[1]-1)],
    #                                                     test_size=0.2)
    X = total_data[:, :(total_data.shape[1]-1)]
    y = total_data[:, (total_data.shape[1]-1)]
    kf = KFold(n_splits=5)
    acc, precision, recall, auc = [], [], [], []
    for train_index, test_index in kf.split(X):
        x_train, x_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf = ensemble.RandomForestClassifier()
        clf.fit(x_train, y_train)
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