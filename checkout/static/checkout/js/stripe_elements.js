const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
const clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
// Style from https://stripe.com/docs/js/appendix/style
const appearance = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
// Pass the appearance object to the Elements instance
let card = elements.create("card", { appearance: appearance });
// Mount card on the div in checkout page
card.mount("#card-element");

// Handle real-time validation errors on the card element
card.addEventListener("change", function (event) {
  const errorDiv = document.getElementById("card-errors");
  if (event.error) {
    const html = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
      `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// STEP 1: Checkout view creates payment intent
// STEP 2: Stripe returns unique client_secret that we return to template
// STEP 3: Use client_secret in template to call confirmCardPayment() & verify the card

// Handle form submit
const form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  // Prevent form default action (here POST)
  ev.preventDefault();
  // Disable card Elem & submit btn to prevent multiple submissions
  // prettier-ignore
  card.update({ 'disabled': true });
  $("#submit-button").attr("disabled", true);
  // Display loading animation & fade out form on submit
  $("#payment-form").fadeToggle(100);
  $("#loading-overlay").fadeToggle(100);

  const saveInfo = Boolean($("#id-save-info").attr("checked"));
  // From using {% csrf_token %} in the form
  const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  // Small object to pass info to new view from form that cannot be passed in payment intent
  const postData = {
    // prettier-ignore
    'csrfmiddlewaretoken': csrfToken,
    // Pass the secret for payment intent
    // prettier-ignore
    'client_secret': clientSecret,
    // prettier-ignore
    'save_info': saveInfo,
  };

  const url = "/checkout/cache_checkout_data/";

  // Post the data to the new view
  // Posts instead data above to url view
  $.post(url, postData)
    .done(function () {
      // Instead execute this code
      // Sends card info securely to Stripe
      stripe
        .confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address: {
                line1: $.trim(form.street_address_1.value),
                line2: $.trim(form.street_address_2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
              },
            },
          },
          shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address_1.value),
              line2: $.trim(form.street_address_2.value),
              city: $.trim(form.town_or_city.value),
              country: $.trim(form.country.value),
              postal_code: $.trim(form.postcode.value),
              state: $.trim(form.county.value),
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            const errorDiv = document.getElementById("card-errors");
            const html = `
              <span class="icon" role="alert">
              <i class="fas fa-times"></i>
              </span>
              <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Fade form on submit
            $("#payment-form").fadeToggle(100);
            $("#loading-overlay").fadeToggle(100);
            // If there is an error, re-enable the btns to fix it
            // prettier-ignore
            card.update({ 'disabled': false });
            $("#submit-button").attr("disabled", false);
          } else {
            if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          }
        });
    })
    .fail(function () {
      // Just reloads the page, the error will be in django messages
      location.reload();
    });
});
