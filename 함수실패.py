#마피아 뽑기
def choosemafia1(rcode):
    userjobrandomlist = []
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = tl + 1      
    for i in range(1, tl):
        data = linecache.getline(user_list, i).strip()
        userjobrandomlist.append(data)
    return userjobrandomlist

def choosemafia2(rcode):
    userjob = choosemafia1(rcode)
    choiceList = random.choice(userjob)
    
    return choiceList

def choosemafia3(rcode, userjob):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         

    with open(user_list, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = ''
        for line in f:
            if(line.startswith(userjob)):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()    
    return     

#경찰뽑기
def choosepolice1(rcode):
    userjobrandomlist = []
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = tl + 1      
    for i in range(1, tl):
        data = linecache.getline(user_list, i).strip()
        userjobrandomlist.append(data)
    return userjobrandomlist

def choosepolice2(rcode):
    userjob = choosepolice1(rcode)
    choiceList = random.choice(userjob)
    
    return choiceList

def choosepolice3(rcode, userjob):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         

    with open(user_list, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = ''
        for line in f:
            if(line.startswith(userjob)):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         
    return

#의사뽑기
def choosedoctor1(rcode):
    userjobrandomlist = []
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = tl + 1      
    for i in range(1, tl):
        data = linecache.getline(user_list, i).strip()
        userjobrandomlist.append(data)
    return userjobrandomlist

def choosedoctor2(rcode):
    userjob = choosepolice1(rcode)
    choiceList = random.choice(userjob)
    
    return choiceList

def choosedoctor3(rcode, userjob):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         

    with open(user_list, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = ''
        for line in f:
            if(line.startswith(userjob)):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         
    return
#나머지는 시민으로 
def get_result(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         
    with open(user_list, encoding='UTF8') as f:
        tl = sum(1 for line in f)

    return tl

def p1(rcode):
    userjobrandomlist = []
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = tl + 1      
    for i in range(1, tl):
        data = linecache.getline(user_list, i).strip()
        userjobrandomlist.append(data)
    return userjobrandomlist

def p2(rcode):
    userjob = choosepolice1(rcode)
    choiceList = random.choice(userjob)
    
    return choiceList

def p3(rcode, userjob):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"         

    with open(user_list, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = ''
        for line in f:
            if(line.startswith(userjob)):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         
    return
