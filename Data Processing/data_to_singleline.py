def to_single_line():
    single_line = ''
    for i in range(26):
        with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/SVM/wjy/output" + str(i+1) +".txt" ) as f:
            for line in f:
                line = line.rstrip("\n")
                single_line = single_line + line + ','

        with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/SVM/wjy/singleline/single" + str(i+1) +".txt", 'w') as f:
            f.write(single_line)
            single_line = ''



# to_single_line()

def combine_file():
    single_line = ''
    for i in range(26):
        with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/SVM/wjy/singleline/single" + str(i+1) +".txt" ) as f:
            for line in f:
                single_line = single_line + line.rstrip(',') + '\n'

    with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/SVM/wjy_combined.txt", 'w' ) as f:
        f.write(single_line)
        single_line = ''

combine_file()


