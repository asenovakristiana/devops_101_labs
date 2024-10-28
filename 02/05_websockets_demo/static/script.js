// Opening WebSocket connection to the server
let ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function(event) {
    let messagesDiv = document.getElementById("messages");
    let message = document.createElement("div");
    message.textContent = event.data;
    messagesDiv.appendChild(message);
};

// Handling WebSocket errors
ws.onerror = function(event) {
    console.error("WebSocket error observed:", event);
};