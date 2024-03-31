// JavaScript code for login functionality
document.addEventListener('DOMContentLoaded', function() {
	// Landlord login form
	document.getElementById("landlord-login").addEventListener("click", function() {
		document.getElementById("landlord-login-form").style.display = "block";
		document.getElementById("tenant-login-form").style.display = "none";
	});

	// Tenant login form
	document.getElementById("tenant-login").addEventListener("click", function() {
		document.getElementById("landlord-login-form").style.display = "none";
		document.getElementById("tenant-login-form").style.display = "block";
	});
});                             
