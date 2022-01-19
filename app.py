from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from compile import main, SUPPORTED_LANGS

app = FastAPI()

class codeInput(BaseModel):
    code: str
    args: str
    lang: str
    

@app.get('/getLangs')
def get_supported_languages():
    return list(SUPPORTED_LANGS.keys())


@app.post('/compile')
def get_compiled_code(input:codeInput):
    return {
        'response': main(input.code,input.lang,input.args)
    }
