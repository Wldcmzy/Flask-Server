import os
from ebooklib import epub
from bs4 import BeautifulSoup
import ebooklib

def extract_chapters_from_epub(epub_file_path, output_dir):
    # 打开EPUB文件
    book = epub.read_epub(epub_file_path)

    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 提取所有章节的文本
    cnt = 0
    for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
        # 获取文档内容
        content = item.get_content()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')

        # 提取文本
        text = soup.get_text()
        text = text.strip()
        if text.strip() == '': continue

        cnt += 1
        # 构造章节文件名
        ii = str(cnt)
        if len(ii) < 4:
            ii = '0' * (4 - len(ii)) + ii
        chapter_file_name = f"{ii} chapter_{cnt}.txt"

        # 写入章节文本文件
        with open(os.path.join(output_dir, chapter_file_name), "w", encoding='utf-8') as chapter_file:
            chapter_file.write(text + '\n')

    # print("Extraction completed. Chapters saved successfully.")

def extract_images_from_epub(epub_file_path, img_output_dir):
    # 打开EPUB文件
    book = epub.read_epub(epub_file_path)

    # 创建输出目录
    if not os.path.exists(img_output_dir):
        os.makedirs(img_output_dir)

    # 提取所有图像文件
    for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_IMAGE)):
        # 构造图像文件名
        ii = str(i + 1)
        if len(ii) < 4:
            ii = '0' * (4 - len(ii)) + ii
        image_file_name = f"{ii} image_{i + 1}.png"

        # 写入图像文件
        with open(os.path.join(img_output_dir, image_file_name), "wb") as image_file:
            image_file.write(item.get_content())

    # print("Extraction completed. Images saved successfully.")



if __name__ == '__main__':
    '''
        把当前目录的所有epub文件转换为txt文件,并创建_EODFSP.json文件。
    '''
    lst = [x for x in os.listdir() if x.endswith('.epub')]
    for epub_file_name in lst:
        print('>>> ', epub_file_name)
        flen = len(epub_file_name.split('.')[-1]) + 1
        output_dir = epub_file_name[ : -flen]
        img_output_dir = output_dir + '/' + 'images'
        extract_chapters_from_epub(epub_file_name, output_dir)
        extract_images_from_epub(epub_file_name, img_output_dir)
    
        with open(os.path.join(output_dir, '_EODFSP.json'), "w", encoding='utf-8') as chapter_file:
            chapter_file.write('{"sign": "end", "type": "textset"}')
    
    os.system('pause')
