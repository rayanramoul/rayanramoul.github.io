// Function to generate relative line numbers
function updateLineNumbers() {
}

document.addEventListener('DOMContentLoaded', function() {
  updateLineNumbers(); // Generate line numbers on page load

  document.addEventListener('keydown', function(event) {
    const statusBar = document.getElementById('status-bar');

    if (event.key === 'i') {
      // Insert mode
      statusBar.textContent = '-- INSERT --';
    }

    if (event.key === 'Escape') {
      // Normal mode
      statusBar.textContent = '-- NORMAL --';
    }

    if (event.key === ':') {
      // Command mode (visual only)
      statusBar.textContent = ':';
    }

    // Dynamically re-update line numbers if content changes (if you were to add more functionality)
    updateLineNumbers();
  });
});

