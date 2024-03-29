class InfoPopup {
    constructor(querySelector, visibilityClass) {
        this.element = document.querySelector(querySelector);
        this.hidePopup = () => {
            if (this.element) {
                this.element.classList.remove(visibilityClass);
            }
        }
        setTimeout(() => { this.hidePopup({}) }, 5000);
    } 
}