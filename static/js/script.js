let next = document.getElementById("next")
next.addEventListener('click', nextImage);
let previous = document.getElementById("previous")
previous.addEventListener('click', backImage);

let imageIndex = 1;
showImage(imageIndex);

function nextImage() {
    imageIndex += 1;
    showImage(imageIndex);
}

function backImage() {
    imageIndex -= 1;
    showImage(imageIndex);
}

function showImage(n) {
  let i;
  let images = document.getElementsByClassName("journeyImages");
  if (n > images.length) {imageIndex = 1}
  if (n < 1) {slideIndex = images.length}
  for (i = 0; i < images.length; i++) {
    images[i].style.display = "none";
  }
  images[imageIndex-1].style.display = "block";
}