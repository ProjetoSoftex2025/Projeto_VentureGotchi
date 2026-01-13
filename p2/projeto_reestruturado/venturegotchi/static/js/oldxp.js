document.addEventListener("DOMContentLoaded", () => {
    const xpFill = document.querySelector(".xp-fill");
    if (!xpFill) return;

    const percent = xpFill.dataset.xp;
    requestAnimationFrame(() => {
        xpFill.style.width = percent + "%";
    });
});