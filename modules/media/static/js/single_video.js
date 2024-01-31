
// var video = document.getElementById('myVideo');
const video = document.getElementById('myVideo');
// const subtitles = document.querySelector('track');
const subtitleButton = document.getElementById('subtitleButton');
const subtitleTracks = video.textTracks;

video.addEventListener('click', function () {
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
});

// video.addEventListener('dblclick', function (event) {
//     event.preventDefault(); // 阻止默认行为

//     var clickPosition = event.clientX < window.innerWidth / 2 ? 'left' : 'right';

//     if (clickPosition === 'left') {
//         video.currentTime -= 5;
//     } else {
//         video.currentTime += 5;
//     }
// });

video.addEventListener('dblclick', function () {
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
});

video.addEventListener('touchend', function (event) {
    event.preventDefault(); // 阻止默认行为

    var clickPosition = event.changedTouches[0].clientX < window.innerWidth / 2 ? 'left' : 'right';

    if (clickPosition === 'left') {
        video.currentTime -= 5;
    } else {
        video.currentTime += 5;
    }
});

video.addEventListener('ended', function () {
    video.currentTime = 0;
});





// for (let i = 0; i < subtitleTracks.length; i++) {
//     subtitleTracks[i].mode = 'hidden'; // 隐藏所有字幕轨道
// }

function toggleSubtitles() {
    for (let i = 0; i < subtitleTracks.length; i++) {
        if (subtitleTracks[i].mode === 'showing') {
            subtitleTracks[i].mode = 'hidden';
        } else {
            subtitleTracks[i].mode = 'showing';
        }
    }
}

subtitleButton.addEventListener('click', () => {
    console.log('captionbutton clicked');
    toggleSubtitles();
});