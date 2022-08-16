// Create Slide Show for Detail View

if (window.location.pathname.includes('/detail')) {

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
}

// Create tabs for profile progress and achievements

if (window.location.pathname.includes('/profile')) {
  let progress_button = document.getElementById("progress-button")
  let achievements_button = document.getElementById("achievements-button")

  let progress = document.getElementById('progress')
  let achievements = document.getElementById('achievements')

  progress_button.addEventListener('click', showProgress);
  achievements_button.addEventListener('click', showAchievements);


  function showProgress() {
    progress.style.display = "block";
    progress_button.classList.add('tabs-button-active')
    achievements.style.display = "none";
    achievements_button.classList.remove('tabs-button-active')
  }

  function showAchievements() {
    progress.style.display = "none";
    progress_button.classList.remove('tabs-button-active')
    achievements.style.display = "block";
    achievements_button.classList.add('tabs-button-active')
  }
}
