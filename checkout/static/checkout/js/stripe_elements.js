const stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
const client_secret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripe_public_key);
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
