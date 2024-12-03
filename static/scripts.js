// Submit Form: POST method
async function submitForm(event) {
    event.preventDefault();

    const form = event.target;

    const data = {
        id: form.elements["id"].value.trim(),
        int1: parseInt(form.elements["int1"].value.trim(), 10),
        int2: parseInt(form.elements["int2"].value.trim(), 10),
    };

    console.log("Data being sent to the server:", data);

    if (!data.id) {
        alert("Identifier is required.");
        return;
    }
    if (isNaN(data.int1) || isNaN(data.int2)) {
        alert("Please enter valid numbers for First Input and Second Input.");
        return;
    }

    try {
        const response = await fetch("/api/user_inputs/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            alert("Data submitted successfully: " + JSON.stringify(result));
        } else {
            const errorMessage = await response.text();
            alert("Failed to submit data: " + errorMessage);
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}

// Fetch Data by ID: GET method
async function getFormData(event) {
    event.preventDefault();

    const form = event.target;
    const id = form.elements["id"].value.trim();

    if (!id) {
        alert("Please enter an ID to fetch data.");
        return;
    }

    try {
        const response = await fetch(`/api/user_inputs/${id}`);

        if (response.ok) {
            const data = await response.json();
            alert("Fetched Data: " + JSON.stringify(data));
        } else {
            const errorMessage = await response.text();
            alert("Failed to fetch data: " + errorMessage);
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}

// Fetch All Data: GET method with pagination
async function getAllData(event) {
    event.preventDefault();

    const form = event.target;
    const offset = parseInt(form.elements["offset"].value.trim(), 10);
    const limit = parseInt(form.elements["limit"].value.trim(), 10);

    if (isNaN(offset) || offset < 0) {
        alert("Please enter a valid offset (page number).");
        return;
    }
    if (isNaN(limit) || limit <= 0) {
        alert("Please enter a valid limit (number of items per page).");
        return;
    }

    try {
        const response = await fetch(`/api/all_user_inputs/?offset=${offset}&limit=${limit}`);

        if (response.ok) {
            const data = await response.json();
            alert("Fetched Data: " + JSON.stringify(data));
        } else {
            const errorMessage = await response.text();
            alert("Failed to fetch data: " + errorMessage);
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}
