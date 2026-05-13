document.addEventListener('DOMContentLoaded', function () {
  var content = document.querySelector('.content');
  if (!content) return;
  var paragraphs = content.querySelectorAll('p');
  if (paragraphs.length >= 4) {
    var adDiv = document.createElement('div');
    adDiv.className = 'ad-wrapper ad-injected';
    adDiv.setAttribute('aria-hidden', 'true');
    paragraphs[3].insertAdjacentElement('afterend', adDiv);
  }
});
