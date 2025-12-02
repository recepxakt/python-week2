from typing import List
isimler:  List[str] = ["ali","ayse","mehmet","zeynep"]
yaslar: list[int] = [25 ,30 , 35 , 28 ]   

for i, (isim, yas) in enumerate(zip(isimler, yaslar)):
    print(i, "=" ,isim,yas)