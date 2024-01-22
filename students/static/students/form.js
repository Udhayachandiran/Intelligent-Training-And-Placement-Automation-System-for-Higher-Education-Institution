const slidePage = document.querySelector(".my-slidepage");
const firstNextBtn = document.querySelector(".my-next-1");
const prevBtnSec = document.querySelector(".my-prev-2");
const nextBtnSec = document.querySelector(".my-next-2");
const prevBtnThird = document.querySelector(".my-prev-3");
const prevBtnFour = document.querySelector(".my-prev-4");
const nextBtnThird = document.querySelector(".my-next-3");
// const submitBtn = document.querySelector(".my-submit");
const progressText = document.querySelectorAll(".my-step p");
const progressCheck = document.querySelectorAll(".my-step .my-check");
const bullet = document.querySelectorAll(".my-step .my-bullet");
let max = 4;
let current = 1;
//below commands help page move
firstNextBtn.addEventListener("click", function () {
    slidePage.style.marginLeft = "-25%";
    bullet[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    current += 1;
});
nextBtnSec.addEventListener("click", function () {
    slidePage.style.marginLeft = "-50%";
    bullet[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    current += 1;
});
nextBtnThird.addEventListener("click", function () {
    slidePage.style.marginLeft = "-75%";
    bullet[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    current += 1;
});
// submitBtn.addEventListener("click", function () {
//     bullet[current - 1].classList.add("active");
//     progressText[current - 1].classList.add("active");
//     progressCheck[current - 1].classList.add("active");
//     current += 1;
//     setTimeout(function () {
//         alert("Details successfully submitted");
//     }, 800);
// });
/* ---------USE incase we need new page
nextBtnThird.addEventListener("click", function(){
    slidePage.style.marginLeft = "-75%";
  
});
submitBtn.addEventListener("click", function(){
    bullet[current -1].classList.add("active");
    progressText[current -1].classList.add("active");
    progressCheck[current -1].classList.add("active");
    current += 1;
    setTimeout(function(){
        alert("Details successfully submitted");
        location.reload();
    }, 800);
  
});
*/

//previous page command..keep increasing percentage for additional pages
prevBtnSec.addEventListener("click", function () {
    slidePage.style.marginLeft = "0%";
    bullet[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    current -= 1;
});
prevBtnThird.addEventListener("click", function () {
    slidePage.style.marginLeft = "-25%";
    bullet[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    current -= 1;
});
prevBtnFour.addEventListener("click", function () {
    slidePage.style.marginLeft = "-50%";
    bullet[current - 2].classList.remove("active");
    progressText[current - 2].classList.remove("active");
    progressCheck[current - 2].classList.remove("active");
    current -= 1;
});
