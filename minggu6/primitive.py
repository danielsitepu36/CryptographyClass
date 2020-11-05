def primgf():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(len(prime)):
        print()
        print("GF(", prime[i], ")")
        for j in range(prime[i])[2:]:
            print("test", j, end=": ")
            isprim = True
            delim = ", "
            for k in range(prime[i])[1:-1]:
                if(j**k) % prime[i] == 1:
                    isprim = False
                    delim = "--"
                print((j**k) % prime[i], end=delim)
            if isprim:
                print("PRIMITIVE")
            else:
                print()


primgf()
