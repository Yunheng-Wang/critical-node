import networkx as nx


#degree
def Degree(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's degree values
    :from:
    :year:
    :link:
    '''
    nodeValue = dict(G.degree())
    return nodeValue


#k-shell
def K_shell(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's k-shell values
    :from:
    :year:
    :link:
    '''
    Graph = G.copy() #复制一个节点图
    nodeValue = []
    Degrees = (Graph.degree[n] for n in Graph.nodes())
    k = min(Degrees)
    while nx.number_of_nodes(Graph):
        nodeDegree = {n: Graph.degree[n] for n in Graph.nodes()}
        kMin = min(nodeDegree.values())
        flag = True
        while (flag):
            nodeDegree = {n: Graph.degree[n] for n in Graph.nodes()}
            for Key,Va in nodeDegree.items():
                if (Va == kMin):
                    nodeValue.append((Key,k))
                    Graph.remove_node(Key)
            nodeDegreeCheck = {n: Graph.degree[n] for n in Graph.nodes()}
            # 检查图中是否存在度为kmin的节点
            if kMin not in nodeDegreeCheck.values():
                flag = False
        k += 1
    nodeValue=dict(nodeValue)
    return nodeValue


#h-index
def H_index(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's h-index values
    :from:
    :year:
    :link:
    '''
    nodeValue = {}
    H = 0
    for u in G.nodes():
        ns = {n: G.degree[n] for n in G[u]}
        sns = sorted(zip(ns.keys(), ns.values()), key=lambda x: x[1], reverse=True)
        for i, n in enumerate(sns):
            if i >= n[1]:
                H = i
                break
            H = i + 1
        nodeValue[u] = H
    return nodeValue


#betweenness
def Betweenness(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's betweeness values
    :from: A Set of Measures of Centrality Based on Betweenness
    :year: 1977
    :link: https://psycnet.apa.org/record/1977-28688-001
    '''
    nodeValue=nx.betweenness_centrality(G)
    #print(nodeValue)
    return nodeValue


#pagerank
def Pagerank(G):
    '''
    :param G: Graph in networkx
    :return: Dictionary of network node's pagerank values
    :from:
    :year:
    :link:
    '''
    nodeValue = nx.pagerank(G)
    return nodeValue
