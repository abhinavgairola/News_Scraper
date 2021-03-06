
import re
import importlib

class enquiry:
    def __init__(self):

        self.pattern = re.compile('__')

        return None
    
    def help_method_module(self, module_to_load):
        module = importlib.import_module(module_to_load) 

        list_  = (dir(module))
        list_= [li for li in list_ if not re.match(self.pattern, li)]
        print("These are the available methods {} in the module {}".format(list_,module_to_load))
        while True:
            print("=="*10)
            text = input("Enter a method\n"+"=="*10+"\n")
            if text == "stop":
                break
            else:
                print(help(getattr(module,text)))
    
    def help_datastruct(self,datastructure):

        list_ = dir(datastructure)
        list_= [li for li in list_ if not re.match(self.pattern, li)]
        print("These are the available methods {} in the datastructure {}".format(list_,datastructure))
        while True:
            print("=="*10)
            text = input("Enter a method name or stop\n"+"=="*10+"\n")
            if text == "stop":
                break
            else:
                print(help(getattr(datastructure,text)))

if __name__ == "__main__":
    obj = enquiry()
    method_or_module = input("module or datastructure\n")
    if method_or_module == 'module':
        print("These are the installed modules {}\n".format(help("modules")))
        module = input("Module name?\n"+"=="*10+"\n")
        obj.help_method_module(module)
    elif method_or_module == 'datastructure':
        list_ds = [dict, list, tuple,str]
        datastructure = input("Datastructure name--\n 0:dict\n 1:list\n 2:tuple\n 3:str ?\n"+"=="*10+"\n")
        obj.help_datastruct(list_ds[int(datastructure)])
        

        

    

