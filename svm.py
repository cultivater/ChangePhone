from sklearn import svm
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score, roc_auc_score
if __name__ == '__main__':
    total_data = np.loadtxt('data/feature_extraction_all')
    total_data = preprocessing.scale(total_data)
    # 0.8 train 0.2 test
    x_train, x_test, y_train, y_test = train_test_split(total_data[:, :(total_data.shape[1]-1)],
                                                        total_data[:, (total_data.shape[1]-1)],
                                                        test_size=0.2)
    # training
    clf = svm.SVC()
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    print('acc: ', clf.score(x_test, y_test))
    print('precision: ', precision_score(y_test, y_predict))
    print('recall: ', recall_score(y_test, y_predict))
    print('auc:', roc_auc_score(y_test, y_predict))