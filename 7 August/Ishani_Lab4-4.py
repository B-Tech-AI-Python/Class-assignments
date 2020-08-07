# Ishani Kathuria A023119819004

def outerfun(a,b):
    def innerfun(c,d):
        return c+d
    return a
    return innerfun(a,b)


res = outerfun(5,10)
print(res)
