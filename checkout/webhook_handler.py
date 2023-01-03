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
            content=f'Webhook received: {event["type"]}',
            status=200
        )
