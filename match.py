import numpy as np
import random

import matplotlib.pyplot as plt


class ann():
    def __init__(self):

        ###创建激活函数
        self.active = {
            "sigmoid": lambda x: 1 / (1 + np.exp(-x)),
            "tanh": lambda x: np.tanh(x),
            "relu": lambda x: np.where(x > 0, x, 0),
            "leakyrelu": lambda x, leaky=0.02: np.where(x > 0, x, leaky * x),
            "elu": lambda x, eluvalue=0.02: np.where(x > 0, x, eluvalue * (np.exp(x) - 1)),
            "softplus": lambda x: np.log(1 + np.exp(x)),
            "none": lambda x: x
        }

        ###创建损失函数
        self.loss = {
            "mse": lambda inp, out: np.sum((inp - out) ** 2) / len(out),
            "mae": lambda inp, out: np.sum(np.absolute(inp - out)) / len(out),
            # "cross_entropy_error":lambda inp,out:np.sum((out/(inp)-(1-out)/(1-inp)))/len(out)
            # "cross_entropy_error":lambda inp,out:-np.sum(out*np.log(inp)+(1-out)*np.log(1-inp))/len(out)
            "cross_entropy_error": lambda inp, out: -np.sum(np.where(out == 1, np.log(inp), np.log(1 - inp))) / len(out)
        }

        ###创建激活函数的导数
        self.deri = {
            "sigmoid": lambda x: 1 / (1 + np.exp(-x)) * (1 - 1 / (1 + np.exp(-x))),
            "tanh": lambda x: 1 - np.tanh(x),
            "relu": lambda x: np.where(x > 0, 1, 0),
            "leakyrelu": lambda x, leaky=0.02: np.where(x > 0, 1, leaky),
            "elu": lambda x, eluvalue=0.02: np.where(x > 0, 1, eluvalue * np.exp(x)),
            "softplus": lambda x: 1 - 1 / (1 + np.exp(x)),
            "none": lambda x: 1
        }

        ###创建损失函数的导数
        self.deriloss = {
            "mse": lambda inp, out: 2 * (inp - out) / len(out),
            "mae": lambda inp, out: np.where(inp > out, 1, -1) / len(out),
            "cross_entropy_error": lambda inp, out: -np.sum(
                out * np.log(inp + 1e-7) + (1 - out) * np.log(1 - inp + 1e-7)) / len(out)
        }

        # 初始化数据
        self.grad = []
        self.bias = []

    def dot(self, inp, w, b=0, activemod="none"):
        data = []
        for j in w:
            data.append(np.sum(inp * j) + b)
        data = np.array(data)
        data = self.active[activemod](data)
        return np.array(data)

    def initial(self, stru):
        self.grad = []
        self.bias = []
        for i in range(len(stru) - 1):
            self.grad.append(np.random.randn(stru[i + 1], stru[i]))
            self.bias.append(random.random())

    def renew(self, wg, bg, size, learnrate, mod="SGD"):
        if mod == "SGD":
            for i in range(len(wg)):
                self.grad[i] = self.grad[i] - learnrate * wg[i] / size
                self.bias[i] = self.bias[i] - learnrate * bg[i] / size

    def train(self, inp, expe, stru, activemod, epoch, batchsize, lossmod, learnrate, gradmod):
        loss = 0
        wgrad = []
        bgrad = []
        lossdata = []
        for i in range(epoch):
            index = np.random.choice(np.array(range(len(expe))), len(expe), replace=False)
            for k in range(len(index)):
                layer = []
                layer.append(np.array(inp[index[k]]))
                for j in range(len(stru) - 1):
                    layer.append(self.dot(layer[j], self.grad[j], self.bias[j], activemod[j]))

                loss = loss + self.loss[lossmod](layer[-1], expe[index[k]])
                layerback = []
                layerback.append(
                    self.deri[activemod[-1]](self.deriloss[lossmod](layer[-1], expe[index[k]])) * self.deriloss[
                        lossmod](layer[-1], expe[index[k]]))
                for j in range(len(activemod) - 1):
                    layerback.insert(0, self.deri[activemod[-2 - j]](
                        self.dot(layerback[-1 - j], self.grad[-1 - j].T)) * self.dot(layerback[-1 - j],
                                                                                     self.grad[-1 - j].T))
                if len(wgrad) == 0:
                    for arr in range(len(layerback)):
                        wgrad.append(np.outer(layerback[arr], layer[arr]))
                    for arr in range(len(layerback)):
                        bgrad.append(np.sum(layerback[arr]))
                else:
                    for arr in range(len(wgrad)):
                        wgrad[arr] = wgrad[arr] + np.outer(layerback[arr], layer[arr])
                    for arr in range(len(bgrad)):
                        bgrad[arr] = bgrad[arr] + np.sum(layerback[arr])
                if (k + 1) % batchsize == 0:
                    lossvalue = loss / batchsize
                    lossdata.append(lossvalue)
                    print(lossvalue)
                    self.renew(wgrad, bgrad, batchsize, learnrate, gradmod)
                    yield lossvalue
                    loss = 0
                    wgrad = []
                    bgrad = []
                elif k + 1 == len(index):
                    lossvalue = loss / (len(index) % batchsize)
                    print(lossvalue)
                    lossdata.append(lossvalue)
                    self.renew(wgrad, bgrad, len(index) % batchsize, learnrate, gradmod)
                    yield lossvalue
                    loss = 0
                    wgrad = []
                    bgrad = []
        # plt.plot(np.linspace(0,epoch,epoch),lossdata)
        # plt.show()


if __name__ == '__main__':
    model = ann()
    model.initial([3, 2, 2])
    gen = model.train(inp=np.array([[1, 2, 3], [4, 5, 6], [2, 3, 4]]),
                      expe=np.array([[1, 0], [0, 1], [0.5, 0.5]]),
                      stru=[3, 2, 2],
                      activemod=["tanh", "sigmoid"],
                      epoch=51,
                      batchsize=3,
                      lossmod="mse",
                      learnrate=0.5,
                      gradmod="SGD")
    for i in gen:
        pass
