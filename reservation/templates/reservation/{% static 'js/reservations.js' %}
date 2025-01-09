const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteButtons = document.getElementsByClassName('btn-delete');
const deleteConfirm = document.getElementById('deleteConfirm');

for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        let reservationId = e.target.dataset.reservationId;

        deleteConfirm.href = `/reservation/${reservationId}/delete/`;
        deleteModal.show();
    });
}