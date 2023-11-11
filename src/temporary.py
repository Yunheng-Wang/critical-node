from critical_node.DATA.Get_Data import Get_Single_BuilInNetwork
from critical_node.COMMON.Read import ReadFolder
from critical_node.COMMON.Save import SaveToPyVar
from critical_node.DATA.Inlay import All_Data_Set

all_name = All_Data_Set()

for name in all_name:
    data = Get_Single_BuilInNetwork(name)
    SaveToPyVar(data, '/critical_node/DataSet/USER_NETWORK', name)
