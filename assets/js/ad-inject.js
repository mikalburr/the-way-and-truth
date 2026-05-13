document.addEventListener('DOMContentLoaded', function () {
  // Reading progress bar
  var bar = document.createElement('div');
  bar.className = 'reading-progress';
  document.body.prepend(bar);
  window.addEventListener('scroll', function () {
    var d = document.documentElement;
    var pct = d.scrollTop / (d.scrollHeight - d.clientHeight) * 100;
    bar.style.width = Math.min(pct, 100) + '%';
  }, { passive: true });

  // Mid-article ad slot injection
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
