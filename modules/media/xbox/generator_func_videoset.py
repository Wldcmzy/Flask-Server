from pathlib import Path
import os
import tqdm
import json
from .generator_config import *
from .generator_strings import (
    VIDEOSET_CONTEXT_HTML_MAIN,
    VIDEOSET_INDEX_HTML_ITEM,
    VIDEOSET_INDEX_HTML_MAIN,
    VIDEOSET_CONTEXT_HTML_CAPTION_TIEM,
)

def generate_videoset(
    content_path: Path,
    webpage_path: Path,
    content_url: str,
    webpage_url: str,
) -> None:
    print(f'<videoset> 开始生成视频集, 路径 = {content_path}')
    lstdir = os.listdir(content_path)
    videos = [f for f in lstdir if f.endswith('.mp4')]
    videos_index_items = ''

    captions_map = None
    captions_path = os.path.join(content_path, VIDEO_CAPTIONS_FOLDER)
    if (VIDEO_CAPTIONS_FOLDER in lstdir) and (os.path.isdir(captions_path)):
        captions_list = os.listdir(captions_path)
        if VIDEO_CAPTIONS_MAP_FILE in captions_list:
            with open(content_path / VIDEO_CAPTIONS_FOLDER / VIDEO_CAPTIONS_MAP_FILE, 'r', encoding='utf-8') as f:
                captions_map =  json.loads(f.read())

    for videoname in tqdm.tqdm(videos):
        video_src = f'{URL_PREFIX}{content_url}/{videoname}'

        captions = ''
        if captions_map != None and videoname in captions_map:
            for caption_file_name in captions_map[videoname]:
                caption_url = f'{URL_PREFIX}{content_url}/{VIDEO_CAPTIONS_FOLDER}/{caption_file_name}'
                captions += VIDEOSET_CONTEXT_HTML_CAPTION_TIEM.format(
                    caption_url = caption_url,
                )

        video_content_html_title = videoname[ : -4] if videoname.endswith('.mp4') else videoname
        video_content_html_text = VIDEOSET_CONTEXT_HTML_MAIN.format(
            title = video_content_html_title, 
            video_src = video_src,
            captions = captions,
        )
        video_content_html_path = webpage_path / f'video_{videoname}.html'
        with open(video_content_html_path, 'w', encoding='utf-8') as f:
            f.write(video_content_html_text)
        
        video_content_html_url = f'{URL_PREFIX}{webpage_url}/video_{videoname}.html'
        videos_index_items += VIDEOSET_INDEX_HTML_ITEM.format(
            text = video_content_html_title, 
            link = video_content_html_url
        )

    cover_url = ''
    for coverimagename in COVER_FILE_NAME_LIST:
        if coverimagename in lstdir:
            cover_url = f'{URL_PREFIX}{content_url}/{coverimagename}'
            break

    video_index_html_text = VIDEOSET_INDEX_HTML_MAIN.format(
        title = str(content_path).replace('\\', '/').split('/')[-1].strip(),
        item_number = len(videos),
        item_info = videos_index_items,
        cover_url = cover_url,
    )
    video_index_html_path = webpage_path / 'index.html'
    with open(video_index_html_path, 'w', encoding='utf-8') as f:
        f.write(video_index_html_text)