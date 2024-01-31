import os
from flask import Flask, request, session, redirect
from flask_cors import CORS
from .identifiy import check_cookie
from .config import LOGIN_REQUIRED


class ModuleMessage:
    def __init__(self, name: str, url_prefix: str) -> None:
        self.__name = name
        self.__url_prefix = url_prefix
    
    def get_name(self) -> str:
        return self.__name
    
    def get_url_prefix(self) -> str:
        return self.__url_prefix
    
    def __str__(self) -> str:
        return f'ModuleName: {self.__name} urlPrefix:{self.__url_prefix}'
    
    def __repr__(self) -> str:
        return f'ModuleName: {self.__name} urlPrefix:{self.__url_prefix}'

active_modules: list[ModuleMessage] = []

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, supports_credentials=True)

def judge_url_pass(url : str) -> bool:
    pass_url: list[str] = ['/login', '/register']
    pass_prefix: list[str] = ['/static/nologin']
    if url in pass_url: return True
    for each in pass_prefix: 
        if url.startswith(each): return True 
    return False

@app.before_request
def before():
    if LOGIN_REQUIRED:
        url = request.path
        if judge_url_pass(url):
            pass
        else:
            username = session.get('username', None)
            cookie = session.get('cookie', None)
            if not cookie or not check_cookie(username, cookie):
                return redirect('/login')
            else:
                pass

