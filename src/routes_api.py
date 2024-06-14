from flask import *
import database_handler as db
api = Blueprint('api', __name__)

@api.route('/api/order-items')
def get_order_items():
    return jsonify(db.read_order_items())

@api.route('/api/customers')
def get_customer_details():
    return jsonify(db.read_customer_details())

@api.route('/api/customers', methods=["PUT"])
def add_customer_details():
    new_customer = db.insert_new_order(
        request.json.get('order_status'),
        request.json.get('customers_name'),
        request.json.get('customers_address'),
        request.json.get('customers_phone'),
        chosens_products = request.json.get('chosen_product').split(","))
    if new_customer:
        return jsonify({"result": "success", "order": new_customer})
    else:
        return jsonify({"result": "Order not found"}), 404
   

@api.route('/api/orders', methods=["POST"])
def update_order():
    db.update_order_status(
        order_id=request.json.get('order_id'),
        status=request.json.get('status'))
    return jsonify({"result": "success"})

@api.route('/api/order/<order_id>')
def get_this_order(order_id):
    order = db.read_one_order(order_id)
    if order:
        return jsonify({"result": "success", "order": order})
    else:
        return jsonify({"result": "Order not found"}), 404
   

@api.route('/api/orders', methods=["DELETE"])
def delete_order():
    db.delete_order(request.json.get('order_id'))
    return jsonify({"result": "success"})

@api.route('/api/orders')
def get_order_details():
    return jsonify(db.read_orders())

@api.route('/api/couriers')
def get_courier_details():
    return jsonify(db.read_couriers())

@api.route('/api/couriers/<courier_id>')
def get_this_courier(courier_id):
    print(courier_id)
    courier_id = db.read_one_courier(courier_id)
    print(courier_id)
    if courier_id:
        return jsonify({"result": "success", "courier": courier_id})
    else:
        return jsonify({"result": "Courier not found"}), 404

@api.route('/api/couriers', methods=["PUT"])
def add_courier_details():
    new_courier = db.insert_new_courier(
        request.json.get('courier_name'),
        request.json.get('courier_phone'),
        request.json.get('courier_status'),)
    if new_courier:
        return jsonify({"result": "success", "order": new_courier})
    else:
        return jsonify({"result": "Order not found"}), 404

@api.route('/api/couriers', methods=["DELETE"])
def delete_courier():
    db.delete_courier(request.json.get('courier_id'))
    return jsonify({"result": "success"})

@api.route('/api/orders', methods=["POST"])
def update_courier():
    db.update_order_status(
        order_id=request.json.get('order_id'),
        status=request.json.get('status'))
    return jsonify({"result": "success"})



@api.route('/api/deliveries')
def get_courier_delivery_details():
    return jsonify(db.read_couriers_delivery())

@api.route('/api/items')
def get_items_details():
    return jsonify(db.read_all_items())