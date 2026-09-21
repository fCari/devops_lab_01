async function cargarInfo() {
  const errorBox = document.getElementById("error");
  errorBox.hidden = true;

  try {
    const response = await fetch("/api/info/");
    if (!response.ok) {
      throw new Error("La API respondió con estado " + response.status);
    }
    const data = await response.json();

    document.getElementById("team").textContent = data.team;
    document.getElementById("web_server").textContent = data.web_server;
    document.getElementById("stack").textContent = data.stack;
    document.getElementById("server_time").textContent = data.server_time;
    document.getElementById("client_ip").textContent = data.client_ip;

    const list = document.getElementById("members");
    list.innerHTML = "";
    data.members.forEach((name) => {
      const li = document.createElement("li");
      li.textContent = name;
      list.appendChild(li);
    });
  } catch (err) {
    errorBox.textContent = "No se pudo cargar la API: " + err.message;
    errorBox.hidden = false;
  }
}

document.getElementById("refresh").addEventListener("click", cargarInfo);
cargarInfo();