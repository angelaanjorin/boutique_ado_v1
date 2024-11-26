let currentIndex = 0;
const texts = document.querySelectorAll('.ticker-text');

setInterval(() => {
  texts.forEach((text, index) => {
    text.style.display = index === currentIndex ? 'inline-block' : 'none';
  });
  currentIndex = (currentIndex + 1) % texts.length;
}, 4500); 
