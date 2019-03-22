import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as graph


# import matplotlib
# matplotlib.use('TkAgg')

# from matplotlib.backends import _macosx

# Function to read the data from file
def read_data(par_filename):
    vl = []
    with open(par_filename, "r") as file_lines:
        for line in file_lines:
            vl.append(map(float, line.split(',')))
    file_lines.close()
    # vl = np.array(vl)
    print vl
    return vl

# print read_data("dataset.txt")


# Function to read the lables from file
def read_labels(file):
    ll = []
    with open(file, "r") as file_lines:
        for line in file_lines:
            ll.append(line)
        # ll = np.array(ll)
    print ll
    return ll
# print read_labels("label.txt")

# Function to read the features from file
# def read_features(vl):
# 	lp = vl
# 	for r in lp:
# 		r.remove(r[12])
# 	return lp;

# Function to compute the classification using SVM
def compute_SVC(train_f, train_l):
    C = 1.0
    cache_size = 200
    class_weight = None
    coef0 = 0.0
    decision_function_shape = None
    degree = 3
    gamma = 'auto'
    kernel = 'rbf'
    max_iter = -1
    probability = False
    random_state = None
    shrinking = True
    tol = 0.001
    verbose = False
    c = svm.SVC(kernel='linear')
    c.fit(train_f, train_l)
    return c


# Function to calculate the accuracy
def compute_accuracy(test_f, test_l, c):
    pred = c.predict(test_f)
    # print pred
    pred_accu = accuracy_score(test_l, pred)
    return pred_accu


# Function to compute the confusion matrix
def compute_confusion_matrix(test_f, test_l, c):
    pred = c.predict(test_f)
    x = confusion_matrix(test_l, pred)
    return x


# Function to compute the error
def compute_error(t_f, t_l, c):
    err = c.score(t_f, t_l)
    return err


# Function to split the data based on percentage
def split_data(f, percent):
    tot = len(f)
    req_xt = int((float(percent) / 100) * tot)
    # req_yt = tot - req_xt
    xt_get = []
    for s in range(0, req_xt):
        xt_get.append(f[s])
    yt_get = []
    for d in range(req_xt, tot):
        yt_get.append(f[d])
    xyt = []
    xyt.append(xt_get)
    xyt.append(yt_get)
    return xyt



# [[[],[],[],...],[[],[],[],...]], [[...],[...]]


# Function to plot the training and testing errors
def compute_plot(filename):
    test_plt = []
    train_plt = []
    percent_plt = []
    with open(filename, "r") as lines_in_file:
        for c1 in lines_in_file:
            percent_plt.append(c1.split()[0])
            train_plt.append(c1.split()[1])
            test_plt.append(c1.split()[2])

    fig = graph.figure()
    ax = fig.add_subplot(111)
    # graph.ylim((50, 100))
    # graph.yticks(my_y_ticks)

    graph.plot(percent_plt, test_plt,  'bo', label='Testing Accuracy')
    graph.plot(percent_plt, test_plt, 'b')
    # graph.plot(percent_plt, train_plt, 'ro', label='Testing Accuracy')

    # graph.gca().invert_yaxis()
    # graph.plot(percent_plt, train_plt, 'r')
    ax.set_xlabel('Percentage of Training data')
    ax.set_ylabel('Percentage of Accuracy')
    graph.legend(loc='upper left', numpoints=1)
    graph.title("Accuracy of testing data")
    graph.show()
    return


# Starting of the flow of program
read_data1 = read_data("1_combined.txt")
read_data_labels1 = read_labels("label-1.txt")
read_data2 = read_data("0_combined.txt")
read_data_labels2 = read_labels("label-2.txt")

# read_data_features = read_features(read_data)
input_percent = [40, 50, 60, 70, 80, 90]
file_created1 = open('Generated_accuracy_table.dat', 'w')
file_created2 = open('Generated_error_table.dat', 'w')
for pri in range(0, len(input_percent)):
    x1 = split_data(read_data1, input_percent[pri])
    x2 = split_data(read_data_labels1, input_percent[pri])
    x3 = split_data(read_data2, input_percent[pri])
    x4 = split_data(read_data_labels2, input_percent[pri])
    # print x1
    read_data_labels_train = x2[0] + x4[0]
    read_data_train = x1[0] + x3[0]
    read_data_labels_test = x2[1] + x4[1]
    read_data_test = x1[1] + x3[1]
    model_svc = compute_SVC(read_data_train, read_data_labels_train)
    # print "train"
    accu_percent_train = compute_accuracy(read_data_train, read_data_labels_train, model_svc) * 100
    # print "test"
    accu_percent_test = compute_accuracy(read_data_test, read_data_labels_test, model_svc) * 100
    train_err = compute_error(read_data_train, read_data_labels_train, model_svc)
    test_err = compute_error(read_data_test, read_data_labels_test, model_svc)
    file_created1.write("%f %f %f \n" % (input_percent[pri], accu_percent_train, accu_percent_test))
    # file_created2.write("%f %f %f \n" % (input_percent[pri], train_err, test_err))
    conf_mat = compute_confusion_matrix(read_data_train, read_data_labels_train, model_svc)
    print conf_mat
    conf_mat1 = compute_confusion_matrix(read_data_test, read_data_labels_test, model_svc)
    print conf_mat1
    # print accu_percent_train
    print accu_percent_test
    # print train_err
file_created1.close()
# file_created2.close()
# conf_mat = compute_confusion_matrix(read_data_features_train,read_data_labels_train,model_svc);
# print conf_mat
# conf_mat1 = compute_confusion_matrix(read_data_features_test,read_data_labels_test,model_svc);
# print conf_mat1

compute_plot("Generated_accuracy_table.dat")
# compute_plot("Generated_error_table.dat")
