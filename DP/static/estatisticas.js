// Fazer uma requisição AJAX para obter o JSON da rota
$.ajax({
    url: '/estatisticas', // Substitua pela URL correta da sua rota
    method: 'GET',
    success: function(response) {
      // Manipular o JSON retornado
      var data = JSON.parse(response);
  
      // Atualizar o estilo da página com base nos dados do JSON
      var approvedCandidates = data.candidatos_aprovados;
      var failedCandidates = data.candidatos_reprovados;
      var pendingCandidates = data.candidatos_aguardando;
  
      // Exemplo de manipulação de estilo
      if (approvedCandidates > 0) {
        $('#approved-candidates').addClass('highlight');
      }
  
      if (failedCandidates > 0) {
        $('#failed-candidates').addClass('highlight');
      }
  
      if (pendingCandidates > 0) {
        $('#pending-candidates').addClass('highlight');
      }
    },
    error: function(error) {
      console.log('Erro na requisição:', error);
    }
  });
  