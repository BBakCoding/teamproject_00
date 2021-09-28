const slideNext = document.querySelector(".slide-next");
const slidePrev = document.querySelector(".slide-prev")
//변수 설정.
const qnaBox = document.querySelector(".qna-showlist");

var clickCnt = 0;


function moveLeft(event) {
  
    qnaBox.style.transition = 'transform 1s';
    qnaBox.style.transform = 'translateX(-60vw)';
    };
    // else if (count = 2) {
    //     qnaBox.style.transition = 'transform 1s';
    // qnaBox.style.transform = 'translateX(-1200px)';
    // }

    function moveRight(event) {
  
        qnaBox.style.transition = 'transform 1s';
        qnaBox.style.transform = 'translateX(0px)';
        };

slideNext.addEventListener('click', moveLeft);
slidePrev.addEventListener('click', moveRight);

