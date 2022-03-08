const $serviceField = $('#id_service')
const $clinicianField = $('#id_clinician');
const $dateField = $('#id_date');
const $timeField = $('#id_time')
const $totalField = $('#total')
const $bookingButton = $('#booking-button');

$clinicianField.prop('disabled', true);
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
            console.log('Error:', error);
        });
}

function cleanUpSelectOptions($element, placeholder) {
    $element.find('option').remove().end().append(`<option value="">${placeholder}</option>`);
}

async function getServices() {
    try {
        const response = await fetch(`/services`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

async function getService(id) {
    try {
        const response = await fetch(`/services/${id}`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

function loadServices() {
    const placeholder = $serviceField.attr('placeholder');
    cleanUpSelectOptions($serviceField, placeholder);
    getServices().then(data => {
        data.forEach(service => {
            $serviceField.append(`<option value="${service.id}"> &euro; ${service.price} - ${service.name}</option>`);
        });
    })
    .catch((error) => {
        cleanUpSelectOptions($serviceField, placeholder);
        $serviceField.prop('disabled', true);
        console.error("Error:", error);
    });
}

function serviceSelectChange() {
    const service_id = $serviceField.val();
    const placeholder = $clinicianField.attr('placeholder');
    if (service_id) {
        cleanUpSelectOptions($clinicianField, placeholder);
        getService(service_id)
            .then(service => {
                $totalField.text(`€ ${service.price}`);
                service.clinicians.forEach(clinician => {
                    $clinicianField.append(`<option value="${clinician.id}">${clinician.full_name}</option>`);
                });
                $clinicianField.prop('disabled', false);
            })
            .catch((error) => {
                $totalField.text('€ 0.00');
                cleanUpSelectOptions($clinicianField, placeholder);
                $clinicianField.prop('disabled', true);
                console.error("Error:", error);
            });
    } else {
        $totalField.text('€ 0.00');
        cleanUpSelectOptions($clinicianField, placeholder);
        $clinicianField.prop('disabled', true);
    }
}

async function getDates() {
    try {
        const response = await fetch(`/bookings/dates`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

async function getTimes(id) {
    try {
        const response = await fetch(`/bookings/times/${id}`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

function loadDates() {
    const placeholder = $dateField.attr('placeholder');
    cleanUpSelectOptions($dateField, placeholder);
    getDates()
        .then(data => {
            data.forEach(date => {
                $dateField.append(`<option value="${date.id}">${date.date}</option>`);
            });
        })
        .catch((error) => {
            cleanUpSelectOptions($dateField, placeholder);
            console.error("Error:", error);
        });
}

function dateSelectChange() {
    const date_id = $dateField.val();
    const placeholder = $timeField.attr('placeholder');
    cleanUpSelectOptions($timeField, placeholder);
    if (date_id) {
        cleanUpSelectOptions($timeField, placeholder);
        getTimes(date_id)
            .then(data => {
                data.forEach(time => {
                    $timeField.append(`<option value="${time.id}">${time.time} h</option>`);
                });
                $timeField.prop('disabled', false);
            })
            .catch(function (error) {
                cleanUpSelectOptions($timeField, placeholder);
                $timeField.prop('disabled', true);
                console.error("Error:", error);
            });
    } else {
        cleanUpSelectOptions($timeField, placeholder);
        $timeField.prop('disabled', true);
    }
}

// attach element events
// $checkoutButton.click(() => checkoutStripe());
$serviceField.change(() => serviceSelectChange());
$dateField.change(() => dateSelectChange());

// load select options
loadServices();
loadDates();