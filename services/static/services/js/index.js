const $serviceField = $('#id_service')
const $clinicianField = $('#id_clinician');
const $dateField = $('#id_date');
const $timeField = $('#id_time')
const $totalField = $('#total')
const $bookingButton = $('#booking-button');

$clinicianField.prop('disabled', true);
$timeField.prop('disabled', true);

function loadingSelectOptions($element) {
    $element.prop('disabled', true);
    cleanUpSelectOptions($element, 'Loading ...');
}

function cleanUpSelectOptions($element, placeholder) {
    $element.find('option').remove().end().append(`<option value="">${placeholder}</option>`);
}

async function getServices() {
    try {
        const response = await fetch(`/services/all`);
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
    loadingSelectOptions($serviceField);
    getServices().then(data => {
        cleanUpSelectOptions($serviceField, placeholder);
        data.forEach(service => {
            $serviceField.append(`<option value="${service.id}"> &euro; ${service.price} - ${service.name}</option>`);
        });
        $serviceField.prop('disabled', false);
    })
    .catch((error) => {
        cleanUpSelectOptions($serviceField, placeholder);
        console.error("Error:", error);
    });
}

function serviceSelectChange() {
    const service_id = $serviceField.val();
    const placeholder = $clinicianField.attr('placeholder');
    if (service_id) {
        loadingSelectOptions($clinicianField);
        getService(service_id)
            .then(service => {
                cleanUpSelectOptions($clinicianField, placeholder);
                $totalField.text(`€ ${service.price}`);
                service.clinicians.forEach(clinician => {
                    $clinicianField.append(`<option value="${clinician.id}">${clinician.full_name}</option>`);
                });
                $clinicianField.prop('disabled', false);
            })
            .catch((error) => {
                $totalField.text('€ 0.00');
                cleanUpSelectOptions($clinicianField, placeholder);
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
        const response = await fetch(`/services/dates`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

async function getTimes(id) {
    try {
        const response = await fetch(`/services/times/${id}`);
        const response_1 = await response.json();
        return response_1.data;
    } catch (error) {
        throw error;
    }
}

function loadDates() {
    const placeholder = $dateField.attr('placeholder');
    loadingSelectOptions($dateField);
    getDates()
        .then(data => {
            $dateField.prop('disabled', false);
            cleanUpSelectOptions($dateField, placeholder);
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
        loadingSelectOptions($timeField);
        getTimes(date_id)
            .then(data => {
                cleanUpSelectOptions($timeField, placeholder);
                data.forEach(time => {
                    $timeField.append(`<option value="${time.id}">${time.time} h</option>`);
                });
                $timeField.prop('disabled', false);
            })
            .catch(function (error) {
                cleanUpSelectOptions($timeField, placeholder);
                console.error("Error:", error);
            });
    } else {
        cleanUpSelectOptions($timeField, placeholder);
        $timeField.prop('disabled', true);
    }
}

$serviceField.change(() => serviceSelectChange());
$dateField.change(() => dateSelectChange());

loadServices();
loadDates();
