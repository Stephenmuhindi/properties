function loadLandlordProperties() {
    // Replace with actual API call or database query to get landlord properties
    const properties = [
        { id: 1, address: '123 Main St', city: 'Anytown', state: 'CA', zip: '12345' },
        { id: 2, address: '456 Oak St', city: 'Anytown', state: 'CA', zip: '12345' },
    ];

    const propertyList = document.getElementById('property-list');
    propertyList.innerHTML = '';

    properties.forEach((property) => {
        const listItem = document.createElement('li');
        listItem.textContent = `${property.address}, ${property.city}, ${property.state} ${property.zip}`;
        propertyList.appendChild(listItem);
    });
}

function loadTenantProperties() {
    // Replace with actual API call or database query to get tenant properties
    const properties = [
        { id: 1, address: '789 Elm St', city: 'Anytown', state: 'CA', zip: '12345' },
        { id: 2, address: '1011 Pine St', city: 'Anytown', state: 'CA', zip: '12345' },
    ];

    const propertyList = document.getElementById('property-list');
    propertyList.innerHTML = '';

    properties.forEach((property) => {
        const listItem = document.createElement('li');listItem.textContent = `${property.address}, ${property.city}, ${property.state} ${property.zip}`;
        propertyList.appendChild(listItem);
    });
}
