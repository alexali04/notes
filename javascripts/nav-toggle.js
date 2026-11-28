document$.subscribe(function () {
  if (document.querySelector(".nav-toggle")) return;

  const btn = document.createElement("button");
  btn.className = "nav-toggle";
  const sync = () => {
    const hidden = localStorage.getItem("navHidden") === "1";
    document.body.classList.toggle("nav-hidden", hidden);
    btn.textContent = hidden ? "›" : "‹";
  };
  btn.onclick = () => {
    const hidden = localStorage.getItem("navHidden") === "1";
    localStorage.setItem("navHidden", hidden ? "0" : "1");
    sync();
  };
  document.body.appendChild(btn);
  sync();
});