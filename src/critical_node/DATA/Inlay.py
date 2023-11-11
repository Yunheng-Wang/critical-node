
# 包内现有的所有数据集名称
def All_Data_Set():
    '''
    :return: The collection of names of all data sets built into critical_node
    '''
    Existing_built_in_data_sets = [
                                        'as','as19971108','bio-yeast-protein-inter','beijing_road','c_elegans','ca_astroph',
                                        'ca_condmat','ca_hepph','ca_hepth','ca_qrqc','can2015',
                                        'dolphins','e_mail','email_enron','euroroad','facebook',
                                        'fb-pages-foods','foodweb-baydry','foodweb-baywet','hamster','jazz',
                                        'karate_club','loc_bright','netsci','oregon1_010331','p2p-Gnutella06',
                                        'p2p-Gnutella08','p2p-Gnutella09','pgp','power_grid','soc-wiki-Votes','terrorist','us_air'
                                   ]
    return Existing_built_in_data_sets

if __name__ == '__main__':
    print(len(All_Data_Set()))