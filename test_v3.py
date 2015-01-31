
myDictionary = { #"Link" : [] ,
	         "BadCounter" : [] , 
		 "Bad Data" : [] ,
                 "Rollover Count" : [] , 
                 "Bad data rate" : [] ,
                 "GTX Reset Cnt" : [] ,
                 "DTC exist" : [] ,
                 "OrbAlign exist" : [] ,
                 "Alignment Done" : [] ,
                 "Reset Done" : [] ,
                 "PLL Lock" : [] ,
                 "Byte Aligned" : [] ,
                 "Align occ" : [] ,
                 "Align delta" : [] ,
                 "OrbitRate(kHz)" : [] ,
                 "Bad align" : [] }

myFile = open("log.txt","r")

for line in myFile :
    
    for i in myDictionary : 
        
	indexI = line.find(i)
        if( indexI != -1 ):
            line = line[indexI+len(i):-1]
            #print line, i
            #print indexI
            elements = line.split(" ")
            while '' in elements :
                elements.remove('')
#            print elements
            for e in elements :
                myDictionary[i].append(e)
            
for keys,values in myDictionary.items():
    print(keys)
    print(values)

