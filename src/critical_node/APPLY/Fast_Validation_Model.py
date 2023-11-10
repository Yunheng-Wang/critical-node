from critical_node.EXPERIMENTAL.Accuracy import Kendall_Tau
from critical_node.DATA.Get_Data import Get_Single_BuilInNetwork,Get_Single_BuilInSIR
from critical_node.COMMON.Graph import CreateGraph
from critical_node.DRAW.Brief import Rough_Draft
from tqdm import tqdm

class FVM():
    '''

    '''
    def __init__( self  ,Network  ):
        '''

        '''
        # Count network's Graph
        self.G = CreateGraph(Get_Single_BuilInNetwork( Network ))
        # Count your model
        # self.Model_Result = Verify_Model(self.G)

        # The SIR Corresponding to the network is found {β：{node:value ...} ... }
        self.SIR_Result = dict(sorted(Get_Single_BuilInSIR(Network).items(), key=lambda item: item[0]))


    def __call__( self , *args ):
        # save the model you want to compare {model_name：{node:value ...} ... }
        Other_Result = {}
        for Compare_Model in args:
            Other_Result[Compare_Model.__name__] = Compare_Model(self.G)
        # Result of Kendall_Tau
        Kendall_Result = {}
        for Compare_Sign in Other_Result:
            mid_data_y = []
            for SIR_Sign in self.SIR_Result:
                mid_data_y.append(Kendall_Tau(Other_Result[Compare_Sign],self.SIR_Result[SIR_Sign]))
            Kendall_Result[Compare_Sign] = mid_data_y
        # draw picture
        Rough_Draft(list(self.SIR_Result.keys()),Kendall_Result)
