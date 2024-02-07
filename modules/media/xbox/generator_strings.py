HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/media/resourcemedia/css/indexpage.css">
    <script src="/media/resourcemedia/js/indexpage.js"></script>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <br/>

    <div class="search-container">
        <input type="text" id="search-input" placeholder="输入关键词">
        <button id="search-button" onclick="search()">搜索</button>
    </div>
    <br/>
    <button id="scroll-up-btn" onclick="scrollPage(-0.2)">向上滑动</button>
    <button id="scroll-down-btn" onclick="scrollPage(0.2)">向下滑动</button>

    {items}

</body>
</html>

'''

HTML_ITEM = '''
    <div class="box" onclick="window.open('{link}')">
        <img src="{image_preview}" alt="Image 1">
        <p>{text}</p>
    </div>

'''


SINGLE_IMAGESET_HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/media/resourcemedia/css/single_imageset.css">
    <title>{title}</title>
</head>
<body>
    <div id="header">{title}</div>
    <div id="images">
        {items}
    </div>
</body>
</html>

'''

SINGLE_IMAGESET_HTML_ITME = '''
    <img src="{src}" alt="Image">

'''


INAGESET_INDEX_HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/media/resourcemedia/css/indexpage.css">
    <script src="/media/resourcemedia/js/indexpage.js"></script>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <br/>
    {cover}

    <div class="search-container">
        <input type="text" id="search-input" placeholder="输入关键词">
        <button id="search-button" onclick="search()">搜索</button>
    </div>
    <br/>
    <button id="scroll-up-btn" onclick="scrollPage(-0.2)">向上滑动</button>
    <button id="scroll-down-btn" onclick="scrollPage(0.2)">向下滑动</button>

    {items}

</body>
</html>

'''

INAGESET_INDEX_HTML_ITEM = '''
    <div class="box" onclick="window.open('{link}')">
        <img src="{image_preview}" alt="Image 1">
        <p>{text}</p>
    </div>

'''
INAGESET_INDEX_HTML_COVER = '''
    <img src="{coverlink}" alt="Image" style="width: 85%; max-width: 100%; height: auto;">
    <br/>
'''

VIDEOSET_INDEX_HTML_MAIN = '''

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="/media/resourcemedia/css/index_videoset.css">
	<script src="/media/resourcemedia/js/someusefulutils.js"></script>
    <title>{title}</title>
</head>
<body>

<h1>{title}</h1>
<img id="coverImage" src="{cover_url}" alt="Cover Image">

<button id="scroll-up-btn" onclick="scrollPage(-0.2)">向上滑动</button>
<button id="scroll-down-btn" onclick="scrollPage(0.2)">向下滑动</button>

<div class="box-container" id="boxContainer">
    <!-- Boxes will be dynamically added here using JavaScript -->
</div>

<script>
    // Number of boxes
    var numberOfBoxes = {item_number}; // Adjust as needed

    // Get the container element
    var boxContainer = document.getElementById('boxContainer');

    // List of items with text and link
    var items = [
        {item_info}
        // Add more items as needed
    ];

    // Dynamic creation of boxes with the same background image
    for (var i = 0; i < numberOfBoxes; i++) {{
        var box = document.createElement('div');
        box.className = 'box';
        box.style.backgroundImage = 'url("{cover_url}")';

        var boxText = document.createElement('div');
        boxText.className = 'box-text';
        boxText.innerHTML = items[i % items.length].text;

        // Set the link for each box
        box.onclick = function(link) {{
            return function() {{
                //window.location.href = link;
                window.open(link, '_blank');
            }};
        }}(items[i % items.length].link);

        box.appendChild(boxText);
        boxContainer.appendChild(box);
    }}
</script>

<script>
    function adjustBoxWidth() {{
        var windowWidth = window.innerWidth;
        var boxes = document.querySelectorAll('.box');

        boxes.forEach(function (box) {{
            if (windowWidth < 400) {{
                box.style.width = '70%';
            }} else if (windowWidth < 600) {{
                box.style.width = '35%';
            }} else if (windowWidth < 700) {{
                box.style.width = '27%';
            }} else if (windowWidth < 850) {{
                box.style.width = '21%';
            }} else if (windowWidth < 1000) {{
                box.style.width = '18%';
            }} else if (windowWidth < 1250) {{
                box.style.width = '14%';
            }} else {{
                box.style.width = '10%';
            }}
        }});
    }}

    // 初始加载时调整一次
    adjustBoxWidth();

    // 在窗口大小改变时触发调整
    window.addEventListener('resize', adjustBoxWidth);
</script>

</body>
</html>

'''

VIDEOSET_INDEX_HTML_ITEM = '''
        {{ text: '{text}', link: '{link}' }},
'''


VIDEOSET_CONTEXT_HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="/media/resourcemedia/css/single_video.css">
    <title>{title}</title>

</head>
<body>

<h1>{title}</h1>

<video id="myVideo" controls preload="auto">
    <source src="{video_src}" type="video/mp4">
    {captions}
    Your browser does not support the video tag.
</video>

<button id="subtitleButton">字幕</button>

<script src="/media/resourcemedia/js/single_video.js"></script>

</body>
</html>

'''

