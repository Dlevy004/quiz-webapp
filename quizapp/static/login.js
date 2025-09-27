/*help icon visibility*/
const helpIcons = document.querySelectorAll('.helpIcon');
helpIcons.forEach(icon => {
  icon.addEventListener('click', () => {
    const tip = icon.nextElementSibling;
    tip.style.display = tip.style.display === 'block' ? 'none' : 'block';
  });
});


/*Login-Signup change*/
const container = document.querySelector('.container'),
      signUp = document.querySelector('.signup-link');

signUp.addEventListener('click', () => {
    container.classList.add('active');
});

/*registration form validation*/
let sigUsernameInput = document.getElementById('username');
let sigEmailInput = document.getElementById('sigEmail');
let sigPasswordInput = document.getElementById('sigPasswordCreate');
let sigConfirmInput = document.getElementById('sigPasswordConfirm');
const sigBtn = document.getElementById('signupBtn');


function isValidEmail(email) {
  let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  return emailPattern.test(email);
}

function isValidPassword(password) {
  let minLength = password.length >= 8;
  let hasLower = /[a-z]/.test(password);
  let hasUpper = /[A-Z]/.test(password);
  let hasNumber = /[0-9]/.test(password);
  let hasSpecial = /[!@#&$%_+\-]/.test(password);
  
  return minLength && hasLower && hasUpper && hasNumber && hasSpecial;
}

function isValidUsername(username) {
  return username.length >= 3 && username.length <= 15;
}

function doPasswordMatch(psw1, psw2) {
  return psw1 === psw2;
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

sigUsernameInput.addEventListener('input', () => {
  markInput(sigUsernameInput, isValidUsername(sigUsernameInput.value));
});

sigEmailInput.addEventListener('input', () => {
  markInput(sigEmailInput, isValidEmail(sigEmailInput.value));
});

sigPasswordInput.addEventListener('input', () => {
  markInput(sigPasswordInput, isValidPassword(sigPasswordInput.value));
});

sigConfirmInput.addEventListener('input', () => {
  markInput(sigConfirmInput, doPasswordMatch(sigPasswordInput.value, sigConfirmInput.value));
});

function allValidInSignup() {
  let errors = [];

  if (!isValidUsername(sigUsernameInput.value)) {
    errors.push("A felhasználónévnek 3-15 karakter hosszúnak kell lennie.");
  }
  if (!isValidEmail(sigEmailInput.value)) {
    errors.push("Érvénytelen email cím.");
  }
  if (!isValidPassword(sigPasswordInput.value)) {
    errors.push("A jelszónak legalább 8 karakter hosszúnak kell lennie, és tartalmaznia kell kisbetűt, nagybetűt, számot és speciális karaktert (!@#&$%_+-).");
  }
  if (!doPasswordMatch(sigPasswordInput.value, sigConfirmInput.value)) {
    errors.push("A két jelszó nem egyezik.");
  }

  if (errors.length > 0) {
    alert("Hiba:\n- " + errors.join("\n- "));
    return false;
  }
  return true;
}

const signUpForm = document.getElementById("signUpForm");

signUpForm.addEventListener("submit", async function(e) {
    e.preventDefault();

    if (!allValidInSignup()) return;

    const formData = new FormData(signUpForm);
    const res = await fetch("/register", {
        method: "POST",
        body: formData
    });
    const data = await res.json();

    alert(data.message);

    if (data.success) {
    container.classList.remove('active');
    signUpForm.reset();
    }
});


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
  if (!allValidInLogin()) {
    e.preventDefault();
    alert("Hiba a bejelentkezés során...");
  }
});
