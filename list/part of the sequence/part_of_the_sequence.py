i = int(input())
m = 0
m_count = m 
while(i > 0):
    m+=1 
    m_count = m
    while(m_count > 0 and i > 0 ): 
        print(m, end=' ')
        m_count-=1 
        i-=1 

