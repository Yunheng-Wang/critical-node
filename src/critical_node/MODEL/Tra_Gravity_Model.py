

#G(i)
def GC(G):
    '''
    :param G:
    :return: Dictionary of network node's G(i) values
    :from: Identifying influential spreaders in complex networks based on gravity formula
    :year: 2016
    :link: https://www.sciencedirect.com/science/article/abs/pii/S0378437116000959
    '''

    from critical_node.MODEL.Basic_Model import Degree
    from critical_node.COMMON.Get_Node_Attributes import GetNeighbor

    degreeValue=Degree(G)
    nodeValue={}
    for i in G.nodes():
        all_neigh=GetNeighbor(i, 3,G)
        res=[]
        for h in all_neigh:
            part=all_neigh[h]
            for t in part:
                res.append((degreeValue[t]*degreeValue[i])/(h**2))
        nodeValue[i]=sum(res)
    return nodeValue


#G+(i)
def GCJ(G):
    '''
    :param G:
    :return: Dictionary of network node's G+(i) values
    :from: Identifying influential spreaders in complex networks based on gravity formula
    :year: 2016
    :link: https://www.sciencedirect.com/science/article/abs/pii/S0378437116000959
    '''
    G_Data=GC(G)
    nodeValue={}
    for i in G.nodes():
        neig=list(G.neighbors(i))
        value=[]
        for n in neig:
            value.append(G_Data[n])
        nodeValue[i] = sum(value)
    return nodeValue

