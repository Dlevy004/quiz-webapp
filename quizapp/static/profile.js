document.addEventListener("DOMContentLoaded", () => {
    const usernameModal = document.getElementById("usernameModal");
    const pictureModal = document.getElementById("pictureModal");
    const passwordModal = document.getElementById("passwordModal");

    const usernameBtn = document.querySelector('button[data-action="username"]');
    const pictureBtn = document.querySelector('button[data-action="picture"]');
    const passwordBtn = document.querySelector('button[data-action="password"]');

    usernameBtn.addEventListener("click", () => {
        usernameModal.classList.remove("hidden");
    });
    pictureBtn.addEventListener("click", () => {
        pictureModal.classList.remove("hidden");
    });
    passwordBtn.addEventListener("click", () => {
        passwordModal.classList.remove("hidden");
    });

    document.querySelectorAll(".modal").forEach(modal => {
        modal.querySelector(".close").addEventListener("click", () => {
            modal.classList.add("hidden");
        });
        modal.querySelector(".cancel-btn").addEventListener("click", () => {
            modal.classList.add("hidden");
        });
    });

    const newPassword = document.getElementById("newPassword");
    const confirmPassword = document.getElementById("confirmPassword");

    function validatePassword(password) {
        const minLength = /.{8,}/;
        const upper = /[A-Z]/;
        const lower = /[a-z]/;
        const number = /[0-9]/;
        const special = /[!@#\$%\^&\*\+\-]/;

        return (
            minLength.test(password) &&
            upper.test(password) &&
            lower.test(password) &&
            number.test(password) &&
            special.test(password)
        );
    }

    newPassword.addEventListener("input", () => {
        if (validatePassword(newPassword.value)) {
            newPassword.classList.add("valid");
            newPassword.classList.remove("invalid");
        } else {
            newPassword.classList.add("invalid");
            newPassword.classList.remove("valid");
        }
    });

    confirmPassword.addEventListener("input", () => {
        if (confirmPassword.value === newPassword.value && validatePassword(newPassword.value)) {
            confirmPassword.classList.add("valid");
            confirmPassword.classList.remove("invalid");
        } else {
            confirmPassword.classList.add("invalid");
            confirmPassword.classList.remove("valid");
        }
    });
});

const handleForm = (formId, url) => {
    const form = document.getElementById(formId);
    form.addEventListener("submit", async e => {
        e.preventDefault();
        const res = await fetch(url, { method: "POST", body: new FormData(form) });
        const data = await res.json();
        alert(data.message);
        if (data.success) window.location.reload();
    });
};

handleForm("updateUsernameForm", "/update_username");
handleForm("updatePictureForm", "/update_picture");
