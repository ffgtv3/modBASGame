window.addEventListener('scroll', function() {
  var elementsToShow = document.querySelectorAll('.animate-on-scroll');

  for (var i = 0; i < elementsToShow.length; i++) {
    var element = elementsToShow[i];

    if (isElementInViewport(element)) {
      element.classList.add('show');
    }
  }
});

function isElementInViewport(el) {
  var rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
