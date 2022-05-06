/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    fontFamily: '"Poppins", sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "14px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle form submit
var form = document.getElementById("booking-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#complete-payment-button").attr("disabled", true);
  $('#submit-button').attr('disabled', true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
    };
var url = '/checkout/cache_checkout_data/';
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
        }
      },
    })
    .then(function (result) {
      if (result.error) {
        var errorDiv = document.getElementById("card-errors");
        var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({ disabled: false });
        $("#complete-payment-button").attr("disabled", false);
      } else if (result.paymentIntent.status === "succeeded") {
        form.submit();
      }
    });
  }).fail(function () {
     // just reload the page, the error will be in django messages
      location.reload();
  })
});
