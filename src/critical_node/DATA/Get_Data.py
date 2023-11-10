from critical_node.COMMON.Read import ReadFile_TXT,ReadFile_SIR,ReadFolder
from critical_node.DATA.Inlay import All_Data_Set
import os
from tqdm import tqdm

# ==================== Get BuiltIn Network Data ====================

# 输入一个NETWORK数据集内现有的数据名称，即可获取该名称在对应库内的绝对路径
def Get_Network_Path( BuiltIn_Network_Name ):
    '''
    :param BuiltIn_Network_Name: The name of the data present in the dataset
    :return: The absolute path of the name
    '''
    #当前脚本所在目录
    file_path = 'critical_node/DataSet/NETWORK/' + BuiltIn_Network_Name
    """
    current_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_path)
    parent_directory = os.path.dirname(current_directory)
    grandparent_directory = os.path.dirname(parent_directory)
    file_path = os.path.join(grandparent_directory, 'DataSet','NETWORK',BuiltIn_Network_Name)
    file_path = file_path.replace('\\', '/')
    """
    return file_path


#获取某个内置网络的数据信息
def Get_Single_BuilInNetwork( BuiltIn_Network_Name ):
    '''
    :param BuiltIn_Network_Name: The name of some built-in data
    :return: A collection of list data for BuiltIn Network names ---- [[node1,node2],[node2,node3],......]
    '''
    All_Network = All_Data_Set()
    if BuiltIn_Network_Name in All_Network:
        Single_BuilInNetwork = Get_Network_Path(BuiltIn_Network_Name)
    else:
        print("\033[31m Sorry, {} network is not in the built-in dataset, please check your input and try again Help me. Built-in data sets include : {}\033[0m".format(BuiltIn_Network_Name,[
                                        'as','as19971108','bio-yeast-protein-inter','c_elegans','ca_astroph',
                                        'ca_condmat','ca_hepph','ca_hepth','ca_qrqc','can2015',
                                        'dolphins','e_mail','email_enron','euroroad','facebook',
                                        'fb-pages-foods','foodweb-baydry','foodweb-baywet','hamster','jazz',
                                        'karate_club','loc_bright','netsci','oregon1_010331','p2p-Gnutella06',
                                        'p2p-Gnutella08','p2p-Gnutella09','pgp','power_grid','soc-wiki-Votes','terrorist','us_air']))
    return ReadFile_TXT(Single_BuilInNetwork)


# 获取内置数据库内的所有数据集合
def Get_All_BuilInNetwork():
    '''
    :return: Dictionary of all built-in network data sets ---- {BuilInData:[[node1,node2],......],......}
    '''
    All_BuilInData = {}
    All_Network = All_Data_Set()
    pbar = tqdm(All_Network)
    for signal in pbar:
        pbar.set_description('Network ：' + str(signal))
        All_BuilInData[signal] = Get_Single_BuilInNetwork(signal)
    return All_BuilInData


# ==================================================================


# ==================== Get BuiltIn Network Data ====================

# 输入一个SIR数据集内现有的数据名称，即可获取该名称在对应库内的绝对路径
def Get_SIR_Path( BuiltIn_Network_Name ):
    '''
    :param BuiltIn_Network_Name: The name of the data present in the dataset
    :return: The absolute path of the name
    '''
    file_path = '../DataSet/SIR/' + BuiltIn_Network_Name
    '''
    #当前脚本所在目录
    current_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_path)
    parent_directory = os.path.dirname(current_directory)
    grandparent_directory = os.path.dirname(parent_directory)
    file_path = os.path.join(grandparent_directory, 'DataSet','SIR',BuiltIn_Network_Name)
    file_path = file_path.replace('\\', '/')
    '''
    return file_path


# 读取某个网络的所有SIR内置文件
def Get_Single_BuilInSIR( BuiltIn_Network_Name  ):
    '''
    :param BuiltIn_Network_Name:
    :return:
    '''
    Single_BuilInSIR = {}
    All_Network = All_Data_Set()

    if BuiltIn_Network_Name in All_Network:
        BuilInSIR_Folder = ReadFolder(Get_SIR_Path(BuiltIn_Network_Name),type='.txt')
    else:
        print("\033[31m Sorry, {} network is not in the built-in dataset, please check your input and try again Help me. Built-in data sets include : {}\033[0m".format(BuiltIn_Network_Name,[
                                        'as','as19971108','bio-yeast-protein-inter','c_elegans','ca_astroph',
                                        'ca_condmat','ca_hepph','ca_hepth','ca_qrqc','can2015',
                                        'dolphins','e_mail','email_enron','euroroad','facebook',
                                        'fb-pages-foods','foodweb-baydry','foodweb-baywet','hamster','jazz',
                                        'karate_club','loc_bright','netsci','oregon1_010331','p2p-Gnutella06',
                                        'p2p-Gnutella08','p2p-Gnutella09','pgp','power_grid','soc-wiki-Votes','terrorist','us_air']))
        return

    for signgle in BuilInSIR_Folder:
        Signgle_Path = Get_SIR_Path( BuiltIn_Network_Name ) + '/' + signgle[:-4]
        Single_BuilInSIR[float(signgle[-11:-4])] = ReadFile_SIR( Signgle_Path )
    return Single_BuilInSIR


# ==================================================================

if __name__=='__main__':
    print(Get_Single_BuilInSIR('as'))