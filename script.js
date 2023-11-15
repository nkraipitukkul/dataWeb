/*
document.getElementById('searchBtn').addEventListener('click', function (event) {
    event.preventDefault();

    const apiUrl = 'https://official-joke-api.appspot.com/random_joke';

    getDataFromAPI(apiUrl)
      .then(data => {
        // Update the placeholder with the received data
        document.getElementById('apiData').textContent = JSON.stringify(data.setup);
        document.getElementById('myForm').reset();
      });
  });
  function getDataFromAPI(apiUrl) {
// Make a GET request to the API
  return fetch(apiUrl)
    .then(response => {
      // Check if the request was successful (status code 200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Parse the JSON response and return it
      return response.json();
    })
    .catch(error => {
      // Handle any errors that occurred during the fetch
      console.error('Error:', error.message);
    });
}

// Example: Get data from 'https://catfact.ninja/fact'
const apiUrl = 'https://official-joke-api.appspot.com/random_joke';

getDataFromAPI(apiUrl)
  .then(data => {
    // Do something with the data
    console.log('API Data:', data);
});
*/

let dataLoaded = false;

function fetchDataAndDisplayMemes() {
    if (!dataLoaded) {
        const dataContainer = document.getElementById("apiData");

        fetch("https://meme.breakingbranches.tech/api")
            .then(response => response.json())
            .then(data => {
                data.memes.forEach(meme => {
                    console.log(meme);
                    const memeElement = document.createElement("div");

                    const imageElement = document.createElement("img");
                    imageElement.src = meme.url;
                    imageElement.alt = meme.title; 

                    imageElement.style.width = "300px"; 
                    imageElement.style.height = "200px"; 

                    const titleElement = document.createElement("p");
                    titleElement.textContent = `${meme.title}`;
                    titleElement.style.width = "300px";
                    titleElement.style.height = "50px";
                    titleElement.style.display = "flex";
                    titleElement.style.justifyContent = "center";
                    titleElement.style.alignItems = "center";

                    memeElement.appendChild(titleElement);
                    memeElement.appendChild(imageElement);

                    dataContainer.appendChild(memeElement);
                });

                dataLoaded = true;
            })
            .catch(error => {
                console.log(error);
            });
    }
}

document.getElementById('searchBtn').addEventListener('click', function (event) {
    event.preventDefault();
    fetchDataAndDisplayMemes();
});
