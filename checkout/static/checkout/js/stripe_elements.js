let stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
let client_secret = $("#id_client_secret").text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let card = elements.create("card");
const appearance = {
  theme: "flat",
  variables: {
    fontFamily: ' "Gill Sans", sans-serif',
    fontLineHeight: "1.5",
    borderRadius: "10px",
    colorBackground: "#F6F8FA",
    colorPrimaryText: "#262626",
  },
  rules: {
    ".Block": {
      backgroundColor: "var(--colorBackground)",
      boxShadow: "none",
      padding: "12px",
    },
    ".Input": {
      padding: "12px",
    },
    ".Input:disabled, .Input--invalid:disabled": {
      color: "lightgray",
    },
    ".Tab": {
      padding: "10px 12px 8px 12px",
      border: "none",
    },
    ".Tab:hover": {
      border: "none",
      boxShadow:
        "0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 7px rgba(18, 42, 66, 0.04)",
    },
    ".Tab--selected, .Tab--selected:focus, .Tab--selected:hover": {
      border: "none",
      backgroundColor: "#fff",
      boxShadow:
        "0 0 0 1.5px var(--colorPrimaryText), 0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 7px rgba(18, 42, 66, 0.04)",
    },
    ".Label": {
      fontWeight: "500",
    },
  },
};
// Pass the appearance object to the Elements instance
const elements = stripe.elements({ client_secret, appearance });
// Mount card on the div in checkout page
card.mount("#card-element");
