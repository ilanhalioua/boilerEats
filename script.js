function scrollToDiv(divId) {
  var element = document.getElementById(divId);
  element.scrollIntoView({ behavior: 'smooth' });
}