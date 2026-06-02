# A list of Little Man Computer programs that I made

<https://peterhigginson.co.uk/lmc/>

## Multiply two numbers

``` Assembly
        INP
        STA num1
        INP
        STA num2

startLoop LDA num2
        SUB i
        BRZ finished
        LDA result
        ADD num1
        STA result
        LDA i
        ADD one
        STA i
        BRA startLoop

i       DAT 0
num1    DAT 0
num2    DAT 0
one     DAT 1
result  DAT 0

finished LDA result 
        OUT
        HLT

```

## Fibonacci series

``` Assembly
        LDA one
        OUT
        OUT

startLoop LDA iterations
        SUB i
        BRZ finished

        LDA num1
        ADD num2
        STA temp
        LDA num2
        STA num1
        LDA temp
        STA num2
        OUT

        LDA i
        ADD one
        STA i
        BRA startLoop

iterations DAT 14
i       DAT 0
num1    DAT 1
num2    DAT 1
temp    DAT 0
one     DAT 1

finished HLT
```

## Division (with remainders)

``` Assembly

        INP
        STA num1
        INP
        STA num2

startLoop LDA num1
        SUB num2
        STA num1
        BRP addOne
        BRA finish

num1    DAT 0
num2    DAT 0
result  DAT 0
one     DAT 1

addOne  LDA result
        ADD one
        STA result
        BRA startLoop

finish  LDA result
        OUT
        LDA num1
        ADD num2
        OUT
        HLT
```

## Calculator

The inputs are:

1. First number
2. Operation (+: 1, -: 2, x: 3, /:4)
3. Second number

``` Assembly
        INP
        STA num1
        INP
        STA operation
        INP
        STA num2

        LDA operation
        SUB one 
        BRZ addition
        SUB one
        BRZ subtract
        SUB one
        BRZ multiply
        BRA div

num1    DAT 0
operation DAT 0
num2    DAT 0
result  DAT 0
one     DAT 1
i       DAT 0

addition LDA num1
        ADD num2
        OUT 
        HLT

subtract LDA num1
        SUB num2
        OUT 
        HLT

multiply LDA num2
        SUB i
        BRZ finishMul
        LDA result
        ADD num1
        STA result
        LDA i
        ADD one
        STA i
        BRA multiply

div     LDA num1
        SUB num2
        STA num1
        BRP addOne
        BRA finishDiv

addOne  LDA result
        ADD one
        STA result
        BRA div

finishMul LDA result
        OUT
        HLT

finishDiv LDA result
        OUT
        LDA num1
        ADD num2
        OUT
        HLT

```

## IsPrime(num)

```Assembly
        INP        STA num
        BRA loop
modulo  LDA a
        SUB i
        STA a
        BRP modulo
        ADD i
        STA moduloRes
        BRA return
num     DAT
a       DAT
i       DAT 2
one     DAT 1
moduloRes DAT
loop    LDA num
        SUB i
        BRZ true
        LDA num
        STA a
        BRA modulo
return  LDA moduloRes
        BRZ false
        LDA i
        ADD one
        STA i
        BRA loop
false   OUT
        HLT
true    LDA one
        OUT
        HLT
```
