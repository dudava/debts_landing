const feedbackModalButtons = document.querySelectorAll(".feedback-button");
const feedbackModal = document.querySelector('.feedback-modal');
const feedbackCloseButton = document.querySelector('.feedback-close-button');

feedbackModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        feedbackModal.style.display = 'block';
    })
});
feedbackCloseButton.addEventListener('click', () => {
    feedbackModal.style.display = 'none';
}) 
window.addEventListener('click', (e) => {
    if (e.target == feedbackModal) {
        feedbackModal.style.display = 'none';
    }
})
document.addEventListener('keydown', (e) => {
    if (e.code == 'Escape') {
        feedbackModal.style.display = 'none';
    }
})