## <big><u>静态</u></big>网页多媒体服务器模块

用于成组存放多媒体数据集，支持多级目录。

因为嫌麻烦所有所有的资源都是<big><u>**静态**</u></big>的，也不支持ajax。

## 使用说明

用户文件皆存放在`static/content`目录中。

`solo_generator.py`脚本可以根据`static/content`目录的结构自动递归生成相同结构的静态网页文件存放在`static/webpage`目录中。`solo_generator.py`脚本不会对`static/content`目录造成任何改动。

`solo_generator.py`脚本无法自动调用，用户更新`static/content`目录后应手动调用`solo_generator.py`脚本生成最新的静态网页文件。

`solo_generator.py`脚本在默认情况下只针对文件目录生成索引网页，只有遇到目录中含有`_EODFSP.json`文件时，才会根据`_EODFSP.json`文件的内容在当前目录生成多媒体文件集的网页，并停止向更深层的目录递归。

`solo_generator.py`脚本每次运行时都会先尝试删除先前的`static/webpage`目录，程序实现这一过程可能较慢，可以提前手动删除。

<big>**具体示范见`static\content\example`目录。**</big>

## 媒体集分类

`_EODFSP.json`指定了媒体集的分类。除"direct"分类外，其他分类只支持一种类型的媒体。

以下为`_EODFSP.json`文件在各种分类时的实例：

#### 图片集 imageset

文件需要放在倒数第二级目录。

```json
{"sign": "end", "type": "imageset"}
```

图片支持: image_preview, cover。

#### 音乐集 musicset

```json
{"sign": "end", "type": "musicset"}
```

图片支持: image_preview。

#### 视频集 videoset

仅支持mp4文件，字幕功能未完善。

```json
{"sign": "end", "type": "videoset"}
```

图片支持: image_preview, cover。

#### 文本集 textset

```json
{"sign": "end", "type": "textset"}
```

图片支持: image_preview, cover。

#### 直接集 direct

直接对用户返回文件。

suffix规定了可以返回文件的类型，若为[]表示返回所有类型文件。

```json
{
	"sign": "end", 
	"type": "direct", 
	"suffix": [
		"pdf"
		, "md"
	]
}
```

图片支持: 无。