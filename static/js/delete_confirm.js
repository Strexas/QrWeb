// static/js/main.js
function confirmDeleteAccount() {
    if (confirm("Are you sure you want to delete your account?")) {
        document.getElementById('delete-account-form').submit();
    }
}
