/*Login-Signup change*/
const container = document.querySelector('.container'),
      signUp = document.querySelector('.signup-link');

signUp.addEventListener('click', () => {
    container.classList.add('active');
});

function isValidEmail(email) {
  let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  return emailPattern.test(email);
}

function markInput(input, isValid) {
  if (isValid) {
    input.classList.remove('error');
    input.classList.add('success');
  } else {
    input.classList.remove('success');
    input.classList.add('error');
  }
}

/*login form validation*/
let logEmailInput = document.getElementById('logEmail');
let logPasswordInput = document.getElementById('logPassword');
let loginBtn = document.getElementById('loginBtn');

logEmailInput.addEventListener('input', () => {
  markInput(logEmailInput, isValidEmail(logEmailInput.value));
});

logPasswordInput.addEventListener('input', () => {
  markInput(logPasswordInput, logPasswordInput.value.length > 0);
});

function allValidInLogin() {
  let errors = [];

  if (!isValidEmail(logEmailInput.value)) {
    errors.push("Érvénytelen email cím.");
  }
  if (logPasswordInput.value.trim() === "") {
    errors.push("A jelszót kötelező megadni.");
  }

  if (errors.length > 0) {
    alert("Hiba:\n- " + errors.join("\n- "));
    return false;
  }
  return true;
}

loginBtn.addEventListener('click', (e) => {
  e.preventDefault();

  if (allValidInLogin()) {
    window.location.href = "index.html";
  } else {
    alert("Hiba a bejelentkezés során. Kérjük, ellenőrizze a megadott adatokat.");
  }
});