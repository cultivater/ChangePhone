
if __name__ == "__main__":
    f = open('data/raw_data2', 'r')
    newf = open('data/good_data_no_01', 'w')
    for i, line in enumerate(f):
        if i % 1000000 == 0:
            print(i)
        line = line.strip()
        line = line.split('\t')
        if line[-1] != '201801' and line.count('\\N') < 6:
            for e in line:
                newf.write(e + '\t')
            newf.write('\n')
    f.close()