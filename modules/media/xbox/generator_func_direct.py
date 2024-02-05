import json
from pathlib import Path
import os
import tqdm
from .generator_config import *
from .generator_strings import (
    HTML_ITEM,
    HTML_MAIN,
)

def generate_direct(
    content_path: Path,
    webpage_path: Path,
    content_url: str,
    webpage_url: str,
) -> None:
    with open(content_path / EODFSP_FILE_NAME, 'rb') as f:
        dic = json.loads(f.read())
    if dic['sign'] != 'end' or dic['type'] != 'direct':
        return None
    
    print(f'\033[1;31;40m<direct>\033[0m 开始生成\033[1;31;40m直接集\033[0m, 路径 = {content_path}')
    suffix_list = ['.' + x for x in dic['suffix']]
    files = []
    for each in os.listdir(content_path):
        if os.path.isfile(os.path.join(content_path, each)):
            if each == EODFSP_FILE_NAME: continue
            if suffix_list == []:
                files.append(each)
            else:
                for suffix in suffix_list:
                    if each.endswith(suffix):
                        files.append(each)
    
    items = ''
    for file in tqdm.tqdm(files):
        items += HTML_ITEM.format(
            link = f'{URL_PREFIX}{content_url}/{file}',
            image_preview = DEFAULT_IMAGE_1_URL,
            text = file,
        )
    
    
    with open(webpage_path / f'index.html', 'w', encoding='utf-8') as f:
        f.write(HTML_MAIN.format(
            title = str(content_path).replace('\\', '/').split('/')[-1].strip(),
            items = items,
        ))


