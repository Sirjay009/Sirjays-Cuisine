const reservationForm = document.getElementById("reservationForm");
const editButtons = document.querySelectorAll(".btn-edit");

for (let button of editButtons){
    button.addEventListener("click", (e) => {
        let reservationId = e.target.getAttribute("data-reservation_id");
        reservationForm.setAttribute("action", `reservation_edit/${reservationId}`);
    });
}