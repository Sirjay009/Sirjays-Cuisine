document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".btn-edit"); // Select all edit buttons

    editButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            // Get reservation ID from data attribute
            const reservationId = event.target.getAttribute("data-reservation_id");

            // Construct the Edit URL (update 'reservation_edit' to match your URL pattern)
            const editUrl = `/reservation/edit/${reservationId}/`;

            // Redirect the user to the Edit URL
            window.location.href = editUrl;
        });
    });
});