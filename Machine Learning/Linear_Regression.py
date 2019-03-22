import matplotlib.pyplot as plt
import numpy as np

#load data
def load_exdata(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            if (len(line)< 4):
                break
            line[3] = line[3].split('\n')[0]
            current = [float(item) for item in line]
            data.append(current)
    return data
 
data = load_exdata('training.txt')
data = np.array(data,np.float64)
 
x = data[:,(0,1,2)].reshape((-1,3))
y = data[:,3].reshape((-1,1))
m = y.shape[0] 

# Print out some data points
print('First 10 examples from the dataset: \n')
print(' x = ',x[range(10),:],'\ny=',y[range(10),:])


def featureNormalize(X):
    X_norm = X;
    mu = np.zeros((1,X.shape[1]))
    sigma = np.zeros((1,X.shape[1]))# x.shape[1]=3 [[0,0,0]]
    for i in range(X.shape[1]):
        mu[0,i] = np.mean(X[:,i]) # mean
        sigma[0,i] = np.std(X[:,i])     # standard
#     print(mu)
#     print(sigma)
    X_norm  = (X - mu) / sigma
    return X_norm,mu,sigma
 

def computeCost(X, y, theta):
    #m = y.shape[0]
    #J = (np.sum((X.dot(theta) - y)**2)) / (2*m)
    C = X.dot(theta) - y
    J2 = (C.T.dot(C))/ (2*m)
    return J2
 

def gradientDescent(X, y, theta, alpha, num_iters):
    #m = y.shape[0]
    #print(m)
    J_history = np.zeros((num_iters, 1)) #[[1],[1],……]
    for iter in range(num_iters):
        # alpha/m * (WX - Y)*x(i)， (3,m)*(m,1)  X (m,3)*(3,1) = (m,1)
        theta = theta - (alpha/m) * (X.T.dot(X.dot(theta) - y))
        J_history[iter] = computeCost(X, y, theta)
        #print(iter,J_history[iter])
    return J_history,theta
     
iterations = 2000  # count of iterations
alpha = 0.01    #Learning Rate
x,mu,sigma = featureNormalize(x)
X = np.hstack([x,np.ones((x.shape[0], 1))])
 
theta = np.zeros((4, 1))
 
j = computeCost(X,y,theta)
J_history,theta = gradientDescent(X, y, theta, alpha, iterations)
 
print('Theta found by gradient descent',theta)

plt.plot(J_history)
plt.ylabel('lost');
plt.xlabel('iter count')
plt.title('convergence graph')

def predict(data):
    testx = np.array(data)
    testx = ((testx - mu) / sigma)
    testx = np.hstack([testx,np.ones((testx.shape[0], 1))])
    user = testx.dot(theta)
    return user

datatest = load_exdata('testing.txt')
datatest = np.array(datatest,np.float64)
xtest = datatest[:,(0,1,2)].reshape((-1,3))
ytest = datatest[:,3].reshape((-1,1)) 
mtest = ytest.shape[0]

sum = 0
for i in range(mtest):
    #print(predict(xtest[i]))
    if(predict(xtest[i])>=0.5):
        res = 1.0
    else:
        res = 0
    sum = sum + res
average = sum/mtest
print ('user:',average)








