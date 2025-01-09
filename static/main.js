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

function submitFlag(input) {
  // submit flag and name(in cookie)
  e = document.getElementById("answer");
  text = e.value;
  text = text.toLowerCase().trim();
  if (text == " " || text == "") {
    alert(`Input is empty`);
    return false;
  }

  console.log(text);
  let data = { flag: text };
  try {
    fetch("/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
      credentials: "include",
    }).then((response) => {
      if (response.status == 200) {
        alert("Correct answer!");
        location.reload();
      } else {
        alert("Incorrect!");
      }
    });
  } catch (error) {
    console.error("Error Submitting Flag:", error);
  }

  // need something for flag already scored
  return false;
}
document.getElementById("submit").onclick = function () {
  submitFlag();
};

// function for scoreboard

// function for hints
