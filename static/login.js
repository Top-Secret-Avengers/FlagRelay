function login() {
  e = document.getElementById("user");
  text = e.value;
  console.log(text);
  let data = { input: text };
  try {
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then((response) => {
      if (response.status === 400) {
        alert("Name taken!");
      } else if (response.status === 201) {
        window.location.href = "/";
      }
    });
  } catch (error) {
    console.error("Fetch error:", error);
  }
  console.log("pressed");
  // send text to backend as a username
  // if backend says name is ok continue
  // create loggedin cookie
  // send user back to home page
}
// should work
document.getElementById("loginButton").onclick = function () {
  login();
};
