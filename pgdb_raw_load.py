import psycopg2
import sys
from edate import cl_date

optype = sys.argv[1]
targettblname = sys.argv[2]
fpathdict = {"double":"/Users/nandabandarupalli/Documents/python/doubledata/","seq":"/Users/nandabandarupalli/Documents/python/seqdata/","odd":"/Users/nandabandarupalli/Documents/python/seqodd/"}

print(optype)
print(targettblname)

v_host = "localhost"
v_database = "postgres"
v_user = "nbandarupa"
v_password = "nbandarupa"

dt = cl_date()
print(dt)
filedate = dt.fcurrentdate()
conn = psycopg2.connect(host=v_host,database=v_database,user=v_user,password=v_password)
cur = conn.cursor()
fload = open(fpathdict[optype] + filedate + '.txt','r')
truncsql = "truncate table staging.{}".format(targettblname)
print(truncsql)
cur.execute(truncsql)
for line in fload:
	lst = line.split('\t')
	#print(f"{lst[0]}")
	insertsql = "insert into staging.{} values ('{}',{},{},{},{},{}) ".format(targettblname,lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
	#print (insertsql)
	cur.execute(insertsql)
#db_version = cur.fetchone()
#print(db_version)
conn.commit()
cur.close()
conn.close()
fload.close()