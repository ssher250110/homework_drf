import os
import stripe
from forex_python.converter import CurrencyRates

stripe.api_key = os.getenv('STRIPE_API_KEY')


def convert_to_dollars(amount):
    c = CurrencyRates()
    rate = c.get_rate('RUB', 'USD')
    return int(amount * rate)


def create_stripe_product(product):
    return stripe.Product.create(name=product)


def create_stripe_price(amount, product):
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product},
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
