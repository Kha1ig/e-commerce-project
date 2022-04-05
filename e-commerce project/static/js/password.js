const buttoneye = document.querySelector<HTMLElement>(".js-button-eye");
const input = document.querySelector<HTMLElement>(".js-input");

buttoneye.addEventListener("click", () => {
    const visible = input.dataset.visible == "true";
    input.dataset.visible = visible ? "false" : "true";
    input.setAttribute("type", visible ? "password1" : "text");
});