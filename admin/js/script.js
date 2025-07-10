// Toggle profile dropdown
document.getElementById("dropdownToggle").addEventListener("click", () => {
  const menu = document.getElementById("dropdownMenu");
  menu.style.display = menu.style.display === "flex" ? "none" : "flex";
});
