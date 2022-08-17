// messages to timeout and go after 3 seconds

if (document.getElementsByClassName('home-page-index')) {
  setTimeout(function() {
    let messages = document.getElementById("msg")
    let alert = new bootstrap.Alert(messages);
    alert.close()
  }, 3000);
}

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

// Expand 'create post' form if image entered into first image slot

if (window.location.pathname.includes('/add_post')) {
  let first_cairn = document.getElementById("firstCairnForm")
  let second_cairn = document.getElementById("secondCairnForm")
  let third_cairn = document.getElementById("thirdCairnForm")

  second_cairn.parentNode.className = "hidden_element"
  third_cairn.parentNode.className = "hidden_element"

  first_cairn.addEventListener('change', showSecondCairn)
  second_cairn.addEventListener('change', showThirdCairn)

  function showSecondCairn() {
    if (first_cairn.value != "") {
      second_cairn.parentNode.className = "shown_element"
    }
  }

  function showThirdCairn() {
    if (second_cairn.value != "") {
      third_cairn.parentNode.className = "shown_element";
    }
  }
}

// Expand 'create post' form if cairn entered

if (window.location.pathname.includes('/add_post')) {
  let id_image_1 = document.getElementById("id_header_image")
  let id_image_2 = document.getElementById("id_image_2")
  let id_image_3 = document.getElementById("id_image_3")

  id_image_2.parentNode.className = "hidden_element"
  id_image_3.parentNode.className = "hidden_element"

  id_image_1.addEventListener('change', showSecondImage)
  id_image_2.addEventListener('change', showThirdImage)

  function showSecondImage() {
    id_image_2.parentNode.className = "shown_element"
  }

  function showThirdImage() {
    id_image_3.parentNode.className = "shown_element"
  }
}