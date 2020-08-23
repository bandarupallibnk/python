from bullet import bullet
from edate import cl_date
import sys
import os



def main(v_units,v_start,v_size):
    units = int(v_units)
    start = int(v_start)
    size = int(v_size)         
    rounds = 1000000
    maxbsize = units*8
    dt = cl_date()
    stoday = dt.fcurrentdate()
    fpath = '/Users/nandabandarupalli/Documents/python/seqdata/' + stoday + '.txt'
    try:
        os.remove(fpath)
    except:
        pass
    objseq = bullet(units,start,size,rounds,fpath)
    for i in range(1,rounds):
        vallist = objseq.gen_list()  # Generates the list
        #print(vallist) 
        blist = objseq.identify_1_12(vallist) # Identifies the if within range
        #print(blist)
        objseq.repeated(blist) # Identify number of times repeated
        #writedouble('Game' + str(i) ,blist)
        objseq.writeseq('Game' + str(i), blist)
        #writeodd('Game' + str(i), blist)
        print(i)
        #blist = identify_1_12(vallist)


if __name__=='__main__':
    main(v_units,v_start,v_size)
