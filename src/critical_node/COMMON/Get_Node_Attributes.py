import networkx as nx


#获取目标的节点指定范围内的所有邻居
def GetNeighbor(Node, Depth,G):
    '''
    :param Node: target node ( Requirement: The target node is in network G )
    :param Depth: Order of the neighbor node
    :param G: Target network
    :return:
    '''
    nodeNei = {}
    layers = dict(nx.bfs_successors(G, source=Node, depth_limit=Depth))
    nodes = [Node]
    for i in range(1,Depth+1):
        nodeNei[i] = []
        for x in nodes:
            nodeNei[i].extend(layers.get(x,[]))
        nodes = nodeNei[i]
    return nodeNei


#获取每个节点的聚类系数
def NodeClustering(G):
    '''
    :param G: Graph in networkx
    :return: A dictionary of clustering coefficients for all nodes in the network
    '''
    return nx.clustering(G)
