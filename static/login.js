function login() {
  e = document.getElementById("user");
  text = e.value;
  let data = { input: text };
  try {
    // send text to backend as a username
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
      // if backend says name is ok continue
    }).then((response) => {
      if (response.status === 400) {
        alert("Name taken!");
      } else if (response.status === 201) {
        // send user back to home page and create login cookie
        document.cookie = `loggedin=${text};`;
        window.location.href = "/";
      }
    });
  } catch (error) {
    console.error("Fetch error:", error);
  }
}

// Function to check for a specific cookie
function checkCookie(cookieName) {
  return document.cookie
    .split("; ")
    .some((cookie) => cookie.startsWith(`${cookieName}=`));
}

// Check for 'loggedin' cookie do this before any other functions
if (checkCookie("loggedin")) {
  // Redirect to login page
  window.location.href = "/";
}
// should work
document.getElementById("loginButton").onclick = function () {
  login();
};
