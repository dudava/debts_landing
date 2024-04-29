const cases = document.querySelectorAll(".cases-won-card");
const prevButton = document.querySelector(".slider-button-prev");
const nextButton = document.querySelector(".slider-button-next");
let caseIndex = 0

function changeCase(index) {
    if (index < 0) {
        index = cases.length - 1;
    }
    else if (index >= cases.length) {
        index = 0;
    }
    cases[caseIndex].classList.remove("active");
    cases[index].classList.add("active");
    caseIndex = index;
}    
prevButton.addEventListener("click", () => {
    changeCase(caseIndex - 1);
})
nextButton.addEventListener("click", () => {
    changeCase(caseIndex + 1);
})
changeCase(caseIndex);

