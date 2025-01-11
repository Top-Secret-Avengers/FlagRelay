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

// function for calling /data
function getData() {
  // get the json object from /data, and put the results into the scoreboard and hints table
  try {
    fetch("/data", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.status == 200) {
          console.log("data received");
        } else {
          console.log("error getting data");
        }
        return response.json();
      })
      .then((data) => {
        // create the html templates here since data will be out of scope otherwise
        let players = data[0];
        const playerTable = document.getElementById("scoreboard");
        const playerTemplate = document.getElementById("scoreboard-template");

        // for each player in players their name and score should be in the table
        // using in since you cant iterate through the object
        console.log(players);
        for (const elem in players) {
          const newRow = playerTemplate.content.cloneNode(true);
          const cells = newRow.querySelectorAll("td");
          console.log(elem);
          cells[0].textContent = elem;
          cells[1].textContent = players[elem];
          playerTable.appendChild(newRow);
        }
        let hints = data[1];

        const hintsTable = document.getElementById("hints");
        const hintsTemplate = document.getElementById("hints-template");
        // can use for of here since hints is an array
        for (const elem of hints) {
          const newRow = hintsTemplate.content.cloneNode(true);
          const cells = newRow.querySelectorAll("td");

          cells[0].textContent = elem;
          hintsTable.appendChild(newRow);
        }
      });
  } catch (error) {
    console.error("error getting data:", error);
  }
}
// call getData()
getData();
