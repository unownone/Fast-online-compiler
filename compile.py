from subprocess import Popen,PIPE
import time
#########Provides helper functions to compile and return
#########different codes , can be hotplugged with performance 
#########metrics and other things
#########Pass the filename with arguments if any as a string 
######### The Argument needs to be in a string with multiline input 
######### being separated by an \n or newline escape character
import os
from uuid import uuid4

def runPython(code,args=''):
    path =f'codes/python/{uuid4()}.py'
    if not os.path.exists('/'.join(path.split('/')[:-1])): os.makedirs('/'.join(path.split('/')[:-1]))
    with open(path,'w') as file:
        file.write(code)
    process = Popen(['python',path],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runJava(code,args=''):
    path =f'codes/java/{uuid4()}.java'
    if not os.path.exists('/'.join(path.split('/')[:-1])): os.makedirs('/'.join(path.split('/')[:-1]))
    with open(path,'w') as file:
        file.write(code)
    process = Popen(['javac',path],stdin=PIPE,stdout=PIPE)
    process = Popen(['java',path],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runCpp(code,args=''):
    path =f'codes/cpp/{uuid4()}.cpp'
    if not os.path.exists('/'.join(path.split('/')[:-1])): os.makedirs('/'.join(path.split('/')[:-1]))
    with open(path,'w') as file:
        file.write(code)
    pathname = '/'.join((pp:=path.split('/'))[:-1])
    outpath = pathname+'/' + '.'.join(pp.split('.')[:-1])
    process = Popen(['g++',path,'-o',+outpath],stdin=PIPE,stdout=PIPE)
    time.sleep(1)
    process = Popen(['./'+outpath],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')

def runC(code,args=''):
    path =f'codes/cpp/{uuid4()}.cpp'
    if not os.path.exists('/'.join(path.split('/')[:-1])): os.makedirs('/'.join(path.split('/')[:-1]))
    with open(path,'w') as file:
        file.write(code)
    pathname = '/'.join((pp:=path.split('/'))[:-1])
    outpath = pathname+'/' + '.'.join(pp.split('.')[:-1])
    process = Popen(['gcc',path,'-o',outpath],stdin=PIPE,stdout=PIPE)
    time.sleep(1)
    process = Popen(['./'+outpath],stdin=PIPE,stdout=PIPE)
    process = process.communicate(bytes(args,'utf-8'))[0]
    return process.decode('utf-8')



SUPPORTED_LANGS = {'Python':runPython,
                   'Java':runJava,
                   'C':runC,
                   'C++':runCpp,
}

def main(code:str,language:str,arguments:str='')-> str:
    if language not in SUPPORTED_LANGS:
        return "Language Not Supported"
    return SUPPORTED_LANGS[language](code,arguments)
