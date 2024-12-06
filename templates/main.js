// async function getData() {
//   const url = "";
//   try {
//     const response = await fetch(url);

//     if (!response.ok) {
//       throw new Error(`Response status: ${response.status}`);
//     }

//     const json = await response.json();
//     console.log(json);
//   } catch (error) {
//     console.error(error.message);
//   }
// }

loginButton = document.getElementById("loginButton");
loginButton.addEventListener("click", signIn);
// set cookie for user when they log in,
function signIn() {
  let username = document.getElementById("user");
  // user cant be already in backend
  alert(username.innerHTML);
  // document.cookie = `username = ${name}`;

  // TODO:send to backend.
}
