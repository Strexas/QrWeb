document.addEventListener("DOMContentLoaded", function() {
    const messageContainer = document.querySelector('.message-container');
    if (messageContainer) {
        const messages = messageContainer.querySelectorAll('.alert');
        if (messages.length === 0) {
            messageContainer.classList.add('hidden');
        } else {
            setTimeout(() => {
                messageContainer.classList.add('hidden');
            }, 5000); // Adjust the timeout duration as needed
        }
    }
});