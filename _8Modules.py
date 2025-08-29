# use to accsess function from anotther files and use 
import sys
sys.path.append(r'D:\python') 
from _7Function import add
d = add(12,12)
print(d)

# jab bhe ham es ko run kare ge to sab run ho ga q ka ham na function file ma sab ko 
# call kr rkha ha agr ham chate han ka sirf add call ho to ya use karna ho ga 
# file ma jab bhe ham na function call kia

"""
if __name__ == "__main__":
    # test calls here, will only run if you execute this file directly
    printSuccess()
"""
# ya phir file ma jhan pr bhe function call hoa han uss ko wha sy hata do