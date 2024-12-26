// Function to check for a specific cookie
function checkCookie(cookieName) {
  return document.cookie
    .split("; ")
    .some((cookie) => cookie.startsWith(`${cookieName}=`));
}

// Check for 'loggedin' cookie do this before any other functions
if (!checkCookie("loggedin")) {
  // Redirect to login page
  window.location.href = "/login";
}
