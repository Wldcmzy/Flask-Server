from pathlib import Path
import sqlite3
import hashlib

USERDATABASE = Path(__file__).parent / "database.sqlite"

def generate_passcode(password: str) -> tuple[str]:
    return str(hashlib.md5(password.encode()).hexdigest()), str(hashlib.sha256(password.encode()).hexdigest())

def sql_open_table_USERS(path: Path) -> sqlite3.Connection:
    if not path.exists():
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE USERS(
            USERNAME        TEXT        PRIMARY KEY,
            PASSCODE1       TEXT        ,
            PASSCODE2       TEXT        ,
            XCODE           TEXT        ,
            FOREIGN KEY (XCODE) REFERENCES XCODES(XCODE)
            );
        ''')
        cursor.execute('''
            CREATE TABLE XCODES(
            XCODE           TEXT        PRIMARY KEY,
            USED            INT
            );
        ''')
        # 对于USED键, 0表示未注册, 1表示正常用户, 其他表示不可使用不可访问
    else:
        conn = sqlite3.connect(path)
    return conn


def sql_adduser(conn: sqlite3.Connection, username: str, password: str, xcode: str) -> bool:
    c = conn.cursor()
    # c.execute(f'''
    #     SELECT USED FROM XCODES WHERE XCODE = "{xcode}";
    # ''')
    # x = c.fetchone()[0]
    # if x != 0: return False
    c.execute(f'''
        SELECT * FROM USERS WHERE XCODE = "{xcode}";
    ''')
    if len(c.fetchall()) > 0: return False
    c.execute(f'''
        SELECT * FROM USERS WHERE USERNAME = "{username}";       
    ''')
    if len(c.fetchall()) >0: return False
    passcode1, passcode2 = generate_passcode(password)
    c.execute(f'''
        UPDATE XCODES
        SET USED = 1
        WHERE XCODE = "{xcode}"
    ''')
    c.execute(f'''
        INSERT INTO USERS (USERNAME, PASSCODE1, PASSCODE2, XCODE)
        VALUES ("{username}", "{passcode1}", "{passcode2}", "{xcode}");
    ''')
    conn.commit()
    return True

def sql_deluser(conn: sqlite3.Connection, username: str) -> None:
    c = conn.cursor()
    c.execute(f'''
        DELETE 
        FROM USERS
        WHERE USERNAME = "{username}";
    ''')
    conn.commit()
    

def sql_identify(conn: sqlite3.Connection, username: str, password: str) -> bool:
    c = conn.cursor()
    c.execute(f'''
        SELECT USERNAME, PASSCODE1, PASSCODE2
        FROM USERS
        WHERE USERNAME = "{username}"
    ''')
    data = c.fetchall()
    if len(data) <= 0: return False
    _, passcode1, passcode2 = data[0]
    return generate_passcode(password) == (passcode1, passcode2)



if __name__ == '__main__':
    import secrets
    import string
    def generate_random_string(length: int) -> str:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(characters) for _ in range(length))
        return random_string

    def sql_generate_new_xcode_inscure(num: int) -> None:
        conn = sql_open_table_USERS(USERDATABASE)
        c = conn.cursor()
        for i in range(num):
            ss = generate_random_string(6)
            for j in range(3):
                ss += '_' + generate_random_string(6)
            c.execute(f'''
                INSERT INTO XCODES (XCODE, USED)
                VALUES ("{ss}", "0");
            ''')
        conn.commit()
    
    # 随机生成xcode
    # sql_generate_new_xcode_inscure(100)
        

    # 注册一个账号
    # conn = sql_open_table_USERS(USERDATABASE)
    # sql_adduser(conn, 'adsf', 'fdf', 'VQ5jOc_wXQwvb_mGDDe5_vOOj17')