document.addEventListener('DOMContentLoaded', function() {
    var chatButton = document.querySelector('.chat-button');
    var chatModal = document.querySelector('.chat-modal');
    var closeButton = document.querySelector('.close-button');
  
    chatButton.addEventListener('click', function() {
      chatModal.style.display = 'block';
    });
  
    closeButton.addEventListener('click', function() {
      chatModal.style.display = 'none';
    });
  });
  
  function expandCard(card) {
    var expandedCards = document.querySelectorAll('.card.expanded');
  
    if (expandedCards.length > 0) {
      for (var i = 0; i < expandedCards.length; i++) {
        if (expandedCards[i] !== card) {
          expandedCards[i].classList.remove('expanded');
        }
      }
    }
  
    card.classList.toggle('expanded');
  }
  
  $(document).ready(function() {
    var carousel = $('.owl-carousel');
    
    carousel.owlCarousel({
      loop: true,
      margin: 10,
      nav: true,
      dots: false,
      responsive: {
        0: {
          items: 1
        },
        600: {
          items: 3
        },
        1000: {
          items: 5
        }
      }
    });
  
    // Centralizar o carrossel
    var owlStage = carousel.find('.owl-stage');
    var owlStageWidth = owlStage.width();
    var windowWidth = $(window).width();
    var offset = (windowWidth - owlStageWidth) / 2;
    owlStage.css('left', offset + 'px');
  
    // Função de expansão do card
    $('.card').on('click', function() {
      $(this).toggleClass('expanded');
      $('.card').not(this).removeClass('expanded');
    });
  });
  
  function openSettings() {
    // Redirecione para a página de configurações
    window.location.href = '/configuracoes';
  }
  