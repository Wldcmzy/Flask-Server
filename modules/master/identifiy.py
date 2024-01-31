import uuid
import time
from .sqlApi import sql_identify, sql_adduser, sql_open_table_USERS, USERDATABASE
from .config import MAX_INACTIVE_TIME



class Cookie:
    def __init__(self, value = None):
        self.time = time.time()
        if not value:
            self.value = uuid.uuid4()
        else:
            self.value = value
    
    def update(self):
        self.time = time.time()
    
    def check_overdue(self):
        return int(time.time()) - self.time > MAX_INACTIVE_TIME

cookie_dict: dict[str, Cookie] = {}

def check_cookie(username: str, cookie: Cookie) -> bool:
    if username not in cookie_dict: return False
    cookie = cookie_dict[username]
    if cookie.check_overdue():
        del cookie_dict[username]
        return False
    cookie.update()
    cookie_dict[username] = cookie
    return True

def check_login_datas(username: str, password: str) -> bool:
    conn = sql_open_table_USERS(USERDATABASE)
    return sql_identify(conn, username, password)


def user_register(username: str, password: str, xcode: str) -> bool:
    conn = sql_open_table_USERS(USERDATABASE)
    return sql_adduser(conn, username, password, xcode)