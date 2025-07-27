document.addEventListener('DOMContentLoaded', function() {
    // Function to create and append items to a list
    function populateList(endpoint, listId, renderItem) {
        fetch(`/api/${endpoint}`)
            .then(response => response.json())
            .then(data => {
                const listElement = document.getElementById(listId);
                listElement.innerHTML = ''; // Clear existing content
                data.forEach(item => {
                    listElement.appendChild(renderItem(item));
                });
            });
    }

    // Render functions for each type of item
    function renderCity(item) {
        const div = document.createElement('div');
        div.className = 'list-item';
        div.innerHTML = `<h3>${item.name_ar}</h3><p>السكان: ${item.population}</p>`;
        return div;
    }

    function renderService(item) {
        const div = document.createElement('div');
        div.className = 'list-item';
        div.innerHTML = `<h3>${item.service_name_ar}</h3><p>${item.description_ar}</p><p>للتواصل: ${item.contact_info}</p>`;
        return div;
    }

    function renderJobSeeker(item) {
        const div = document.createElement('div');
        div.className = 'list-item';
        div.innerHTML = `<h3>${item.name_ar}</h3><p>المهارات: ${item.skills_ar}</p><p>للتواصل: ${item.contact_info}</p>`;
        return div;
    }

    function renderJobVacancy(item) {
        const div = document.createElement('div');
        div.className = 'list-item';
        div.innerHTML = `<h3>${item.title_ar}</h3><p>${item.description_ar}</p><p>للتواصل: ${item.contact_info}</p>`;
        return div;
    }

    function renderProduct(item) {
        const div = document.createElement('div');
        div.className = 'list-item';
        div.innerHTML = `<h3>${item.product_name_ar}</h3><p>${item.description_ar}</p><p>السعر: ${item.price}</p><p>للتواصل: ${item.contact_info}</p>`;
        return div;
    }

    // Populate all lists
    populateList('cities', 'cities-list', renderCity);
    populateList('services', 'services-list', renderService);
    populateList('job_seekers', 'job-seekers-list', renderJobSeeker);
    populateList('job_vacancies', 'job-vacancies-list', renderJobVacancy);
    populateList('products', 'products-list', renderProduct);
});
