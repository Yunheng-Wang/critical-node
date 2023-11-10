from src.critical_node.APPLY.Fast_Validation_Model import FVM
from src.critical_node.MODEL.Basic_Model import K_shell,Degree,H_index
from src.critical_node.MODEL.Ks_Gravity_Model import KSGC

count = FVM(K_shell,'as')
count(Degree,H_index,K_shell,KSGC)

