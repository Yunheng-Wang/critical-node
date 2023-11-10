# **1. 内置数据集**

## **1.1 Network**

### **1.1.1 数据概述**

### **1.1.2 网络简介**

### **1.1.3 快速上手API**

## **1.2 SIR**

# **2. critical_node API**

## **2.1 DATA**

### **2.1.1 Inlay**
#### **2.1.1.1 All_Data_Set**
- 简介：该函数用于获取该库中所以内置数据集的名称
- 快速上手：<code>
% 快速获取库内的所有内置的网络名称
from src.critical_node.DATA.Inlay import All_Data_Set
AllData = All_Data_Set()
print(AllData)</code>

### **2.1.2 Get_Data**
#### **2.1.2.1 Get_Single_BuilInNetwork**
- 简介：获取某个网络的点边数据集合
- return: [[node1,node2],[node2,node3],......]
- 快速上手：<code>
% 快速获取as网络的数据列表
from src.critical_node.DATA.Get_Data import Get_Single_BuilInData
print(Get_Net_Data('as'))</code>
#### **2.1.2.2 Get_All_BuilInNetwork**
- 简介：获取内置数据库内的所有数据的字典
- return: {BuilInData:[[node1,node2],......],......}
- 快速上手：<code>
% 快速获取内置所有网络的数据字典
from src.critical_node.DATA.Get_Data import Get_All_BuilInData
print(Get_All_BuilInData())</code>

## **