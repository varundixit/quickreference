def instr(inString,searchPhrase,startPos,occurance):
    found = occurance
    pos = startPos
    while (1==1):

        pos=inString.find(searchPhrase,pos)
        #Nothing found
        if(pos==-1):
            return pos
     
        # The required occurrence found 
        if(found==1):
            break
             
        # Prepare to find another one occurrence
        found = found - 1;
        pos = pos + 1;         
    
    return pos

print('Printing 1st Occurance:',instr('abcdef.abcdef.abcdef','abcdef',0,1))
print('Printing 2nd Occurance:',instr('abcdef.abcdef.abcdef','abcdef',0,2))
print('Printing 3rd Occurance:',instr('abcdef.abcdef.abcdef','abcdef',0,3))
print('Printing 4th Occurance:',instr('abcdef.abcdef.abcdef','abcdef',0,4))
print('Printing pqrstu Occurance:',instr('abcdef.abcdef.abcdef','pqrstu',0,2))
