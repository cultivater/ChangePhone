
def extract_table(f, newfilename, month):
    newf = open('data/'+newfilename, 'w')
    # 从raw_data2里找出4个月的数据
    for line in f:
        line = line.strip()
        line = line.split('\t')
        if line[-1] == month:
            for e in line:
                newf.write(e + '\t')
            newf.write('\n')


if __name__ == "__main__":
    f = open('data/raw_data2', 'r')
    extract_table(f, 'raw_data2_201612', '201612')
    extract_table(f, 'raw_data2_201708', '201708')
    f.close()