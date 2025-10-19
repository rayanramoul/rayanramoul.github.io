// Function to generate relative line numbers (nvim style)
function updateLineNumbers() {
  const lineNumbersContainer = document.getElementById('line-numbers');
  const contentLines = document.querySelectorAll('.editor-line');
  
  if (lineNumbersContainer && contentLines.length > 0) {
    const totalLines = contentLines.length;
    const currentLine = 4; // The line with the cursor (4th line - title line)
    
    lineNumbersContainer.innerHTML = '';
    
    for (let i = 0; i < totalLines; i++) {
      const lineDiv = document.createElement('div');
      lineDiv.className = 'line-number';
      
      if (i === currentLine - 1) {
        // Current line shows actual line number
        lineDiv.textContent = currentLine;
        lineDiv.classList.add('current');
      } else {
        // Other lines show relative distance
        const distance = Math.abs((i + 1) - currentLine);
        lineDiv.textContent = distance;
      }
      
      lineNumbersContainer.appendChild(lineDiv);
    }
  }
}

document.addEventListener('DOMContentLoaded', function() {
  updateLineNumbers(); // Generate line numbers on page load

  document.addEventListener('keydown', function(event) {
    const statusBar = document.getElementById('status-bar');
    const modeIndicator = document.getElementById('mode-indicator');

    if (event.key === 'i') {
      // Insert mode
      modeIndicator.textContent = '-- INSERT --';
      statusBar.classList.remove('visual-mode');
      statusBar.classList.add('insert-mode');
    }

    if (event.key === 'v') {
      // Visual mode
      modeIndicator.textContent = '-- VISUAL --';
      statusBar.classList.remove('insert-mode');
      statusBar.classList.add('visual-mode');
    }

    if (event.key === 'Escape') {
      // Normal mode
      modeIndicator.textContent = '-- NORMAL --';
      statusBar.classList.remove('insert-mode');
      statusBar.classList.remove('visual-mode');
    }

    if (event.key === ':') {
      // Command mode (visual only)
      modeIndicator.textContent = ':';
      statusBar.classList.remove('insert-mode');
      statusBar.classList.remove('visual-mode');
    }

    // Dynamically re-update line numbers if content changes (if you were to add more functionality)
    updateLineNumbers();
  });
});

