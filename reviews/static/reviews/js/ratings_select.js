// Hex rating functionality for review form
let hexes = document.getElementsByClassName("rating-hex");

// Loop through hexes
for (let i = 0; i < hexes.length; i++) {
    // Attach click event for rating select
    hexes[i].addEventListener("click", function (e) {
        e.preventDefault(); // Prevent form submission on click

        // Get selected rating
        let selectedHex = parseInt(this.getAttribute("data-hex"));

        // Set the hidden input value
        let ratingField = document.getElementsByClassName("rating-field")[0];
        if (ratingField) {
            ratingField.value = selectedHex;
        }

        // Highlight selected stars and remove highlight from others
        for (let j = 0; j < hexes.length; j++) {
            if (j < selectedHex) {
                hexes[j].classList.add("rating-hex-selected");
            } else {
                hexes[j].classList.remove("rating-hex-selected");
            }
        }
    });

    // Optional: Attach hover effect to preview rating
    hexes[i].addEventListener("mouseover", function () {
        let hoverHex = parseInt(this.getAttribute("data-hex"));
        for (let j = 0; j < hexes.length; j++) {
            if (j < hoverHex) {
                hexes[j].classList.add("rating-hex-hover");
            } else {
                hexes[j].classList.remove("rating-hex-hover");
            }
        }
    });

    // Remove hover effect when mouse leaves
    hexes[i].addEventListener("mouseout", function () {
        for (let j = 0; j < hexes.length; j++) {
            hexes[j].classList.remove("rating-hex-hover");
        }
    });
}
