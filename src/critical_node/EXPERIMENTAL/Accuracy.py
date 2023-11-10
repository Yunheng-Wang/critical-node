from math import ceil
from scipy.stats import kendalltau


#计算模型结果与sir真实的kendalltau值
def Kendall_Tau(Model_result,Sir_result,Places = 3):
    '''
    :param Model_result: The result of model calculation ( input form : {node:influence,......})
    :param Sir_result: The result of the sir Calculation ( input form : {node:influence,......})
    :param Places: Keep the number of decimal places
    :return: kendall calculation results of model and sir Real value
    '''

    Model_result = [i[1] for i in sorted(Model_result.items(),key=lambda x:x[0],reverse=False)]
    # print(Model_result)
    Sir_result = [i[1] for i in sorted(Sir_result.items(),key=lambda x:x[0],reverse=False)]
    kendallta,p= kendalltau(Model_result,Sir_result)
    kendallta=round(kendallta,Places)
    return kendallta


#计算模型结果与sir真实值的不精确函数值
def Impresion_Function(Model_result,Sir_result,n=100):
    '''
    :param Model_result: Model_result: The result of model calculation ( input form : {node:influence,......})
    :param Sir_result: Sir_result: The result of the sir Calculation ( input form : {node:influence,......})
    :param n: The ratio of compute nodes, typically 100, does not need to be more precise or rough
    :return: Results of n imprecise function values at different proportions (output : [value1,value2,......])
    '''

    impro_result = []
    for k in range(1, n):
        infected_result_sort = sorted(Sir_result.items(), key=lambda e: e[1], reverse=True)
        method_result_sort = sorted(Model_result.items(), key=lambda e: e[1], reverse=True)
        count_p = ceil(len(Model_result)*k*1.0/n)  # 计算节点的比例
        sum_method = 0
        sum_inf = 0
        for i in range(int(count_p)):
            sum_method += Sir_result[method_result_sort[i][0]]
            sum_inf += infected_result_sort[i][1]
        impro_result.append(1 - sum_method/sum_inf)
    return impro_result


#计算模型结果与sir真实值的Jaccard的值
def Jaccard(Model_result,Sir_result,n = 200 , span = 5):
    '''
    :param Model_result: Model_result: The result of model calculation ( input form : {node:influence,......})
    :param Sir_result: Sir_result: The result of the sir Calculation ( input form : {node:influence,......})
    :param n: Range of the top n nodes ( Note: The value of n must be less than or equal to the value of the network node, otherwise it is invalid )
    :param span: Represents the span of the node. The larger the span, the smaller n, and the less value is returned
    :return: Results of n/span Jaccard values at different proportions (output : [value1,value2,......])
    :from: A Novel Method to Rank Influential Nodes in Complex Networks Based on Tsallis Entropy
           Fuzzy System Based Medical Image Processing for Brain Disease Prediction
           An extended improved global structure model for influential node identification in complex networks
    '''

    a=[i for i in range(span,n,span)]
    Model_result = sorted(Model_result.items(), key=lambda e: e[1], reverse=True)
    Sir_result = sorted(Sir_result.items(), key=lambda e: e[1], reverse=True)
    all=[]
    for get in a:
        data_sir = [ i[0] for i in Sir_result[:get]]
        data_model = [ i[0] for i in Model_result[:get]]
        result=len(set(data_sir).intersection(set(data_model))) / len(set(data_sir).union(set(data_model)))
        all.append(result)
    return all