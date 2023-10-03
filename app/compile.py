from subprocess import Popen,PIPE
import time
from concurrent.futures import ThreadPoolExecutor
#########Provides helper functions to compile and return
#########different codes , can be hotplugged with performance 
#########metrics and other things
#########Pass the filename with arguments if any as a string 
######### The Argument needs to be in a string with multiline input 
######### being separated by an \n or newline escape character
import os
from uuid import uuid4

def compile_and_run(code, language, run_process, args=''):
    path = f'/tmp/codes/{language.lower()}/{uuid4()}'
    if not os.path.exists('/'.join(path.split('/')[:-1])):
        os.makedirs('/'.join(path.split('/')[:-1]))
    with open(path, 'w') as file:
        file.write(code)
    process = None
    for step in run_process:
        command = step.get('command')
        ext = step.get('ext')
        use_args = step.get('USE_ARGS', False)
        if command:
            if process:  # If there's a previous process, wait for it to finish
                process.wait()
            process_args = [command]
            if ext:
                process_args.append(f'{path}{ext}')
            if use_args:
                process_args.append(args)
            process = Popen(process_args, stdin=PIPE, stdout=PIPE)
    if process:  # If there's a final process, get its output
        output = process.communicate(bytes(args, 'utf-8'))[0]
        return output.decode('utf-8')


SUPPORTED_LANGS = {
        'Python': [{'command': 'python3', 'ext': '.py', 'USE_ARGS': True}],
        'Java': [{'command': 'javac', 'ext': '.java'}, {'command': 'java', 'ext': '', 'USE_ARGS': True}],
        'C++': [{'command': 'g++', 'ext': '.cpp'}, {'command': '', 'ext': '', 'USE_ARGS': True}],
        'C': [{'command': 'gcc', 'ext': '.c'}, {'command': '', 'ext': '', 'USE_ARGS': True}]
}

def main(code:str, language:str, arguments:str='', run_process:dict={})-> str:
    if language not in SUPPORTED_LANGS:
        return "Language Not Supported"
    return compile_and_run(code, language, SUPPORTED_LANGS[language], arguments)
