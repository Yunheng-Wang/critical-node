

def SaveToTXT(Date_Dist,Save_Path,Name,n = 1):
    '''
    :param Date_Dist: The data set you want to save (input must: {node:value,......})
    :param Save_Path: Path save address
    :param Name: Save the name of the file
    :param n: n indicates the number of Spaces between data ,
              @Generally, n=8 is used to train the true value of sir
              @Save the model results with the default value n=1
    :return: File under the corresponding file
    '''
    file = open(Save_Path + '/' + Name + '.txt','w')
    dataChange = list(zip(Date_Dist.keys(),Date_Dist.values()))
    for i in range(len(dataChange)):
        file.write(str(dataChange[i][0]))
        file.write(' '*n)
        file.write(str(dataChange[i][1]))
        file.write('\n')

def SaveToPyVar( Python_Type_Data, Save_Path, Name ):
    with open(Save_Path + '/' + Name + '.py','w') as file:
        file.write(f'{Name} = {Python_Type_Data}\n')
    file.close()