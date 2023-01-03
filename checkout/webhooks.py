import json
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from checkout.webhook_handler import StripeWH_Handler
from django.views.decorators.csrf import csrf_exempt
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhook endpoint from Stripe
    https://stripe.com/docs/payments/handling-payment-events
    """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data & verify its signature
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key, wh_secret
            )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle the event
    print('Success!')
    return HttpResponse(status=200)
