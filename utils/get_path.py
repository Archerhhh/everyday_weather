# coding: utf-8
# author: hmk

import os
def get_path():
    base_path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    return base_path_dir

def get_cwd():
    root_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本的目录
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return root_dir

if __name__ == '__main__':
    print(get_path())
    print(get_cwd())