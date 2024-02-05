
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
    print(f'\033[1;94;40m<musicset>\033[0m 开始生成\033[1;94;40m音乐集\033[0m, 路径 = {content_path}')
    lstdir = os.listdir(content_path)
    musics = []
    for eachfile in lstdir:
        for eachformat in MUSIC_FILE_FORMA_LIST:
            if eachfile.endswith(f'.{eachformat}'):
                musics.append(eachfile)
                break
    musics_items = ''

    for music in tqdm.tqdm(musics):
        # print(music)
        musics_items += MUSICSET_HTML_ITEM.format(
            mname = f'{music}',
        )
    
    folder_name = str(content_path).replace("\\", "/").split("/")[-1].strip()
    htmltext = MUSICSET_HTML_MAIN.format(
        title = f'音乐集:{folder_name}',
        items = musics_items,
        itempath = f'{URL_PREFIX}{content_url}',
    )


    with open(webpage_path / f'index.html', 'w', encoding='utf-8') as f:
        f.write(htmltext)

