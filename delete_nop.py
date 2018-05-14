if __name__ == '__main__':
    f = open('data/tst.data', 'r')
    f1 = open('data/raw_data2_deleted', 'w')
    for line in f:
        line = line.strip()
        t = line.split('    ')
        t1 = t[2:11]
        if '\\N' in t1 or t[-2] == '\\N':
            continue
        for e in t1:
            f1.write(str(e)+' ')
    f.close()