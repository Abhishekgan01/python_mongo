from flask import request, jsonify
import service

def register_routes(app):
    @app.route('/items', methods=['GET'])
    def get_items():
        items = service.get_all_items()
        return jsonify(items)

    @app.route('/items', methods=['POST'])
    def add_item():
        data = request.json
        inserted_id = service.add_item(data)
        return jsonify({"inserted_id": inserted_id}), 201
    
    @app.route('/items/<item_id>', methods=['PUT'])
    def update_item(item_id):
        data = request.json
        updated_count = service.update_item(item_id, data)
        if updated_count == 1:
            return jsonify({"message": "Item updated successfully"}), 200
        else:
            return jsonify({"message": "Item not found"}), 404
        
    @app.route('/items/<item_id>', methods=['DELETE'])
    def delete_item(item_id):
        deleted_count = service.delete_item(item_id)
        if deleted_count == 1:
            return jsonify({"message": "Item deleted successfully"}), 200
        else:
            return jsonify({"message": "Item not found"}), 404