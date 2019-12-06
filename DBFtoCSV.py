from simpledbf import Dbf5

dbf = Dbf5('/Users/katherinenewcomb/Desktop/TestingRepo/gadm36_PHL_shp/gadm36_PHL_2.dbf', codec='utf-8')
print(dbf.fields)

# dbf = Dbf5('/Users/katherinenewcomb/Desktop/TestingRepo/gadm36_PHL_shp/gadm36_PHL_0.dbf')
dbf.to_csv('/Users/katherinenewcomb/Desktop/Philippines/Gadm36_PHL_2.csv')
