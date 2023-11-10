from critical_node.MODEL.Basic_Model import K_shell
from critical_node.COMMON.Graph import MaxConnectSub
from critical_node.MODEL.Basic_Model import Degree
import networkx as nx



#获取网络中最大和最小的k-shell值
def GetMaxMinKs(G):
    '''
    :param G: Graph in networkx
    :return: Maximum and minimum k-shell values in the network
    '''
    K_shell_dict = K_shell(G)
    K_shell_Value_list = K_shell_dict.values()
    MaxKs = max(K_shell_Value_list)
    MinKs = min(K_shell_Value_list)
    return MaxKs, MinKs


#获取网络中的平均最短路径
def AverageShortestPath(G,Connect=True):
    '''
    :param G: Graph in networkx
    :param Connect: True - Calculate with maximum group ; Flase - Calculate with the original network
    :apply: Connect=True - There are disconnected or isolated nodes in the network
            Connect=Flase - The network is connected everywhere
    :return: The average minimum radius of the network
    '''
    if Connect == True:
        G = MaxConnectSub(G)
    Average_Shortest_Path_Length = nx.average_shortest_path_length(G)
    return Average_Shortest_Path_Length


#获取网络的节点个数
def NodeNumber(G):
    '''
    :param G: Graph in networkx
    :return: Number of network nodes
    '''
    nodeNumber = G.number_of_nodes()
    return nodeNumber


#获取网络的边个数
def EdgeNumber(G):
    '''
    :param G: Graph in networkx
    :return: Number of network edges
    '''
    edgeNumber = G.number_of_edges()
    return edgeNumber


#获取网络的1阶平均度
def AverageDegree(G):
    '''
    :param G: Graph in networkx
    :return: The average degree of the network
    '''
    nodeNumber = NodeNumber(G) #网络中点的个数
    nodeDegree = Degree(G) #网络中所有度的值
    #计算一阶
    one_degree = sum(nodeDegree.values())
    return one_degree/nodeNumber


#获取网络的最大度值
def MaxDegree(G):
    '''
    :param G:
    :return:
    '''
    return max(Degree(G).values())


#获取网络的临界感染阈值
def InfectionThreshold(G):
    '''
    :param G: Graph in networkx
    :return: The critical infection threshold of the network
    :formula: βc = λ<k>/<k^2> ( λ = 1.0 )
    :from: Identification of influential spreaders in complex networks
    :year: 2010
    :link: https://www.nature.com/articles/nphys1746/
    '''
    λ = 1.0
    nodeNumber = NodeNumber(G)
    nodeDegree = Degree(G)
    firstOrder = AverageDegree(G)
    secondOrder = sum(list( i*i for i in nodeDegree.values())) * λ / nodeNumber
    return firstOrder/secondOrder


#获取网络的直径
def Diameter(G):
    '''
    :param G: Graph in networkx
    :return:
    '''
    diameterValue = nx.diameter(G)
    return diameterValue


#获取网络的平均聚类系数
def AverageClustering(G):
    '''
    :param G: Graph in networkx
    :return:
    '''
    return nx.average_clustering(G)


#获取网络的传递性
def Transitivity(G):
    '''
    :param G: Graph in networkx
    :return: Transitive value of the network
    :explain: 图或网络的传递性。即图或网络中，认识同一个节点的两个节点也可能认识双方，计算公式为3*图中三角形的个数/三元组个数（该三元组个数是有公共顶点的边对数，这样就好数了）。
    :from : https://blog.csdn.net/ztf312/article/details/107711916#:~:text=nx.clustering%20%28G%29%20%23%20%E7%BD%91%E7%BB%9C%E8%8A%82%E7%82%B9%E7%9A%84%E8%81%9A%E7%B1%BB%E7%B3%BB%E6%95%B0%E3%80%82%20%E8%AE%A1%E7%AE%97%E5%85%AC%E5%BC%8F%E4%B8%BA%EF%BC%9A%E8%8A%82%E7%82%B9u%E7%9A%84%E4%B8%A4%E4%B8%AA%E9%82%BB%E5%B1%85%E8%8A%82%E7%82%B9%E9%97%B4%E7%9A%84%E8%BE%B9%E6%95%B0%E9%99%A4%E4%BB%A5%20%28%28d,%28u%29%20%28d%20%28u%29-1%29%2F2%29%E3%80%82%20nx.degree_centrality%20%28G%29%20%23%20%E8%8A%82%E7%82%B9%E5%BA%A6%E4%B8%AD%E5%BF%83%E7%B3%BB%E6%95%B0%E3%80%82
    '''
    return nx.transitivity(G)