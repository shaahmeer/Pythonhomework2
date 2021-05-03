def  the_sequence( n ):
    seq = [ 0 ]
    while len( seq ) < n:
        rev_seq = seq[ : : -1 ]
        new_number = 0
        for i in range( len( seq ) ):
            new_number += ( seq[i] == rev_seq[i] )
        seq.append( new_number )          
    return seq
    
print(the_sequence(16))