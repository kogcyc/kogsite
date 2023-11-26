
// The code under this will run after the page is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  
  // Add event listener to the logo image
  document.getElementById('logoBtn').addEventListener('click', function() {
    // Navigate to "index.html" when the logo is clicked
    window.location.href = 'index.html';
  });
  
  // Add event listener to the hamburger image
  document.getElementById('hamburgerBtn').addEventListener('click', function() {
    // Navigate to "menu.html" when the hamburger is clicked
    window.location.href = 'menu.html';
  });

});
