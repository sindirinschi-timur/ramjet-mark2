function startGame() {
const playerName = document.getElementById("player_name").value.trim();
const textElement = document.getElementById("text");



  if (playerName) {
      const message = `Hello, traveller ${playerName}! Get ready for the Adventure!`;
      let index = 0;

      const writeText = () => {
          if (index < message.length) {
              textElement.textContent += message[index];
              index++;
              setTimeout(writeText, 100);
          } else {
              textElement.style.animation = "fadeIn 2s forwards";
              setTimeout(() => { document.getElementById("gameForm").submit(); }, 2000);
          }
      };
      textElement.textContent = '';
      writeText(); 
} else {
alert("Please enter your name before starting the game.");
}
}

function refreshPage() {
  location.reload();
}

function store_species() {
  const speciesChoice = document.getElementById("species").value;
  localStorage.setItem('species', speciesChoice);
}