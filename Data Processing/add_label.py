def add_label():
    list = []
    # for i in range(7):
    with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/wjy_testing.txt" ) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line + ',' + '1' + '\n'
            list.append(line)
    with open("C:/Users/nicho/Google Drive/EECS221 Data Collection/Linear Regression/wjy_testing.txt", 'w') as f:
        for element in list:
            f.write(element)
        list = []


add_label()

# def add_label():
#     list = []
#
#     i = 0
#     with open("C:/Users/nicho/Google Drive/EECS221 Traning Data/user.txt") as f:
#         for line in f:
#             i += 1
#             line = line.rstrip('\n')
#             if i <= 344:
#                 line = line + ',' + '0' + '\n'
#                 list.append(line)
#             else:
#                 line = line + ',' + '1' + '\n'
#                 list.append(line)
#     with open("C:/Users/nicho/Google Drive/EECS221 Traning Data/user_with_label.txt", 'w') as f:
#         for element in list:
#             f.write(element)
#
# add_label()

