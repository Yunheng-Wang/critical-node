

def Train_Sir(Read_Path,Save_Path,iter_time = 200 , range_begin = 0.01 , range_end = 0.5 , span = 0.01):
    '''
    :param Read_Path: You Want to Compute the Network Path (Don't in ending wih file suffix, such as '.txt','.py')
    :param Save_Path: The calculation result is saved to the local path (use folder and  Don't in ending with '/')
    :param iter_time: Count the number of iterations, the more the result is more accurate, the slower the calculation speed
                      @ Networks with less than 2000 nodes are usually set to 300
                      @ A network of 2000 to 8000 nodes is usually set to 200
                      @ A network with more than 8000 nodes is usually set to 100
    :param range_begin: The starting value of the infection range
    :param range_end: The end value of the infection range
    :param span: The spread of infection rate calculation range
    :return: Calculation result file saved to Save_Path address
    '''
    import copy
    from tqdm import tqdm
    from random import random
    from critical_node.COMMON.Get_Network_Attributes import NodeNumber
    from critical_node.COMMON.Save import SaveToTXT
    from critical_node.COMMON.Read import ReadFile_TXT
    from critical_node.COMMON.Graph import CreateGraph
    def infected_process( inf_nodes, G , B ):
        target_nei = []
        infected_temp = []
        for i in inf_nodes:
            target_nei.extend(G.neighbors(i))  # 获取感染点的邻居列表  将邻居节点内的每个节点都添加到target_nei列表中
            G.remove_node(i)  # 图中删除感染点
            for j in inf_nodes:
                if j in target_nei:
                    target_nei.remove(j)  # 将邻居中存在的已感染点删除（可能存在）
        for k in target_nei:
            if random() <= B:  # 随机生成一个[0,1)的数
                infected_temp.append(k)  # 满足感染条件，进行感染
        return set(infected_temp)  # 返回新感染源的集合（无相同点）

    def infected_range(inf_nodes, G, B):
        sum_inf_nodes = []
        sum_inf_nodes.extend(inf_nodes)  # 得到初始感染节点
        while bool(inf_nodes) == True:  # 依旧存在感染源
            inf_nodes = list(infected_process(inf_nodes, G, B ))
            sum_inf_nodes.extend(inf_nodes)  # j将新感染节点加入到感染节点列表中
        return len(sum_inf_nodes)

    def count_single_B(B, G, iter_time,Path,Name):
        node_list = sorted(list(G.nodes()))  # 节点列表
        node_num = NodeNumber(G)  # 获取节点数量
        Results = {}
        for i in node_list:
            result_temp = []  # 存储每次感染结果
            for j in range(iter_time):  # 循环计算次数
                G_new = copy.deepcopy(G)  # 拷贝网络
                result_temp.append(infected_range([i], G_new, B) / (node_num * 1.0))  # 添加每次感染范围
            Results[i] = sum(result_temp) / iter_time
        #保存文件数据
        SaveToTXT(Results,Path,Name,8)

    #====main====
    data = ReadFile_TXT(Read_Path)
    G = CreateGraph(data)
    if range_begin>0.7 or range_end>0.7 or span>0.7:
        print('The critical infection threshold must not be greater than 0.7')
        return
    else:
        Range_Of_Infection = [i/100 for i in range(int(range_begin*100),int(range_end*100)+1,int(span*100))]
        pbar = tqdm(Range_Of_Infection)
        for i in pbar:
            pbar.set_description('Progress β ： ' + str(i))
            #将输入的Read_Path字符串中的有效网络名称提取出来
            last_slash_index = Read_Path.rfind('/')
            Name = Read_Path[last_slash_index + 1:] + '_result_' + str('{:.5f}'.format(i))
            count_single_B(i,G,iter_time,Save_Path,Name)
