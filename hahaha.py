if __name__ == '__main__':
    f4 = open('data/selected_201712', 'r',encoding='UTF-8')
    f8 = open('data/appdata201712', 'r',encoding='UTF-8')
    f3 = open('data/app+rawdata2_201712', 'w')
    appdata_list, rawdata_list = [], []

    for line in f4:
        line = line.strip().split('\t')
        rawdata_list.append(line)
    for line in f8:
        line = line.strip().split('\t')
        appdata_list.append(line)
    for i, e in enumerate(appdata_list):
        for e2 in rawdata_list:
            if e[0] == e2[0]:
                line = e2[:-2] + e[1:-1] + e2[-2:]
                for e3 in line:
                    f3.write(e3 + '\t')
                f3.write('\n')
                break