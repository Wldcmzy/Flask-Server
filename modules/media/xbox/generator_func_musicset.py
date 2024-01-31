
from pathlib import Path
import os
import tqdm
from .generator_config import *
from .generator_strings import (
    MUSICSET_HTML_MAIN,
    MUSICSET_HTML_ITEM,
)


def generate_musicset(
    content_path: Path,
    webpage_path: Path,
    content_url: str,
    webpage_url: str,
) -> None:
    print(f'<musicset> 开始生成音乐集, 路径 = {content_path}')
    lstdir = os.listdir(content_path)
    musics = []
    for eachfile in lstdir:
        for eachformat in MUSIC_FILE_FORMA_LIST:
            if eachfile.endswith(f'.{eachformat}'):
                musics.append(eachfile)
                break
    musics_items = ''

    # for musicname in musics:



