$(document).ready(function() {
    // Adiciona o evento de clique nos cabeçalhos das mensagens
    $('.card-header').click(function() {
      // Obtém o elemento de conteúdo da mensagem correspondente
      var content = $(this).next('.collapse');
  
      // Verifica se o conteúdo está atualmente visível
      if (content.hasClass('show')) {
        // Se estiver visível, remove a classe 'show' para ocultar o conteúdo com uma animação
        content.removeClass('show');
      } else {
        // Se estiver oculto, adiciona a classe 'show' para mostrar o conteúdo com uma animação
        content.addClass('show');
      }
    });
  });
  