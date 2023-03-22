x=int(input())
y=x
k=2
s=''
while y>0:
    o=y%2
    c=str(o)
    s=s+c
    y=y//2
    text = s[::-1]
    print(text)
    text=str(text)
    text=text.replace('0', "")
    print(text)