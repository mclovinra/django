function showLoadingSpinner(event) {
    event.preventDefault();  // Evita la acción predeterminada del evento
    document.getElementById('loading-spinner').style.display = 'block';
    setTimeout(() => {
        window.location.href = event.target.href;
    }, 2000); // Retraso en milisegundos (por ejemplo, 2000ms = 2 segundos)
}
