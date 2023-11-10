import matplotlib.pyplot as plt


def Rough_Draft( X_Data, Y_Data ):
    '''
    :param X_Data: IS List
    :param Y_Data: IS DICT {y1:[value1,value2 ... ]}
    :return:
    '''
    assert isinstance(Y_Data, dict) , 'The input data y must be in the form of a dictionary.'
    assert all(len(val_list) == len(X_Data) for val_list in Y_Data.values()) , 'The number of input elements must be the same.'
    plt.figure(dpi=100)
    for Sign_Y_Data in Y_Data:
        plt.plot(X_Data,Y_Data[Sign_Y_Data],label = Sign_Y_Data)
    plt.legend( loc='best')
    plt.show()

if __name__ == '__main__':
    Rough_Draft([1,2,3],{'1':[1,2,3],'2':[2,4,6]})