import numpy as np
import cPickle
import gzip
import matplotlib.pyplot as plt
if __name__ == '__main__':
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    plt.figure(figsize=(5,5))
    for i in range(5 * 5):
        plt.subplot(5, 5, i + 1)
        plt.imshow(np.round(train_set[0][i].reshape(28,28)), cmap=plt.cm.gray)
        plt.xticks(())
        plt.yticks(())
    plt.show()