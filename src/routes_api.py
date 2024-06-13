from flask import *
import database_handler as db
api = Blueprint('api', __name__)

@api.route('/api/order-items')
def get_order_items():
    return jsonify(db.read_order_items())

@api.route('/api/customers')
def get_customer_details():
    return jsonify(db.read_customer_details())


@api.route('/api/orders', methods=["POST"])
def update_order():
    db.update_order_status(order_id=request.json.get('order_id'), status=request.json.get('status'))
    return jsonify({"result": "success"})

@api.route('/api/order/<order_id>')
def get_this_order(order_id):
    order = db.read_one_order(order_id)
    if order:
        return jsonify({"result": "Success", "order": order})
    else:
        return jsonify({"result": "Order not found"}), 404
   

@api.route('/api/orders', methods=["DELETE"])
def delete_order():
    db.
    db.delete_order(request.json.get('order_id'))
    return jsonify({"result": "success"})

@api.route('/api/orders')
def get_order_details():
    return jsonify(db.read_orders())

@api.route('/api/couriers')
def get_courier_details():
    return jsonify(db.read_couriers())

@api.route('/api/deliveries')
def get_courier_delivery_details():
    return jsonify(db.read_couriers_delivery())

@api.route('/api/items')
def get_items_details():
    return jsonify(db.read_all_items())