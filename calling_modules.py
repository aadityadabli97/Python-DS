from  new import new_script # here we are importing package
from modules import my_fun # here we are importing modules
from new.subpackage import subpackagefile # here we are importing subpackage  but for that first we have to import its parent package  that is new package

my_fun()     # we are calling modules file from here ,in modules file we have given a function called as my_fun

new_script.new_script_fun() # here we are calling package
subpackagefile.sub_package()  # here we are calling subpackage