
from pathlib import Path
import os
import tqdm
from .generator_config import *
from .generator_strings import (
    SINGLE_IMAGESET_HTML_ITME, 
    SINGLE_IMAGESET_HTML_MAIN,
    INAGESET_INDEX_HTML_ITEM,
    INAGESET_INDEX_HTML_MAIN,
    INAGESET_INDEX_HTML_COVER,
)

def generate_imagesets(
    content_path: Path,
    webpage_path: Path,
    content_url: str,
    webpage_url: str,
) -> None:
    print(f'<imageset> 开始生成图片集, 路径 = {content_path}')
    folders = [d for d in os.listdir(content_path) if os.path.isdir(os.path.join(content_path, d))]
    imagesets_html_text = ''
    for foldername in tqdm.tqdm(folders):
        webpage_file_path = webpage_path / f'imageset_{foldername}.html'
        image_path = content_path / foldername
        image_url_prefix = f'{URL_PREFIX}{content_url}/{foldername}'
        images_html_text = ''
        for imagename in os.listdir(image_path):
            if imagename in IMAGE_PREVIEW_FILE_NAME_LIST: continue
            image_url = image_url_prefix + '/' + imagename
            images_html_text += SINGLE_IMAGESET_HTML_ITME.format(src = image_url)

        webpage_title = foldername
        for pattern in IMAGESET_NAME_REPLACE_PATTERN_LIST:
            if re.match(pattern, webpage_title):
                webpage_title = re.sub(pattern, '', webpage_title)
                break
        webpage_html_text = SINGLE_IMAGESET_HTML_MAIN.format(
            title = webpage_title,
            items = images_html_text,
        )
        with open(webpage_file_path, 'w', encoding='utf-8') as f:
            f.write(webpage_html_text)
        
        webpage_file_url = f'{URL_PREFIX}{webpage_url}/imageset_{foldername}.html'
        image_preview = DEFAULT_IMAGE_1_URL
        lstdir = os.listdir(image_path)
        for imagepreviewfilename in IMAGE_PREVIEW_FILE_NAME_LIST:
            if imagepreviewfilename in lstdir:
                image_preview = f'{URL_PREFIX}{content_url}/{foldername}/{imagepreviewfilename}'

        imagesets_html_text += INAGESET_INDEX_HTML_ITEM.format(
            link = webpage_file_url,
            image_preview = image_preview,
            text = webpage_title,
        )

    title = str(content_path).replace('\\', '/').split('/')[-1]
    cover = ''
    lstdir = os.listdir(content_path)
    for covername in COVER_FILE_NAME_LIST:
        if covername in lstdir:
            cover = INAGESET_INDEX_HTML_COVER.format(coverlink = f'{URL_PREFIX}{content_url}/{covername}')

    index_html_text = INAGESET_INDEX_HTML_MAIN.format(
        title = title.strip(),
        items = imagesets_html_text,
        cover = cover
    )

    with open(webpage_path / f'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html_text)
        
