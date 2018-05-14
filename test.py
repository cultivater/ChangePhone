import numpy as np
from keras.models import Sequential,load_model
from keras.layers import Dense, Dropout
# dictionary of uncontinuous variables
work_class = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay',
              'Never-worked']

education = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th',
             '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']

marital_status = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent',
                  'Married-AF-spouse']

occupation = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
              'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
              'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

relationship = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

race = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

sex = ['Female', 'Male']

native_country = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany',
                  'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran',
                  'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland',
                  'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary',
                  'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago',
                  'Peru', 'Hong', 'Holand-Netherlands']
salary = ['<=50K', '>50K']

def reWriteTxt(filename, newfilename):
    f = open(filename, 'r')
    new_file = open(newfilename, 'w')
    splited_line = []
    write_line = [-1]*15
    for line in f:
        # splited_line.append(line.split(', '))
        line = line.strip()
        line_split = line.split(', ')
        # continuous feature
        try:
            write_line[0] = line_split[0]
        except:
            break
        try:
            write_line[2] = line_split[2]
        except:
            break
        try:
            write_line[4] = line_split[4]
        except:
            break
        try:
            write_line[10] = line_split[10]
        except:
            break
        try:
            write_line[11] = line_split[11]
        except:
            break
        try:
            write_line[12] = line_split[12]
        except:
            break
        # uncontinuous feature
        try:
            write_line[1] = work_class.index(line_split[1])
        except:
            write_line[1] = -1
        try:
            write_line[3] = education.index(line_split[3])
        except:
            write_line[3] = -1
        try:
            write_line[5] = marital_status.index(line_split[5])
        except:
            write_line[5] = -1
        try:
            write_line[6] = occupation.index(line_split[6])
        except:
            write_line[6] = -1
        try:
            write_line[7] = relationship.index(line_split[7])
        except:
            write_line[7] = -1
        try:
            write_line[8] = race.index(line_split[8])
        except:
            write_line[8] = -1
        try:
            write_line[9] = sex.index(line_split[9])
        except:
            write_line[9] = -1
        try:
            write_line[13] = native_country.index(line_split[13])
        except:
            write_line[13] = -1
        try:
            write_line[14] = salary.index(line_split[14])
        except:
            break
        for e in write_line:
            new_file.write(str(e)+' ')
        new_file.write('\n')



    f.close()

training = False
if __name__ == '__main__':
    # reWriteTxt('data/adult.data','data/newtrain.data')
    # reWriteTxt('data/adult.test', 'data/newtest.data')
    train_data = np.loadtxt('data/newtrain.data')
    test_data = np.loadtxt('data/newtest.data')
    # Generate dummy data
    x_train = train_data[:, :14]
    y_train = train_data[:, 14]
    x_test = test_data[:, :14]
    y_test = test_data[:, 14]
    if training:
        model = Sequential()
        model.add(Dense(64, input_dim=14, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])
        model.fit(x_train, y_train,
                  epochs=30,
                  batch_size=128)
        model.save('model/my_model.h5')
    else:
        model = load_model('model/my_model.h5')
    score = model.evaluate(x_test, y_test, batch_size=128)
    print(model.metrics_names)
    predict_y = model.predict(x_test)
    cnt = 0
    for i in range(len(predict_y)):
        if predict_y[i] == y_test[i]:
            cnt += 1
    print(score, cnt/len(predict_y))
