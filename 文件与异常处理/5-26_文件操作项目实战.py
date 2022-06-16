#第一题
from openpyxl import Workbook
import os
def main(txt):
    new=txt[:-3]+'xlsx'
    wb=Wockbook()
    ws=wb.worksheets[0]
    with open(txt) as fp:
        for ine in fp:
            ine=ine.strip().split(".")
            ws.append(ine)
        wb.save(new)


#第二题
file_list=os.listdir()
for filename in file_list:
    try:
        pos=filename.rindex(".")
    except:
        pass
    else:
        main(filename)