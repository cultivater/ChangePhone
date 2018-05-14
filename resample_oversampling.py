import numpy as np
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.externals import joblib
from sklearn.metrics import precision_score, accuracy_score, recall_score, roc_auc_score
from sklearn import ensemble
training = True
if __name__ == '__main__':
    print('tree,using oversampled data:')
    total_data = np.loadtxt('data/newtrain.data')
    # 0.8 train 0.2 test
    x_train, x_test, y_train, y_test = train_test_split(total_data[:, :(total_data.shape[1]-1)],
                                                        total_data[:, (total_data.shape[1]-1)],
                                                        test_size=0.2)
    xy_train = np.hstack((x_train, np.matrix(y_train).transpose()))
    # split 0/1 rows
    xy_train_positive = xy_train[y_train[:] == 1, :]
    xy_train_negative = xy_train[y_train[:] == 0, :]

    print('positive: ', xy_train_positive.shape[0],' negative: ', xy_train_negative.shape[0])
    # oversampling minority
    minority_oversampled = resample(xy_train_positive,
                                     replace=True,  # sample with replacement
                                     n_samples=xy_train_negative.shape[0],  # num of majority
                                     random_state=123)  # seed

    print('now positive: ', minority_oversampled.shape[0])
    new_train = np.vstack((minority_oversampled, xy_train_negative))
    new_x_train = new_train[:, :(total_data.shape[1]-1)]
    new_y_train = new_train[:, (total_data.shape[1]-1)]
    if training:
        clf = ensemble.RandomForestClassifier()
        clf.fit(new_x_train, new_y_train)
        joblib.dump(clf, 'model/oversampling.m')
    else:
        clf = joblib.load('model/oversampling.m')

    y_predict = clf.predict(x_test)

    print('acc: ', clf.score(x_test, y_test))
    print('precision: ', precision_score(y_test, y_predict))
    print('recall: ', recall_score(y_test, y_predict))
    print('auc:', roc_auc_score(y_test, y_predict))