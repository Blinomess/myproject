document.addEventListener("DOMContentLoaded", function() {
    const toggleButtons = document.querySelectorAll(".toggle-btn");
    toggleButtons.forEach((btn) => {
        if (btn.nextElementSibling.classList.contains("mess_empty")){
            btn.style.display = "none";
        }
        else{ 
            btn.addEventListener("click", function () {
                const messagesBlock = this.nextElementSibling; // Блок после кнопки
                if (messagesBlock.classList.contains("hidden")) {
                    messagesBlock.classList.remove("hidden"); // Показываем
                    this.querySelector(".arrow").textContent = "Скрыть";
                } else {
                    messagesBlock.classList.add("hidden"); // Скрываем
                    this.querySelector(".arrow").textContent = "Показать";
                }
            });
        }
    });
});