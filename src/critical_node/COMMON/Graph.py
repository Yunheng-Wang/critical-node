import networkx as nx


# 将一组连边数据快速转化为无向图
def CreateGraph( Date , Self_connected = False ):
    '''
    :param Date: A dataset of raw data
                 Form - [(Node number i , Node number j)......]
    :param Self_connected: False - Remove self-connected edges when creating a network ; True - No changes are made when the network is created
    :return: Abstract into the network node G
    '''
    G = nx.Graph()
    G.add_edges_from(Date)
    if Self_connected == False:
        G.remove_edges_from(nx.selfloop_edges(G))
    return G


#构建网络的最大连通子团
def MaxConnectSub( G ):
    '''
    :param G: Graph in networkx
    :return: The largest connected subgroup of a network G
    '''
    # 改动
    if len(G.nodes()) == 0:
        # Handle the case of an empty graph
        return G
    if not nx.is_connected(G):
        # Handle the case of a disconnected graph
        largest = max(nx.connected_components(G), key=len)
        G = G.subgraph(largest)
    return G

