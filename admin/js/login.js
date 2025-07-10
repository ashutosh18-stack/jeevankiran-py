document.getElementById('loginForm').addEventListener('submit', function (e) {
  e.preventDefault();
  
  const phone = document.getElementById('phone').value;
  const password = document.getElementById('password').value;
  const errorElement = document.getElementById('error');

  // Simple demo user
  const demoUser = {
    phone: "1234567890",
    password: "1234"
  };

  if (phone  === demoUser.phone && password === demoUser.password) {
    localStorage.setItem("isLoggedIn", "true");
    window.location.href = "dashboard.html";
  } else {
    errorElement.textContent = "Invalid phone or password.";
  }
});
