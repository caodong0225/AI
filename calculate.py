import numpy as np
import random


class Ann:
    def __init__(self):

        # 创建激活函数
        # 此处罗列了一些最常用的激活函数，如果需要其他激活函数，可以自行添加
        self.active = {
            "sigmoid": lambda x: 1 / (1 + np.exp(-x)),
            "tanh": lambda x: np.tanh(x),
            "relu": lambda x: np.where(x > 0, x, 0),
            "leakyrelu": lambda x, leaky=0.02: np.where(x > 0, x, leaky * x),
            "elu": lambda x, elu_value=0.02: np.where(x > 0, x, elu_value * (np.exp(x) - 1)),
            "softplus": lambda x: np.log(1 + np.exp(x)),
            "none": lambda x: x
        }

        # 创建损失函数
        # 此处罗列了一些最常用的损失函数，如果需要其他损失函数，可以自行添加
        self.loss = {
            "mse": lambda inp, out: np.sum((inp - out) ** 2) / len(out),
            "mae": lambda inp, out: np.sum(np.absolute(inp - out)) / len(out),
            "cross_entropy_error": lambda inp, out: -np.sum(np.where(out == 1, np.log(inp), np.log(1 - inp))) / len(out)
        }

        # 创建激活函数的导数
        self.derivative = {
            "sigmoid": lambda x: 1 / (1 + np.exp(-x)) * (1 - 1 / (1 + np.exp(-x))),
            "tanh": lambda x: 1 - np.tanh(x),
            "relu": lambda x: np.where(x > 0, 1, 0),
            "leakyrelu": lambda x, leaky=0.02: np.where(x > 0, 1, leaky),
            "elu": lambda x, elu_value=0.02: np.where(x > 0, 1, elu_value * np.exp(x)),
            "softplus": lambda x: 1 - 1 / (1 + np.exp(x)),
            "none": lambda x: 1
        }

        # 创建损失函数的导数
        self.derivative_loss = {
            "mse": lambda inp, out: 2 * (inp - out) / len(out),
            "mae": lambda inp, out: np.where(inp > out, 1, -1) / len(out),
            "cross_entropy_error": lambda inp, out: -np.sum(
                out * np.log(inp + 1e-7) + (1 - out) * np.log(1 - inp + 1e-7)) / len(out)
        }

        # 初始化数据
        self.grad = []
        self.bias = []

    def dot(self, inp, w, b=0, active_mod="none"):
        # 该函数用于计算输入数据与权重的点积，并且加上偏置，最后通过激活函数
        data = []
        for _ in w:
            data.append(np.sum(inp * _) + b)
        data = np.array(data)
        data = self.active[active_mod](data)
        return np.array(data)

    def initial(self, structure):
        # 初始化权重和偏置，默认为0~1之间的随机数
        self.grad = []
        self.bias = []
        for _ in range(len(structure) - 1):
            self.grad.append(np.random.randn(structure[_ + 1], structure[_]))
            self.bias.append(random.random())

    def renew(self, wg, bg, size, learning_rate, mod="SGD"):
        # 更新权重和偏置，通过梯度下降法
        if mod == "SGD":
            for _ in range(len(wg)):
                self.grad[_] = self.grad[_] - learning_rate * wg[_] / size
                self.bias[_] = self.bias[_] - learning_rate * bg[_] / size

    def train(self, inp, expe, stru, activemod, epoch, batchsize, lossmod, learnrate, gradmod):
        loss = 0
        sample_size = len(expe)  # 获取样本数量
        wgrad = []
        bgrad = []
        lossdata = []
        for i in range(epoch):  # 迭代次数
            index = np.random.choice(np.array(range(sample_size)), sample_size, replace=False)  # 随机打乱数据，获取打乱后的索引
            for k in range(sample_size):
                layer = []
                layer.append(np.array(inp[index[k]]))
                for j in range(len(stru) - 1):
                    layer.append(self.dot(layer[j], self.grad[j], self.bias[j], activemod[j]))

                loss += self.loss[lossmod](layer[-1], expe[index[k]])
                layerback = []
                layerback.append(
                    self.derivative[activemod[-1]](self.derivative_loss[lossmod](layer[-1], expe[index[k]])) *
                    self.derivative_loss[
                        lossmod](layer[-1], expe[index[k]]))
                for j in range(len(activemod) - 1):
                    layerback.insert(0, self.derivative[activemod[-2 - j]](
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
                    self.renew(wgrad, bgrad, batchsize, learnrate, gradmod)
                    wgrad = []
                    bgrad = []
                elif k + 1 == len(index):
                    self.renew(wgrad, bgrad, len(index) % batchsize, learnrate, gradmod)
                    wgrad = []
                    bgrad = []
            loss_value = loss / sample_size
            lossdata.append(loss_value)
            yield loss_value
            loss = 0
        # plt.plot(np.linspace(0,epoch,epoch),lossdata)
        # plt.show()


if __name__ == '__main__':
    model = Ann()
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
