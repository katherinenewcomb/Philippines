from master import *

connect_csv_files('PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv.CSV','province','#adm2+name',
r'/Users/katherinenewcomb/Desktop/Philippines/housingv2.csv','mun_code',
r'/Users/katherinenewcomb/Desktop/TestingRepo/Philippines/ConnectFiles/editedCSV.csv',
r'/Users/katherinenewcomb/Desktop/TestingRepo/Philippines/ConnectFiles/Gadm36_PHL_2.csv','CC_2',
r'/Users/katherinenewcomb/Desktop/TestingRepo/Philippines/ConnectFiles/Mergev1.csv')
