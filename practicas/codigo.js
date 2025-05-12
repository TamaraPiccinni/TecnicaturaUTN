// Genera un número aleatorio entre min y max, incluyendo ambos
function aleatorio(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Traduce el número de jugada a texto con emoji
function eleccion(jugada) {
  switch (parseInt(jugada)) {
    case 1: return "Piedra 🥌";
    case 2: return "Papel 📄";
    case 3: return "Tijera ✂️";
    default: return "Elección inválida";
  }
}

// Variables para contar triunfos y derrotas
let triunfos = 0;
let perdidas = 0;

// Función principal que se ejecuta al hacer clic en una opción
function jugar(jugador) {
  const pc = aleatorio(1, 3); // PC elige aleatoriamente del 1 al 3

  // Muestra las elecciones de ambos
  let mensaje = `Tú eliges: ${eleccion(jugador)}<br>PC elige: ${eleccion(pc)}<br>`;

  // Lógica del juego: empate, gana jugador, o gana PC
  if (jugador === pc) {
    mensaje += "🤝 ¡Empate!";
  } else if (
    (jugador === 1 && pc === 3) ||
    (jugador === 2 && pc === 1) ||
    (jugador === 3 && pc === 2)
  ) {
    mensaje += "🎉 ¡Ganaste!";
    triunfos++;
  } else {
    mensaje += "💀 Perdiste.";
    perdidas++;
  }

  // Muestra resultado parcial
  document.getElementById("resultado").innerHTML = mensaje;
  document.getElementById("marcador").innerText = `Triunfos: ${triunfos} | Derrotas: ${perdidas}`;

  // Si alguno gana 3 veces, termina la partida
  if (triunfos >= 3) {
    document.getElementById("resultado").innerHTML += "<br><strong>🏆 ¡Ganaste la partida!</strong>";
    desactivarBotones();
  } else if (perdidas >= 3) {
    document.getElementById("resultado").innerHTML += "<br><strong>😢 Perdiste la partida.</strong>";
    desactivarBotones();
  }
}

// Reinicia los contadores y la interfaz
function reiniciarJuego() {
  triunfos = 0;
  perdidas = 0;
  document.getElementById("resultado").innerHTML = "";
  document.getElementById("marcador").innerText = "Triunfos: 0 | Derrotas: 0";
  activarBotones();
}

// Desactiva los botones de jugada (cuando termina la partida)
function desactivarBotones() {
  document.querySelectorAll(".buttons button").forEach(btn => btn.disabled = true);
}

// Vuelve a habilitar los botones (cuando se reinicia)
function activarBotones() {
  document.querySelectorAll(".buttons button").forEach(btn => btn.disabled = false);
}
