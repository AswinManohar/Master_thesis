from psrqpy import QueryATNF
import sys

sys.argv[0]
sys.argv[1]


c=['A','B',0.233333]

query = QueryATNF(params=['JNAME', 'RAJ', 'DECJ'], circular_boundary=c)
print(query.table)



