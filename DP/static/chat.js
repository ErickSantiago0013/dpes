// chat.js

window.addEventListener('DOMContentLoaded', function() {
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

