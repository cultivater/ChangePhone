from sklearn import tree
import numpy as np
from sklearn.externals import joblib

# dictionary of uncontinuous variables
age, sex, group_code, net_tpye, brand, type, month, avg_month, var_month = [], [], [], [], [], [], [], [], []
def check(dict,element):
    if element in dict:
        return dict.index(element)
    else:
        dict.append(element)
        return dict.index(element)

def reWriteTxt(filename, newfilename):
    f = open(filename, 'r')
    new_file = open(newfilename, 'w', encoding='UTF-8')
    splited_line = []
    write_line = [-1]*10
    for line in f:
        # splited_line.append(line.split(', '))
        line = line.strip()
        line_split = line.split('    ')
        # transform feature
        write_line[0] = check(age, line_split[2])  # age
        write_line[1] = check(sex, line_split[3])
        write_line[2] = check(group_code, line_split[4])
        write_line[3] = check(net_tpye, line_split[5])
        write_line[4] = check(brand, line_split[6])
        write_line[5] = check(type, line_split[7])
        write_line[6] = check(month, line_split[8])
        write_line[7] = check(avg_month, line_split[9])
        write_line[8] = check(var_month, line_split[10])
        write_line[9] = line_split[11]
        for e in write_line:
            new_file.write(str(e)+' ')
        new_file.write('\n')
    f.close()


training = False
if __name__ == '__main__':
    reWriteTxt('data/tst.data','data/newtst.data')
    # reWriteTxt('data/adult.test', 'data/newtest.data')
    # train_data = np.loadtxt('data/newtrain.data')
    # test_data = np.loadtxt('data/newtest.data')
    # # Generate dummy data
    # x_train = train_data[:, :14]
    # y_train = train_data[:, 14]
    # x_test = test_data[:, :14]
    # y_test = test_data[:, 14]
    # if training:
    #     clf = tree.DecisionTreeClassifier()
    #     clf.fit(x_train, y_train)
    #     joblib.dump(clf, "model/tree_model.m")
    # else:
    #     clf = joblib.load("model/tree_model.m")
    # print('acc:', clf.score(x_test, y_test))
    # SystemExit()

