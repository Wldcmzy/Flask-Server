from pathlib import Path
import os
import tqdm
import json
from .generator_config import *
from .generator_strings import (
    TEXTSET_HTML_MAIN,
    TEXTSET_HTML_ITEM,
    TEXTSET_HTML_IFREAM_MAIN,
    TEXTSET_HTML_IFREAM_ITEM_P,
    TEXTSET_HTML_IFREAM_ITEM_IMG,
)

def generate_textset(
    content_path: Path,
    webpage_path: Path,
    content_url: str,
    webpage_url: str,
) -> None:
    
    IFREAM_HTML_FILE_PREFIX = 'textpage_'

    print(f'\033[1;36;40m<textset>\033[0m 开始生成\033[1;36;40m文本集\033[0m, 路径 = {content_path}')
    lstdir = os.listdir(content_path)
    textfiles = []
    for file in lstdir:
        if os.path.isfile(content_path / file):
            for form in TEXT_FILE_FORMAT_LIST:
                if file.endswith('.' + form):
                    textfiles.append(file)
                    break
    
    dictionary_items = ''
    dictionary_items_extra = ''
    ifream_link = ''
    subtitle = ''
    cnt = 0
    for textfile in tqdm.tqdm(textfiles):
        cnt += 1
        textfile: str
        text_items_html = ''
        with open(content_path / textfile, 'r', encoding = 'utf-8') as f:
            text = f.read()
            paragraphs = text.split('\n')
            for paragraph in paragraphs:
                text_items_html += TEXTSET_HTML_IFREAM_ITEM_P.format(
                    text = paragraph,
                )
        text_html = TEXTSET_HTML_IFREAM_MAIN.format(
            items = text_items_html,
        )

        flen = len(textfile.split('.')[-1]) + 1
        ifream_html_file_name = IFREAM_HTML_FILE_PREFIX + textfile[ : -flen] + '.html'
        with open(webpage_path / ifream_html_file_name, 'w', encoding='utf-8') as f:
            f.write(text_html)

        link = f'{URL_PREFIX}{webpage_url}/{ifream_html_file_name}'
        dictionary_items += TEXTSET_HTML_ITEM.format(
            link = link,
            text = textfile[ : -flen],
        )




        if cnt == 1:
            ifream_link = link
            subtitle = textfile[ : -flen]
            
            if TEXTSET_IMAGESET_FOLDER in lstdir:
                AT_IFREAM_IMAGESET_FILE_NAME = f'imageset.html'
                if os.path.isdir(content_path / TEXTSET_IMAGESET_FOLDER):
                    subdir = os.listdir(content_path / TEXTSET_IMAGESET_FOLDER)
                    image_items = ''
                    for eachfile in subdir:
                        for eachformat in IMAGE_FILE_FORMAT_LIST:
                            if eachfile.endswith(eachformat):
                                image_items += TEXTSET_HTML_IFREAM_ITEM_IMG.format(
                                    link = f'{URL_PREFIX}{content_url}/{TEXTSET_IMAGESET_FOLDER}/{eachfile}',
                                    des = 'image',
                                )
                                break
                    with open(webpage_path / AT_IFREAM_IMAGESET_FILE_NAME, 'w', encoding='utf-8') as f:
                        f.write(
                            TEXTSET_HTML_IFREAM_MAIN.format(
                                items =  image_items,
                            )
                        )
                    dictionary_items_extra += TEXTSET_HTML_ITEM.format(
                        link = f'{URL_PREFIX}{webpage_url}/{AT_IFREAM_IMAGESET_FILE_NAME}',
                        text = '图集',
                    )
                


    AT_IFREAM_COVER_FILE_NAME = f'cover.html'
    for covername in COVER_FILE_NAME_LIST:
        if covername in lstdir:
            with open(webpage_path / AT_IFREAM_COVER_FILE_NAME, 'w', encoding='utf-8') as f:
                f.write(
                    TEXTSET_HTML_IFREAM_MAIN.format(
                        items =  
                        TEXTSET_HTML_IFREAM_ITEM_IMG.format(
                            link = f'{URL_PREFIX}{content_url}/{covername}',
                            des = 'COVER',
                        )
                    )
                )
            ifream_link = f'{URL_PREFIX}{webpage_url}/{AT_IFREAM_COVER_FILE_NAME}'
            dictionary_items_extra += TEXTSET_HTML_ITEM.format(
                link = ifream_link,
                text = '封面',
            )
            subtitle = '封面'
            break
    


    textset_html_main = TEXTSET_HTML_MAIN.format(
        title = str(content_path).replace('\\', '/').split('/')[-1].strip(),
        subtitle = subtitle,
        ifream_link = ifream_link,
        dictionary_tiems = dictionary_items_extra + dictionary_items,
    )

    with open(webpage_path / f'index.html', 'w', encoding='utf-8') as f:
        f.write(textset_html_main)

