from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    """
    Init method is called every time an instance of the class
    is created.
    """
    def __init__(self, request):
        """
        Assign the request as an attribute of the class
        in case we want to access the attributes
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event that
        Stripe is sending, returning HTTP response
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
