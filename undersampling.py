import numpy as np

if __name__ == '__main__':
    f = open('data/modified_data_all', 'r')
    new_file = open('data/sampled_train', 'w')
    for i, line in enumerate(f):
        line = line.strip()
        line_split = line.split(' ')
        if line_split[-1] == '1':
            new_file.write(line + '\n')
        else:
            if np.random.uniform() < 0.1:
                new_file.write(line + '\n')
    f.close()
    new_file.close()