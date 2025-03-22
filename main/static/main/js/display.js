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
    openYandexMapButton.addEventListener("click", function () {
        let latitude = this.getAttribute("data-latitude").replace(",", ".");
        let longitude = this.getAttribute("data-longitude").replace(",", ".");

        if (!isNaN(latitude) && !isNaN(longitude) && latitude !== 0 && longitude !== 0) {
            const yandexMapUrl = `https://yandex.ru/maps/?ll=${longitude},${latitude}&z=17&mode=routes&rtext=54.913570%2C37.371710~${latitude}%2C${longitude}&rtt=mt`;
            window.open(yandexMapUrl, '_blank');
        } else {
            alert("Ошибка: неверные координаты! " + latitude + ", " + longitude);
        }
    });
});