const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const form = document.getElementById("form");
const input = document.getElementById("input");

const socket = new WebSocket(`ws://${window.location.host}/ws`);

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = `message ${type}`;
    div.textContent = text;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
    statusEl.textContent = "Connected";
};

socket.onclose = () => {
    statusEl.textContent = "Disconnected";
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (text === "") return;
    socket.send(text);
    addMessage(text, "sent");
    input.value = "";
});
