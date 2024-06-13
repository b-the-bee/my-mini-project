from flask import *
import database_handler as db
web = Blueprint('web', __name__)

# GET order items
@web.route('/index')
def order_details():
    return send_file('static/index.html')

@web.route('/order-items')
def order_items():
    return send_file('static/order-items.html')

# GET items info
@web.route('/orders')
def orders():
    return send_file('static/orders.html')

# GET customer details
@web.route('/customer-details')
def customer_details():
    return send_file('static/customer-details.html')

# GET couriers
@web.route('/couriers')
def couriers():
    return send_file('static/couriers.html')



# GET delivery info
@web.route('/deliveries')
def couriers_deliviries():
    return send_file('static/deliveries.html')



# GET items info
@web.route('/items')
def items():
    return send_file('static/items.html')

