var bgColor;
var fontColor;
var fontSize;
var fontStyle;
var fontWeight;


function moveTitle(event) {
    const title = document.getElementById('title');
    const movement = 10; // 每次移动的距离
    if (event.clientX < 100 && title.scrollLeft > 0) {
        title.scrollLeft -= movement;
    } else if (event.clientX > window.innerWidth - 100 && title.scrollLeft < title.scrollWidth - window.innerWidth) {
        title.scrollLeft += movement;
    }
}

function toggleSettings(_case) {
    var settingsPopup = document.getElementById('settings-popup');
    var dictionaryPopup = document.getElementById('directory-popup');
    
    
    switch (_case){
            
        case 1:
            dictionaryPopup.style.display = 'none';
            settingsPopup.style.display = settingsPopup.style.display === 'block' ? 'none' : 'block';
            break;
            
        case 2:	
            settingsPopup.style.display = 'none';
            dictionaryPopup.style.display = dictionaryPopup.style.display === 'block' ? 'none' : 'block';
            break;
        
    }
    
}

function changeFontColor(event) {
    fontColor = event.target.value;
    document.getElementById('novel-iframe').contentDocument.body.style.color = fontColor;
}

function changeBgColor(event) {
    bgColor = event.target.value;
    document.getElementById('novel-iframe').contentDocument.body.style.backgroundColor = bgColor;
}

function changeFontSize(event) {
    fontSize = event.target.value + 'px';
    document.getElementById('novel-iframe').contentDocument.body.style.fontSize = fontSize;
}

function changeFontStyle(event) {
    fontStyle = event.target.value;
    document.getElementById('novel-iframe').contentDocument.body.style.fontFamily = fontStyle;
}

function changeFontWeight(event) {
    fontWeight = event.target.checked ? 'bold' : 'normal';
    document.getElementById('novel-iframe').contentDocument.body.style.fontWeight = fontWeight;
}

function changePage(pageUrl, subtitle) {
    document.getElementById('subtitle').innerHTML = subtitle;
    document.getElementById('novel-iframe').src = pageUrl;
    // 关闭目录弹出框
    document.getElementById('directory-popup').style.display = 'none';
}


document.getElementById('novel-iframe').onload = function() {
    if (typeof bgColor !== 'undefined') {
        this.contentDocument.body.style.backgroundColor = bgColor;
    }
    if (typeof fontColor !== 'undefined') {
        this.contentDocument.body.style.color = fontColor;
    }
    if (typeof fontSize !== 'undefined') {
        this.contentDocument.body.style.fontSize = fontSize;
    }
    if (typeof fontStyle !== 'undefined') {
        this.contentDocument.body.style.fontFamily = fontStyle;
    }
    if (typeof fontWeight !== 'undefined') {
        this.contentDocument.body.style.fontWeight = fontWeight;
    }
};