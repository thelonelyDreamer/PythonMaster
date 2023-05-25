import sys

from base import script1
from base import script2
import json
import os
import re

if __name__ == '__main__':
    script1.test()
    script2.test()
    print(os.getcwd())
    print(os.name)
    os.makedirs('test/1',exist_ok=True)
    print(sys.path[0])

    s = 'Hello, Mr.Gumby : 2016/10/26'
    p = re.compile("(?P<name>\w+\.\w+).*?(\d+)(?#comment)")
    m = p.search(s)

    # 使用别名访问
    print(m.group('name'))
    # 输出 Mr.Gumby
    # 使用分组访问
    print(m.group(2))
    # 输出 2016


def fun(file: str):
    try:
        with open(file) as f:
            username = json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        username = None
    else:
        pass
    finally:
        pass
    return username
