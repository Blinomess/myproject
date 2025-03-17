document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("modal");
    const openModal = document.getElementById("openModal");
    const closeModal = document.getElementById("closeModal");

    openModal.onclick = function() {
        modal.classList.add("show");
    }

    closeModal.onclick = function() {
        modal.classList.remove("show");
    }

    const toggleButtons = document.querySelectorAll(".toggle-btn");

    toggleButtons.forEach((btn) => {
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
    });

    const openYandexMapButton = document.getElementById("openYandexMap");

    openYandexMapButton.addEventListener("click", function() {
        const latitude = parseFloat("{{ message.latitude }}");
        const longitude = parseFloat("{{ message.longitude }}");
        const yandexMapUrl = `https://yandex.ru/maps/?ll=${longitude}%2С${latitude}&z=14`;
        window.open(yandexMapUrl, '_blank');
    });
});