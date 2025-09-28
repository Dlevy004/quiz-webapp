const logoutBtn = document.querySelector('.logout-btn');

logoutBtn.addEventListener('click', () => {
    window.location.href = '/logout';
});

/*Cookie Panel*/
const cookiePanel = document.querySelector('.cookie-panel');
const acceptBtn = document.querySelector('#acceptBtn');
const rejectBtn = document.querySelector('#rejectBtn');

function hasAcceptedCookies() {
  return document.cookie.split(';').some(cookie => cookie.trim().startsWith('cookie_consent'));
}

window.addEventListener('load', () => {
  if (!hasAcceptedCookies()) {
    cookiePanel.classList.add("show");
  }
});

acceptBtn.addEventListener('click', () => {
  document.cookie = "cookie_consent=Quizzy; max-age=" + 60 * 60 * 24 * 30;
  cookiePanel.classList.remove("show");
});

rejectBtn.addEventListener('click', () => {
  cookiePanel.classList.remove("show");
});