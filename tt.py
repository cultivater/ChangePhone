if __name__ == '__main__':
    cnt = 0
    for i in range(10):
        f = open('~/traintable_app/00000'+str(i)+'_0', 'r')
        for line in f:
            cnt += 1
    for i in range(5):
        f = open('~/traintable_app/00001'+str(i)+'_0', 'r')
        for line in f:
            cnt += 1
    print('total lines: ', cnt)
    ma3_s_call_len, ma3_s_call_qty, ma3_s_call_oth_qty = [], [], []
    var3_s_call_len, var3_s_call_qty, var3_s_call_oth_qty = [], [], []
    ma3_r_call_len, ma3_r_call_qty, ma3_r_call_oth_qty = [], [], []
    var3_r_call_len, var3_r_call_qty, var3_r_call_oth_qty = [], [], []
    ma3_flow, ma3_curr_fee, ma3_owe_fee = [], [], []
    var3_flow, var3_curr_fee, var3_owe_fee = [], [], []
    write_line[9] = check_null(line_split[11])
    write_line[10] = check_null(line_split[12])
    write_line[11] = check_null(line_split[13])
    write_line[12] = check_null(line_split[14])
    write_line[13] = check_null(line_split[15])
    write_line[14] = check_null(line_split[16])
    write_line[15] = check_null(line_split[17])
    write_line[16] = check_null(line_split[18])
    write_line[17] = check_null(line_split[19])
    write_line[18] = check_null(line_split[20])
    write_line[19] = check_null(line_split[21])
    write_line[20] = check_null(line_split[22])
    write_line[21] = check_null(line_split[23])
    write_line[22] = check_null(line_split[24])
    write_line[23] = check_null(line_split[25])
    write_line[24] = check_null(line_split[26])
    write_line[25] = check_null(line_split[27])
    write_line[26] = check_null(line_split[28])