VIDEOSET_CONTEXT_HTML_CAPTION_TIEM = '''
    <track kind="subtitles" src="{caption_url}" srclang="zh-CN" label="中文">

'''


MUSICSET_HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/media/resourcemedia/css/index_music.css">
    <script src="/media/resourcemedia/js/someusefulutils.js"></script>
	<script src="/media/resourcemedia/js/index_music.js"></script>
    
</head>
<body>
    <div id="scroll-buttons">
        <div class="scroll-button" onclick="scrollPage(-0.2)">向上滑动</div>
        <div class="scroll-button" onclick="scrollPage(0.2)">向下滑动</div>
    </div>

    <div id="play-buttons">
        <div class="play-button" onclick="togglePlayMode()">随机播放</div>
    </div>

    <div id="header">{title}</div>

    <div id="search">
        <input type="text" id="search-box" placeholder="搜索音乐">
        <input class="xfjwEi34_IOdsfmZ" type="button" value="搜索" onclick="searchMusic()">
    </div>

    <div id="music-list">
        <!-- 这里可以动态生成音乐框，例如使用服务器端数据 -->
        {items}
        <!-- 添加更多音乐框... -->
    </div>

    <div id="player">
        <div id="progress-bar">
            <div id="song-name"></div>
            <div>
                <audio controls id="audio-player">
                    <!-- 这里可以通过JavaScript设置音频源 -->
                </audio>
            </div>
        </div>
    </div>

    <script>
        var playMode = 'random'; // 初始播放模式为随机播放
		var audioPlayer = document.getElementById('audio-player');
		audioPlayer.addEventListener('ended', playRandom);
        const itempath = "{itempath}";
    </script>
</body>
</html>

'''

MUSICSET_HTML_ITEM = '''
        <div class="music-box" onclick="playMusic('{mname}')">{mname}</div>
'''


TEXTSET_HTML_MAIN = '''
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="/media/resourcemedia/css/index_textset.css">

<title>{title}</title>

</head>
<body>
<div class="header" id="title-bar" onmousemove="moveTitle(event)">
    <span id="title">{title}</span> 
    <br/>
    <span id="subtitle">{subtitle}</span>
</div>
<iframe class="content" id="novel-iframe" src="{ifream_link}" frameborder="0"></iframe> <!-- 外部网页链接 -->
<div class="menu">
    <div class="menu-option" onclick="toggleSettings(1)">设置</div>
	<div class="menu-option" onclick="toggleSettings(2)">目录</div>
</div>

<!-- 设置弹出框 -->
<div class="settings-popup" id="settings-popup">
    <div class="color-picker">
        <label for="font-color">字体颜色：</label>
        <input type="color" id="font-color" onchange="changeFontColor(event)">
    </div>
    <div class="color-picker">
        <label for="bg-color">背景颜色：</label>
        <input type="color" id="bg-color" onchange="changeBgColor(event)">
    </div>
    <div>
        <label for="font-size">字体大小：</label>
        <input type="range" id="font-size" min="10" max="40" value="20" onchange="changeFontSize(event)">
    </div>
    <div>
        <label for="font-style">字体样式：</label>
        <select id="font-style" onchange="changeFontStyle(event)">
            <option value="SimSun, sans-serif">宋体</option>
            <option value="SimHei, sans-serif">黑体</option>
            <option value="KaiTi, sans-serif">楷体</option>
			<option value="Microsoft YaHei, sans-serif">微软雅黑</option>
			<option value="FangSong, sans-serif">仿宋</option>
			
			<option value="Arial, sans-serif">Arial</option>
			<option value="Helvetica, sans-serif">Helvetica</option>
			<option value="Times New Roman, serif">Times New Roman</option>
			<option value="Georgia, serif">Georgia</option>
			<option value="Verdana, sans-serif">Verdana</option>
			<option value="Tahoma, sans-serif">Tahoma</option>
			<option value="Impact, sans-serif">Impact</option>
			<option value="Courier New, monospace">Courier New</option>
			<option value="Lucida Console, monospace">Lucida Console</option>
			<option value="Trebuchet MS, sans-serif">Trebuchet MS</option>
			<option value="Palatino Linotype, Book Antiqua, Palatino, serif">Palatino</option>
			<option value="Garamond, serif">Garamond</option>
			<option value="Bookman, serif">Bookman</option>
        </select>
    </div>
    <div>
        <label for="bold">加粗：</label>
        <input type="checkbox" id="bold" onchange="changeFontWeight(event)">
    </div>
</div>


<div class="settings-popup" id="directory-popup">
    <!-- 目录弹出框内容 -->
    {dictionary_tiems}
</div>

<script src="/media/resourcemedia/js/index_textset.js"></script>

</body>
</html>

'''

TEXTSET_HTML_ITEM = '''
    <div class="page-link" onclick="changePage('{link}', '{text}')">{text}</div>
'''

TEXTSET_HTML_IFREAM_MAIN = '''
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="/media/resourcemedia/css/index_textset_ifream.css">

<title>外部文本</title>
</head>
<body>
<div id="novel-content">
{items}
</div>
</body>
</html>

'''

TEXTSET_HTML_IFREAM_ITEM_P = '''
    <p>{text}</p>
'''

TEXTSET_HTML_IFREAM_ITEM_IMG = '''
    <img src="{link}" alt="{des}">
'''