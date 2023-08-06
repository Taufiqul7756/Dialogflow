// Dialogflow API access token
// require("dotenv").config(); // Load the environment variables

const projectId = "";
const accessToken = "";
// const projectId = process.env.PROJECT_ID;
// const accessToken = process.env.ACCESS_TOKEN;
// Function to detect intent and get response from Dialogflow
async function detectIntent(query) {
  try {
    const response = await fetch(
      `https://dialogflow.googleapis.com/v2/projects/${projectId}/agent/sessions/test-session:detectIntent`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          queryInput: {
            text: {
              text: query,
              languageCode: "en",
            },
          },
        }),
      }
    );

    if (!response.ok) {
      throw new Error("Failed to detect intent");
    }

    const result = await response.json();
    console.log(result);
    return result;
  } catch (error) {
    console.error("Error detecting intent:", error);
  }
}

// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault();
  const queryInput = document.getElementById("query-input");
  const query = queryInput.value;

  detectIntent(query).then((result) => {
    const responseContainer = document.getElementById("response-container");
    responseContainer.innerHTML = `
        <p> <b>Query: </b> ${result.queryResult.queryText}</p>
        <p> <b>Response: </b> ${result.queryResult.fulfillmentText}</p>
        <p> <b>Detected Intent: </b> ${result.queryResult.intent.displayName}</p>
      `;
  });

  queryInput.value = "";
}

// Attach form submission event listener
const form = document.getElementById("query-form");
form.addEventListener("submit", handleSubmit);
