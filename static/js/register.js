const passwordInput = document.getElementById("password-input");

passwordInput.addEventListener("input", () => {
  const password = passwordInput.value;
  const passwordValidation = document.getElementById("password-validation");

  var hasNumber = /\d/.test(password);
  var hasUpper = /[A-Z]/.test(password);
  var hasLower = /[a-z]/.test(password);
  var isLongEnough = password.length >= 6;

  if (hasNumber && hasUpper && hasLower && isLongEnough) {
    passwordValidation.innerHTML = "Password is valid!";
    passwordValidation.style.color = "green";

    // Set the value of the password field to the validated password
    passwordInput.value = password;
  } else {
    passwordValidation.innerHTML = "Password must contain at least one number, one uppercase letter, and be at least 6 characters long.";
    passwordValidation.style.color = "red";
  }
});
