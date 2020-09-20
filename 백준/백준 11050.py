def factorial(numa, numb) :
    geta = 1
    getb = 1
    
    start = numb

    while start != 0 :
        geta = geta * numa

        numa = numa - 1
        start = start - 1

    while numb != 1 :
        getb = getb * numb

        numb = numb - 1

    return geta // getb


n , k = map(int, input().split())

print(factorial(n,k))
