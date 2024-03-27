const loginForm = document.getElementById('login-form');
const propertiesContainer = document.getElementById('properties-container');

loginForm.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get form data
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // Check if user exists and password is correct
    if (username === 'landlord' && password === 'password') {
        // Landlord
        loginForm.style.display = 'none';
        propertiesContainer.style.display = 'block';
        loadLandlordProperties(); // Load landlord properties
    } else if (username === 'tenant' && password === 'password') {
        // Tenant
        loginForm.style.display = 'none';
        propertiesContainer.style.display = 'block';
        loadTenantProperties(); // Load tenant properties
    } else {
        alert('Invalid username or password');
    }
});
