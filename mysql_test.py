import mysql_crud as my

my.connect()
data_to_insert = (6, 'สมเจตน์', 26,'male')
my.insert(data_to_insert)
#my.updateTable(5,10)
#my.deleteData(10)
my.selectAll()
my.close()
