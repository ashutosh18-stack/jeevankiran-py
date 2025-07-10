// Toggle profile dropdown
document.getElementById("profileDropdown").addEventListener("click", () => {
  const dropdown = document.getElementById("dropdownMenu");
  dropdown.style.display = dropdown.style.display === "flex" ? "none" : "flex";
});

// Fetch and animate counters
async function fetchAndAnimateCounters() {
  try {
    // In production, replace with actual backend API endpoint
    const response = await fetch('/api/dashboard-metrics');
    const data = await response.json();

    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
      const key = counter.getAttribute('data-key');
      const target = data[key] || 0;
      let current = 0;

      const update = () => {
        const increment = target / 200;
        if (current < target) {
          current = Math.ceil(current + increment);
          counter.innerText = current.toLocaleString();
          setTimeout(update, 10);
        } else {
          counter.innerText = target.toLocaleString();
        }
      };

      update();
    });

  } catch (err) {
    console.error("Failed to load metrics:", err);
  }
}

fetchAndAnimateCounters();
