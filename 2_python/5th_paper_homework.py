#プログラミング教室05の課題#

#===========#a+bの結果が100以上ならtrue 未満ならfalseを返す#===========#

#python3.8以降で使えるセイウチ演算子を使った行数圧縮バージョン#
if((a:=int(input())) + (b:=int(input())) > 100):
    print("True")
else:
    print("False")

#普通に書いたバージョン
print("aを入力")
a = int(input())
print("bを入力")
b = int(input())

if (a+b) > 100:
    print("True")
else:
    print("False")    


#===========#0~100までの偶数を全て足す#===========#
b = 0
for a in range(1,101):
    if a%2 == 0:
        b = b + a

print(b)