def zaciatok(a,b):
    #Vlozim ku kazdej bázy císlo
    a_zaklad_cisla = []
    
    cislo_1 = 0

    cislo_3 = 0

    match = 1
    mismatch = -1
    gap = -2
    

    matica = []

    for i in range(len(a)):
        
        a_zaklad_cisla.append(cislo_1)

        cislo_1+=gap

    matica.append(a_zaklad_cisla)
    
    for i in range(1, len(b)):  #stĺpec
        cislo_3+=gap         
        
        novy_riadok = []
        
        novy_riadok.append(cislo_3)
        

        for j in range(1,len(a)):   #riadok
            
            values = []
            value_riadok= matica[i-1][j] 
            value_stlpec = novy_riadok[j-1]

            value_up = value_riadok + gap
            values.append(value_up)
            value_left = value_stlpec + gap
            values.append(value_left)

            if a[j] == b[i]:
                diagonal = matica[i-1][j-1] + match
                values.append(diagonal)
            else:
                diagonal = matica[i-1][j-1] + mismatch
                values.append(diagonal)

            novy_riadok.append(max(values))
        
        matica.append(novy_riadok)
    
    return matica, a, b
     

def trace_back(matica, a, b):

    final_sequence_a = []
    final_sequence_b = []

    i = len(a) -1
    j = len(b) -1
    

    while i>0 and j>0: 
        

        if a[i] == b[j]:
            final_sequence_a.append(a[i])
            final_sequence_b.append(b[j])
            i-=1
            j-=1

        else:
            values = {}
            values.update({"top" : matica[j-1][i]})
            values.update({"left" : matica[j][i-1]})
            values.update({"diagonal" : matica[j-1][i-1]})

            
            max_value = max(values.values())

            if max_value == values["top"]:
                final_sequence_a.append("-")
                final_sequence_b.append(b[j])
                j-=1   

            elif max_value == values["left"]:
                i-=1
                final_sequence_a.append(a[i])
                final_sequence_b.append("-")


            elif max_value == values["diagonal"]:
                i-=1
                j-=1
                final_sequence_a.append("-")
                final_sequence_b.append("-")
            
    print(final_sequence_a)      
    print(final_sequence_b)          


    #for i in range(len(final_sequence)):
        #print(final_sequence.pop(len(final_sequence)))           



    

matica, a ,b = zaciatok(" ATGCT"," AGCT")
trace_back(matica, a, b)
