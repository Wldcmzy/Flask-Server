function togglePlayMode() {
    var audioPlayer = document.getElementById('audio-player');
    var playButton = document.querySelector('.play-button');
    switch (playMode) {
        case 'random':
            playMode = 'loop-single';
            playButton.textContent = '单曲循环';
            break;
        case 'loop-single':
            playMode = 'loop-list';
            playButton.textContent = '列表循环';
            break;
        case 'loop-list':
            playMode = 'stop-after-play';
            playButton.textContent = '播完就停';
            break;
        case 'stop-after-play':
            playMode = 'random';
            playButton.textContent = '随机播放';
            break;
    }
    
    audioPlayer.removeEventListener('ended', playRandom);
    audioPlayer.removeEventListener('ended', playSameMusic);
    audioPlayer.removeEventListener('ended', playNextInList);
    audioPlayer.removeEventListener('ended', stopAfterPlay);
    
    // 根据当前播放模式处理播放行为
    switch (playMode) {
        case 'random':
            console.log('random');
            // 随机播放：在播放完成后继续随机播放下一首
            audioPlayer.addEventListener('ended', playRandom);
            break;
        case 'loop-single':
            console.log('loop-single');
            // 单曲循环：在播放完成后继续循环播放当前歌曲
            audioPlayer.addEventListener('ended', playSameMusic);
            break;
        case 'loop-list':
            console.log('loop-list');
            // 列表循环：在播放完成后按照搜索结果列表顺序播放下一首
            audioPlayer.addEventListener('ended', playNextInList);
            break;
        case 'stop-after-play':
            console.log('stop');
            // 播完就停：在播放完成后停止播放
            audioPlayer.addEventListener('ended', stopAfterPlay);
            break;
    }
}

function playRandom() {
    console.log('playRandom');
    var musicBoxes = document.querySelectorAll('.music-box:not([style*="display: none"])');
    var availableSongs = [];

    var searchBox = document.getElementById('search-box');
    var searchText = searchBox.value.toLowerCase();

    musicBoxes.forEach(function(box) {
        var musicName = box.innerText.toLowerCase();
        if (musicName.includes(searchText)) {
            availableSongs.push(musicName);
        }
    });

    if (availableSongs.length > 0) {
        var randomIndex = Math.floor(Math.random() * availableSongs.length);
        var randomSong = availableSongs[randomIndex];
        playMusic(randomSong);
    }
}

function playSameMusic() {
    var audioPlayer = document.getElementById('audio-player');
    console.log('func-loop-single')
    audioPlayer.currentTime = 0; // 从头开始播放
    audioPlayer.play();
}

function playMusic(songName) {
    console.log('playerMusic = ' + songName)
    var audioPlayer = document.getElementById('audio-player');
    audioPlayer.src = itempath + '/' + songName;
    audioPlayer.play();

    var songNameDisplay = document.getElementById('song-name');
    songNameDisplay.textContent = songName;

}

function playNextInList() {
    console.log('PlayNextInList');
    var musicBoxes = document.querySelectorAll('.music-box:not([style*="display: none"])');
    var currentSong = document.getElementById('song-name').textContent;
    
    var currentIndex = -1;
    for (var i = 0; i < musicBoxes.length; i++) {
        if (musicBoxes[i].innerText === currentSong) {
            currentIndex = i;
            break;
        }
    }

    // 如果找到当前歌曲，播放下一首，否则播放第一首
    var nextIndex = (currentIndex !== -1) ? (currentIndex + 1) % musicBoxes.length : 0;
    var nextSong = musicBoxes[nextIndex].innerText;

    console.log('nextSong = ' + nextSong)
    playMusic(nextSong);
}

function stopAfterPlay() {
    var audioPlayer = document.getElementById('audio-player');
    audioPlayer.pause();
}

function searchMusic() {
    var searchBox = document.getElementById('search-box');
    var searchText = searchBox.value.toLowerCase();

    var musicBoxes = document.querySelectorAll('.music-box');
    musicBoxes.forEach(function(box) {
        var musicName = box.innerText.toLowerCase().replace(/\.[^.]*$/, '');

        // 判断是否匹配搜索文本
        if (musicName.includes(searchText)) {
            // 匹配成功，显示该音乐框
            box.style.display = 'block';
        } else {
            // 不匹配，隐藏该音乐框
            box.style.display = 'none';
        }
    });
}