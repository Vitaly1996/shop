from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from products.views import (CreateCheckoutSessionView,
                            IndexPageView,
                            SuccessView,
                            CancelView,
                            stripe_webhook)


urlpatterns = [
    path('buy/<int:id>',
         CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),
    path('item/<int:id>', IndexPageView.as_view(), name='index'),
    path('webhooks/stripe', stripe_webhook, name='stripe-webhook'),
    path('success',SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel'),
]