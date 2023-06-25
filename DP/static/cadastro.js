document.getElementById("quantidade_filhos").addEventListener("change", function() {
    var quantidadeFilhos = parseInt(this.value);
    var filhosDetails = document.getElementById("filhos_details");
    
    // Remove todos os campos de idade dos filhos existentes
    while (filhosDetails.firstChild) {
        filhosDetails.removeChild(filhosDetails.firstChild);
    }
    
    // Adiciona novos campos de idade dos filhos com base na quantidade selecionada
    for (var i = 1; i <= quantidadeFilhos; i++) {
        var label = document.createElement("label");
        label.setAttribute("for", "idade_filho_" + i);
        label.textContent = "Idade do filho " + i + ":";
        
        var input = document.createElement("input");
        input.setAttribute("type", "number");
        input.setAttribute("id", "idade_filho_" + i);
        input.setAttribute("name", "idade_filho_" + i);
        input.setAttribute("min", "0");
        input.setAttribute("max", "18");
        input.required = true;
        
        filhosDetails.appendChild(label);
        filhosDetails.appendChild(input);
        filhosDetails.appendChild(document.createElement("br"));
    }
});
