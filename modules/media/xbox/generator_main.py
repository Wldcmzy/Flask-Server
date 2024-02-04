from pathlib import Path
import os
import json
import shutil
from typing import Optional
from .generator_config import *
from .generator_strings import HTML_ITEM, HTML_MAIN
from .generator_func_imageset import generate_imagesets
from .generator_func_videoset import generate_videoset
from .generator_func_musicset import generate_musicset

content_path: Path
webpage_path: Path

get_webpage_url = lambda: str(webpage_path).replace('\\', '/').replace(f'{STATIC_FOLDER}', STATIC_URL_PATH)
get_content_url = lambda: str(content_path).replace('\\', '/').replace(f'{STATIC_FOLDER}', STATIC_URL_PATH)

# create html content pages for items (leaf tree node) by different type
def generate_by_type(path: Path, datatype: str):
    global content_path
    global webpage_path
    content_url = get_content_url()
    webpage_url = get_webpage_url()

    # func: function = lambda *args: None

    func_map = {
        'imageset' : generate_imagesets,
        'videoset' : generate_videoset,
        'musicset' : generate_musicset,
    }

    func_map[datatype](content_path, webpage_path, content_url, webpage_url)


# create html link pages from file to subfile(tree node to child tree node)
def create_index(folders: list[str], designed_title: Optional[str]) -> None:
    global content_path
    global webpage_path

    title = str(webpage_path).split('\\')[-1]
    if designed_title:
        title = designed_title
    
    items = ''
    for folder in folders:
        
        # find image preview of each item
        folderitems = os.listdir(content_path / folder)
        image_preview = DEFAULT_IMAGE_1_URL
        for filename in IMAGE_PREVIEW_FILE_NAME_LIST:
            if filename in folderitems:
                folderitem_image_preview_url = get_content_url() + '/' + folder
                image_preview = f'{URL_PREFIX}{folderitem_image_preview_url}/{filename}'
                break

        # define (link, text, image preview) of each item
        item_url = get_webpage_url() + '/' + folder
        items += HTML_ITEM.format(
            link = f'{URL_PREFIX}{item_url}/{INDEX_FILE_NAME}',
            image_preview = image_preview,
            text = folder,
        )
    
    html = HTML_MAIN.format(
        title = title,
        items = items,
    )
    
    with open(webpage_path / INDEX_FILE_NAME, 'w', encoding = 'utf-8') as f:
        f.write(html)

# create html link pages from file to subfile(tree node to child tree node)
# create html content pages for items (leaf tree node) by different type
def dfs(designed_title: Optional[str] = None) -> None:
    global content_path
    global webpage_path

    path_eodfsp: Path = content_path / EODFSP_FILE_NAME
    if path_eodfsp.exists():
        with open(path_eodfsp, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
            if data['sign'] == 'end':
                generate_by_type(content_path, data['type'])
                return 
            
    folders = [d for d in os.listdir(content_path) if os.path.isdir(os.path.join(content_path, d))]
    create_index(folders, designed_title)
    
    for folder_name in folders:
        content_path /= folder_name
        webpage_path /= folder_name
        os.mkdir(webpage_path)
        dfs()
        content_path = content_path.parent
        webpage_path = webpage_path.parent

# main function
def regenerate() -> None:
    global content_path
    global webpage_path

    content_path = Path() / STATIC_FOLDER / CONTENT_FOLDER
    webpage_path = Path() / STATIC_FOLDER / WEBPAGE_FOLDER

    if os.path.exists(webpage_path) and os.path.isdir(webpage_path):
        shutil.rmtree(webpage_path)
    os.mkdir(webpage_path)

    dfs(MODULE_NAME)

    template_path = Path() / TEMPLATE_FOLDER 
    if os.path.exists(template_path) and os.path.isdir(template_path):
        shutil.rmtree(template_path)
    os.mkdir(template_path)
    shutil.copy(webpage_path / INDEX_FILE_NAME, template_path / INDEX_FILE_NAME)

    print('生成完成...')