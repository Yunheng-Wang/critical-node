

# 计算网络的CCDF值
def CCDF(Model_result):
    '''
    :param Model_result: Model_result: The result of model calculation ( input form : {node:influence,......})
    :return: The CCDF value of the model results calculated in the specified network ( output : [value1,value2,......])
    '''

    rank_inf = sorted(Model_result.values())  # 找到节点影响力 并排序
    rank_num = len(rank_inf ) *1.0
    # print rank_num
    rank_del_multi = list(Model_result.keys())  # 去掉重复的节点
    rank_dict = {}
    for i in rank_inf:
        k = 0
        for j in rank_del_multi:
            if i == Model_result[j]:
                k += 1
        rank_dict[i] = k
    rank_pdf = []
    influe_list = sorted(rank_dict.keys(), reverse=True)  # 从小到大进行排序
    for n in influe_list:
        rank_pdf.append(rank_dict[n ] /rank_num)
    rank_ccdf = [] # 互补分布概率值
    for m in range(len(rank_pdf)):
        rank_ccdf.append(sum(rank_pdf[ m +1:]))
    if len(rank_ccdf) < len(Model_result):
        num_zero = len(Model_result ) -len(rank_ccdf) # 需要补0的个数
        for f in range(num_zero):
            rank_ccdf.append(0)
    return rank_ccdf

def Monotonic_Value(Model_result):
    '''
    :param Model_result: Model_result: The result of model calculation ( input form : {node:influence,......})
    :return: The monotone value of the result calculated by the model under the specified network
    '''

    node_inf = sorted(Model_result.values())  # 找到节点影响力 并排序
    node_num = len(node_inf)
    node_del_multi = list(set(node_inf))  # 去掉重复的节点
    node_dict = {}
    for i in node_del_multi:
        k = 0
        for j in node_inf:
            if i == j:
                k += 1
                node_dict[j] = k
    n_r = 0
    for n in node_dict.values():
        if n > 1:
            n_r += n * (n - 1)
    M = (1 - (n_r * 1.0) / (node_num * (node_num - 1))) ** 2
    return M