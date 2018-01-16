# Init the parameter
from random import randint
import numpy as np



class Simple_Perceptron:
    def __init__(self, train_data = [], real_result = [], eta = 1):
        self.w   =   np.zeros([1, len(train_data.T)], int)
        self.b   =   0
        self.eta =   eta
        self.train_data   = train_data
        self.real_result  = real_result
    def nomalize(self, x):
        if x > 0 :
            return 1
        else :
            return -1
    def model(self, x):
        # Here are matrix dot multiply get one value
        y = np.dot(x, self.w.T) + self.b
        # Use sign to nomalize the result
        predict_v = self.nomalize(y)
        return predict_v, y
    def update(self, x, y):
        # w = w + n*y_i*x_i
        self.w = self.w + self.eta*y*x
        # b = b + n*y_i
        self.b = self.b + self.eta*y
    def loss(slef, fx, y):
        return fx.astype(int)*y

    def train(self, count):
        while count > 0:
            # count--
            count = count - 1

            if len(self.train_data) <= 0:
                print("exception exit")
                break
            # random select one train data
            index = randint(0,len(self.train_data)-1)
            x = self.train_data[index]
            y = self.real_result.T[index]
            # wx+b
            predict_v, linear_y_v = self.model(x)
            # y_i*(wx+b) > 0, the classify is correct, else it's error
            if self.loss(y, linear_y_v) > 0:
                continue
            self.update(x, y)
        pass
    def verify(self, verify_data, verify_result):
        size = len(verify_data)
        failed_count = 0
        if size <= 0:
            pass
        for i in range(size):
            x = verify_data[i]
            y = verify_result.T[i]
            if self.loss(y, self.model(x)[1]) > 0:
                continue
            failed_count = failed_count + 1
        success_rate = (1.0 - (failed_count/size))*100
        print("Success Rate: ", success_rate, "%")
        print("Size: ", size, " failed_count: ", failed_count)

    def predict(self, predict_data):
        size = len(predict_data)
        result = []
        if size <= 0:
            pass
        for i in range(size):
            x = verify_data[i]
            y = verify_result.T[i]
            result.append(self.model(x)[0])
        return result

if __name__ == "__main__":
    # Make the training data and test data
    pos_data = [[3,3], [4,3], [1,1]]
    test_data = np.mat(pos_data)
    real_result = np.mat([1,1,-1])
    verify_data = np.mat([[3,3],[4,3],[5,2],[12,3],[1,2],[1,1]])
    verify_result = np.mat([1,1,-1,1,-1,-1])
    # First training
    perceptron = Simple_Perceptron(test_data, real_result)
    perceptron.train(1000)
    print("T1: w:", perceptron.w," b:", perceptron.b)
    perceptron.verify(verify_data, verify_result)
    # Second training for verify the model
    perceptron2 = Simple_Perceptron(verify_data, verify_result)
    perceptron2.train(1000)
    print("T2: w:", perceptron.w," b:", perceptron.b)
    perceptron2.verify(verify_data, verify_result)
    print(perceptron2.predict(verify_data))
