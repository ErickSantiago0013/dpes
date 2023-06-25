        // Obtém o modal
        var modal = document.getElementById("beneficiosModal");

        // Obtém o botão que abre o modal
        var btnAbrirModal = document.getElementById("openModalBtn");

        // Obtém o elemento <span> que fecha o modal
        var spanFecharModal = document.getElementsByClassName("close")[0];

        // Abre o modal quando o botão é clicado
        btnAbrirModal.onclick = function() {
            modal.style.display = "block";
        };

        // Fecha o modal quando o usuário clica no <span> (x)
        spanFecharModal.onclick = function() {
            modal.style.display = "none";
        };

        // Fecha o modal quando o usuário clica fora da área do modal
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        };