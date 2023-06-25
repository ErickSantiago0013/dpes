$(document).ready(function() {
    $('#candidatos-table').DataTable();

    $(document).on('click', '.candidate-details-icon', function() {
        var id = $(this).data('id');

        $.ajax({
            url: '/get-candidate-details',
            method: 'POST',
            data: { id: id },
            success: function(response) {
                var details = response;

                // Atualizar o conteúdo do modal com os detalhes do funcionário
                var modalBody = $('#employeeDetailsModalBody');
                modalBody.empty();

                var fieldNames = ['Nome', 'Idade', 'Sexo', 'Estado Civil', 'Quantidade de Filhos', 'Idade', 'Escolaridade', 'Área de Formação', 'Entidade', 'Logradouro', 'Bairro', 'Cidade', 'UF', 'Filial', 'Cargo', 'Admissão', 'Praça', 'V.T', 'Entrevistador', 'Data da Entrevista', 'Status', 'Grau de Anotação', 'Anotação'];

                for (var i = 0; i < fieldNames.length; i++) {
                    var fieldName = fieldNames[i];
                    var fieldValue = details[i + 1];
                    modalBody.append('<p><strong>' + fieldName + ':</strong> ' + fieldValue + '</p>');
                }

                // Exibir o modal
                $('#employeeDetailsModal').modal('show');
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    function loadEmployeeDetails(employeeId) {
        // ... código para obter os dados do funcionário com o ID fornecido ...
        // Supondo que você tenha os dados do funcionário em uma variável chamada "employee"

        // Preencher os campos do modal com os dados do funcionário em modo de edição
        $('#employeeNameInput').val(employee.name);
        $('#employeeCPFInput').val(employee.cpf);
        $('#employeeCEPInput').val(employee.cep);
        $('#employeeLogradouroInput').val(employee.logradouro);
        $('#employeeNotesInput').val(employee.notes);

        // Abrir o modal
        $('#employeeEditModal').modal('show');
    }

    $(document).on('click', '.employee-details-icon, .edit-employee-button', function() {
        var employeeId = $(this).data('id');
        loadEmployeeDetails(employeeId);
    });

    $('#editEmployeeButton').on('click', function() {
        // Aqui você pode adicionar a lógica para editar os dados do funcionário
        // e atualizar o banco de dados
        // Por exemplo, abrir um modal de edição com campos de entrada
        $('#employeeEditModal').modal('show');
    });

    $('#saveEmployeeButton').on('click', function() {
        // Aqui você pode adicionar a lógica para salvar as alterações do funcionário
        // e atualizar o banco de dados
        var editedEmployee = {
            name: $('#employeeNameInput').val(),
            cpf: $('#employeeCPFInput').val(),
            cep: $('#employeeCEPInput').val(),
            logradouro: $('#employeeLogradouroInput').val(),
            notes: $('#employeeNotesInput').val()
        };
        console.log('Funcionário editado:', editedEmployee);

        // Fechar o modal de edição
        $('#employeeEditModal').modal('hide');
    });

    $('#exportEmployeeButton').on('click', function() {
        // Exportar dados do funcionário para um arquivo CSV
        exportToCSV();
    });

    $('#printEmployeeButton').on('click', function() {
        // Imprimir os detalhes do funcionário
        printEmployeeDetails();
    });

    function exportToCSV() {
        // Obter os dados do funcionário
        var employee = getEmployeeData();

        // Criar uma string CSV com os dados do funcionário
        var csvContent = "Nome,CPF,CEP,Logradouro,Notas\n";
        csvContent += employee.name + "," + employee.cpf + "," + employee.cep + "," + employee.logradouro + "," + employee.notes + "\n";

        // Criar um elemento de link temporário para download
        var link = document.createElement("a");
        link.setAttribute("href", "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent));
        link.setAttribute("download", "employee_details.csv");
        document.body.appendChild(link);

        // Simular um clique no link para iniciar o download
        link.click();

        // Remover o elemento de link temporário
        document.body.removeChild(link);
    }

    function printEmployeeDetails() {
        // Obter os dados do funcionário
        var employee = getEmployeeData();

        // Criar uma janela pop-up para imprimir os detalhes do funcionário
        var printWindow = window.open("", "_blank", "toolbar=yes,scrollbars=yes,resizable=yes,top=100,left=100,width=800,height=600");

        // Construir o conteúdo HTML para impressão
        var htmlContent = "<html><head><title>Detalhes do Funcionário</title>";
        htmlContent += "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>";
        htmlContent += "</head><body>";
        htmlContent += "<div class='container'><h3>Detalhes do Funcionário</h3>";

        var fieldNames = ['Nome', 'CPF', 'CEP', 'Logradouro', 'Notas'];

        for (var i = 0; i < fieldNames.length; i++) {
            var fieldName = fieldNames[i];
            var fieldValue = employee[fieldName.toLowerCase()];
            htmlContent += "<p><strong>" + fieldName + ":</strong> " + fieldValue + "</p>";
        }

        htmlContent += "</div>";
        htmlContent += "<script>window.onload = function() { window.print(); window.onafterprint = function() { window.close(); } }</script>";
        htmlContent += "</body></html>";

        // Escrever o conteúdo HTML na janela pop-up
        printWindow.document.open();
        printWindow.document.write(htmlContent);
        printWindow.document.close();
    }

    function getEmployeeData() {
        // Obter os dados do funcionário do modal
        var employee = {
            name: $('#employeeName').text(),
            cpf: $('#employeeCPF').text(),
            cep: $('#employeeCEP').text(),
            logradouro: $('#employeeLogradouro').text(),
            notes: $('#employeeNotes').text()
        };

        return employee;
    }
});
