#################
# 演算子
#################


print('-----------------算術演算-----------------')
#定義
iNum1=5
iNum2=3
strData1='おはよう'
strData2='さん'

print('加算( + ) = ',iNum1 + iNum2)
print('減算( - ) = ',iNum1 - iNum2)
print('掛け算( * ) = ',iNum1 * iNum2)
print('わり算( / ) = ',iNum1 / iNum2)
print('切捨てわり算( // ) = ',iNum1 // iNum2)
print('余り( % ) = ',iNum1 % iNum2)
print('べき乗( ** ) = ',iNum1 ** iNum2)

print('加算( + ) = ',strData1 + strData2)

print('-----------------論理演算-----------------')

print('aかつb( and ) = ',iNum1==5 and iNum2==2)
print('aまたはb( or ) = ',iNum1==5 or iNum2==2)
print('aまたはbでない( or not ) = ',not iNum1==4 or not iNum2==2)

print('-----------------比較演算子-----------------')
#定義
#定義
iNum3=5
iNum4=[3,5,7]
strData1='はよ'
strData2='おはよう'

print('aとb等しい( == ) = ',iNum1==iNum2)
print('aとb異なる( != ) = ',iNum1!=iNum2)
print('aとb等しい( is ) = ',iNum1 is iNum2)
print('aとb異なる( is not ) = ',iNum1 is not iNum2)
print('a < b( < ) = ',iNum1 < iNum2)
print('a > b( > ) = ',iNum1 > iNum2)
print('a <= b( <= ) = ',iNum1 <= iNum2)
print('a >= b( >= ) = ',iNum1 >= iNum2)

#文字列、もしくはリストやタプル、辞書
print('aがbに含まれる( in ) = ',iNum3 in iNum4)
print('aがbに含まれない( not in ) = ',iNum3 not in iNum4)
print('aがbに含まれる( in ) = ',strData1 in strData2)
print('aがbに含まれない( not in ) = ',strData1 not in strData2)

print('-----------------代入演算子-----------------')
#定義
iNum5=1
iNum6=3

iNum5 = iNum6
print('aにbを入れる( = ) = ',iNum5)
iNum5 += iNum6
print('+= 3(a = a + 3と同じ) = ',iNum5)
iNum5 -= iNum6
print('-= 3(a = a - 3と同じ)  = ',iNum5)
iNum5 *= iNum6
print('*= 3(a = a * 3と同じ)  = ',iNum5)
iNum5 /= iNum6
print('/= 3(a = a / 3と同じ) = ',iNum5)
iNum5=5
iNum5 %= iNum6
print('%= 3(a = a % 3と同じ)  = ',iNum5)
iNum5 **= iNum6
print('**= 3(a = a ** 3と同じ)  = ',iNum5)
iNum5 //= iNum6
print('//= 3(a = a // 3と同じ)  = ',iNum5)
