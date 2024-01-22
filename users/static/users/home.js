const modal = document.querySelector(".my-modal")
const openModal = document.querySelector(".login-button")
const closeModal = document.querySelector(".close-button")

openModal.addEventListener('click', () => {
    modal.showModal();
})

closeModal.addEventListener('click', () => {
    modal.close();
})

