(() => {
  "use strict";

  const create = (tagName, className = "", text = "") => {
    const node = document.createElement(tagName);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  };

  const button = create("button", "provifact-share", "Share");
  button.type = "button";
  button.setAttribute("aria-label", "Share this Provifact view");
  button.title = "Share this view";
  const icon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  icon.setAttribute("viewBox", "0 0 24 24");
  icon.setAttribute("aria-hidden", "true");
  icon.innerHTML =
    '<path d="M18 8a3 3 0 1 0-2.83-4H15a3 3 0 0 0 .52 1.69L8.91 9.08A3 3 0 0 0 7 8.4a3 3 0 1 0 1.91 5.31l6.61 3.39A3 3 0 0 0 15 18.8a3 3 0 1 0 .91-2.14L9.3 13.27c.18-.55.18-1.14 0-1.69l6.61-3.39c.55.51 1.28.81 2.09.81Z" fill="currentColor"/>';
  button.prepend(icon);
  const status = create("span", "provifact-share-status");
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  document.body.append(button, status);

  const setStatus = (message) => {
    status.textContent = message;
    window.setTimeout(() => {
      status.textContent = "";
    }, 2400);
  };

  button.addEventListener("click", async () => {
    const data = {
      title: document.title,
      text: "Provifact — From approved change to audit-ready proof.",
      url: window.location.href,
    };
    try {
      if (typeof navigator.share === "function") {
        await navigator.share(data);
        setStatus("Share sheet opened");
        return;
      }
      await navigator.clipboard.writeText(data.url);
      setStatus("Link copied");
    } catch (error) {
      if (error instanceof DOMException && error.name === "AbortError") return;
      setStatus("Use the address bar to copy this link");
    }
  });
})();
