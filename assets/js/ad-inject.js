// DEFERRED: mid-article ad injection — enable when site.adsense.enabled flips to true.
// When active: if the .post-content div has 4+ <p> tags, inject an ad placeholder after paragraph 4.
//
// document.addEventListener('DOMContentLoaded', function () {
//   var content = document.querySelector('.post-content');
//   if (!content) return;
//   var paragraphs = content.querySelectorAll('p');
//   if (paragraphs.length >= 4) {
//     var adDiv = document.createElement('div');
//     adDiv.className = 'ad-wrapper ad-injected';
//     adDiv.setAttribute('aria-hidden', 'true');
//     (window.adsbygoogle = window.adsbygoogle || []).push({});
//     paragraphs[3].insertAdjacentElement('afterend', adDiv);
//   }
// });
