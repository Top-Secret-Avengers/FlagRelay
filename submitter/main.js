async function getData() {
  const url = "";
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error.message);
  }
}

function login() {
    const url = ""
    const headers = new Headers();
    
    headers.append("Content-Type", "application/json");

    const response = await 

    try {
        const response = await fetch(url);
    }
}