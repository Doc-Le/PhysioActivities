const $resourceField = $('#resourceField');
const $serviceField = $('#serviceField')
const $dateField = $('#dateField');
const $timeField = $('#timeField')
const $checkoutButton = $('#checkout-button');

$serviceField.prop('disabled', true);
$timeField.prop('disabled', true);


function checkoutStripe() {
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    const $serviceSelect = $('#serviceField');
    const serviceId = $serviceSelect.val();
    // save appointment model backend
    // populate available services per selected resource via JS call from UI
    // populate available times per selected date via JS call from UI
    const appointment = {
        firstName: $('#firstNameField').val(),
        lastName: $('#lastNameField').val(),
        gender: $('#genderField').val(),
        phone: $('#phoneField').val(),
        email: $('#emailField').val(),
        resourceId: $('#resourceField').val(),
        locationId: $('#locationField').val(),
        serviceId: $('#serviceField').val(),
        dateId: $('#dateField').val(),
        timeId: $('#timeField').val(),
    };

    // HTTP options
    const options = {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        body: JSON.stringify(appointment)
    };

    fetch(`${checkoutUri}${serviceId}/`, options)
        .then((response) => {
            return response.json();
        })
        .then((session) => {
            return stripe.redirectToCheckout({ sessionId: session.id });
        })
        .then((result) => {
            // If redirectToCheckout fails due to a browser or network
            // error, you should display the localized error message to your
            // customer using error.message.
            if (result.error) {
                alert(result.error.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function resourceSelectChange() {
    const resource_id = $resourceField.val();
    const cleanUp = () => $serviceField.find('option').remove().end().append(`<option value="">...</option>`);
    if (resource_id) {
        cleanUp();
        fetch(`/services/${resource_id}`)
            .then((response) => response.json())
            .then((response) => {
                response.data.forEach(service => {
                    $serviceField.append(`<option value="${service.id}"> &euro; ${service.get_display_price} - ${service.name}</option>`);
                });
                $serviceField.prop('disabled', false);
            })
            .catch(function (error) {
                cleanUp();
                $serviceField.prop('disabled', true);
                console.error("Error:", error);
            });
    } else {
        cleanUp();
        $serviceField.prop('disabled', true);
    }
}

function dateSelectChange() {
    const date_id = $dateField.val();
    const cleanUp = () => $timeField.find('option').remove().end().append(`<option value="">...</option>`);
    if (date_id) {
        cleanUp();
        fetch(`/times/${date_id}`)
            .then((response) => response.json())
            .then((response) => {
                response.data.forEach(time => {
                    $timeField.append(`<option value="${time.id}">${time.hour}:${time.minute}h</option>`);
                });
                $timeField.prop('disabled', false);
            })
            .catch(function (error) {
                cleanUp();
                $timeField.prop('disabled', true);
                console.error("Error:", error);
            });
    } else {
        cleanUp();
        $timeField.prop('disabled', true);
    }
}

// attach element events
$checkoutButton.click(() => checkoutStripe());
$resourceField.change(() => resourceSelectChange());
$dateField.change(() => dateSelectChange());