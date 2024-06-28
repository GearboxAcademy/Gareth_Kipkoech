let container = document.getElementById("Slide_Container");
let slides = document.getElementsByClassName("slides");
let pos = 0;
console.log(slides.length);

slides[0].innerHTML = (1) + " : " + slides[0].innerHTML;
for (let i = 1; i < slides.length; i++) {
    slides[i].innerHTML = (i + 1) + " : " + slides[i].innerHTML;
    slides[i].classList.add("hide");
}

function next() {
    slides[pos].classList.add("hide");
    pos += 1;
    if (pos < slides.length) {
        pos = pos;
    } else {
        pos = 0;
    }
    slides[pos].classList.remove("hide");
}

function prev() {
    slides[pos].classList.add("hide");
    pos -= 1;
    if (pos > 0) {
        pos = pos;
    } else {
        pos = slides.length - 1;
    }
    slides[pos].classList.remove("hide");
}