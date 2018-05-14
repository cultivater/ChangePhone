if __name__ == '__main__':
    f3 = open('data/app+rawdata2', 'w')
    f4 = open('data/selected_201707', 'r')
    f5 = open('data/selected_201708', 'r')
    f6 = open('data/selected_201711', 'r')
    f7 = open('data/selected_201712', 'r')

    f8 = open('data/appdata201707', 'r')
    f9 = open('data/appdata201708', 'r')
    f10 = open('data/appdata201711', 'r')
    f11 = open('data/appdata201712', 'r')

    for line_app in f8:
        line_app = line_app.strip().split('\t')
        for line_raw in f4:
            line_raw = line_raw.strip().split('\t')
            if line_raw[0] == line_app[0]:
                line = line_raw[:-2] + line_app[1:-1] + line_raw[-2:]
                for e in line:
                    f3.write(e + '\t')
                f3.write('\n')
                break
    f3.close()
    f3 = open('data/app+rawdata2', 'a')
    for line_raw in f5:
        line_raw = line_raw.strip().split('\t')
        for line_app in f9:
            line_app = line_app.strip().split('\t')
            if line_raw[0] == line_app[0]:
                line = line_raw[:-2] + line_app[1:-1] + line_raw[-2:]
                for e in line:
                    f3.write(e + '\t')
                f3.write('\n')
                break
    f3.close()
    f3 = open('data/app+rawdata2', 'a')
    for line_raw in f6:
        line_raw = line_raw.strip().split('\t')
        for line_app in f10:
            line_app = line_app.strip().split('\t')
            if line_raw[0] == line_app[0]:
                line = line_raw[:-2] + line_app[1:-1] + line_raw[-2:]
                for e in line:
                    f3.write(e + '\t')
                f3.write('\n')
                break
    f3.close()
    f3 = open('data/app+rawdata2', 'a')
    for line_raw in f7:
        line_raw = line_raw.strip().split('\t')
        for line_app in f11:
            line_app = line_app.strip().split('\t')
            if line_raw[0] == line_app[0]:
                line = line_raw[:-2] + line_app[1:-1] + line_raw[-2:]
                for e in line:
                    f3.write(e + '\t')
                f3.write('\n')
                break
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f11.close()