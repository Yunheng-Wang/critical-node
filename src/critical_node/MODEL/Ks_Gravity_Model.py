

def KSGC(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's KSGC values
    :from: An improved gravity model to identify influential nodes in complex networks based on k-shell method
    :year: 2021
    :link: https://www.sciencedirect.com/science/article/pii/S0950705121004603
    '''

    import math
    import networkx as nx
    from tqdm import tqdm
    from critical_node.COMMON.Get_Node_Attributes import GetNeighbor
    from critical_node.COMMON.Get_Network_Attributes import AverageShortestPath
    from critical_node.COMMON.Get_Network_Attributes import GetMaxMinKs
    from critical_node.MODEL.Basic_Model import K_shell,Degree

    AllKsData = K_shell(G)
    AllDgreeData = Degree(G)
    MaxKs,MinKs = GetMaxMinKs(G)

    def Count_C(tar_node, nei_node):
        '''
        :param tar_node: The target node to be computed
        :param nei_node: The corresponding neighbor node
        :return: C value of the target node and the corresponding neighbor node
        '''
        C = pow(math.e,(AllKsData[tar_node] - AllKsData[nei_node]) / (MaxKs - MinKs))
        return C

    def Count_F(tar_node, nei_node):
        '''
        :param tar_node: The target node to be computed
        :param nei_node: The corresponding neighbor node
        :return: F value of the target node and the corresponding neighbor node
        '''
        C = Count_C(tar_node, nei_node)
        F = (C * AllDgreeData[tar_node] * AllDgreeData[nei_node]) / (pow(nx.shortest_path_length(G, tar_node, nei_node), 2))
        return F

    def network_R(G):
        '''
        :param G: Graph in networkx
        :return: 1/2 times the average shortest path of the network
        '''
        D = AverageShortestPath(G)
        R = D / 2
        R = math.floor(R)
        return R

    #==main==
    R = network_R(G)
    nodeValue = {}
    for i in G.nodes():
        AllNei = GetNeighbor(i,R,G)
        sin_result = 0
        for j in AllNei:
            for k in AllNei[j]:
                sin_result += Count_F(i,k)
        nodeValue[i] = sin_result
    return nodeValue


