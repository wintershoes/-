# editor : banyanrong
# time : 2024/6/23 16:39
from flask import Blueprint, request, jsonify
from app.services.activity_service import ActivityService

activity_bp = Blueprint('activity_bp', __name__)

@activity_bp.route('/activities', methods=['POST'])
def add_activity():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    location = data.get('location')
    link = data.get('link')

    print(type(start_time), start_time)

    new_activity = ActivityService.add_activity(name, description, start_time, end_time, location, link)
    return jsonify(new_activity.to_dict()), 201

@activity_bp.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    activity = ActivityService.get_activity(activity_id)
    if activity:
        return jsonify(activity.to_dict()), 200
    return jsonify({'error': 'Activity not found'}), 404

@activity_bp.route('/activities', methods=['GET'])
def get_all_activities():
    activities = ActivityService.get_all_activities()
    return jsonify([activity.to_dict() for activity in activities]), 200

@activity_bp.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    location = data.get('location')
    link = data.get('link')

    updated_activity = ActivityService.update_activity(activity_id, name, description, start_time, end_time, location, link)
    if updated_activity:
        return jsonify(updated_activity.to_dict()), 200
    return jsonify({'error': 'Activity not found'}), 404

@activity_bp.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    deleted_activity = ActivityService.delete_activity(activity_id)
    if deleted_activity:
        return jsonify({'message': 'Activity deleted successfully'}), 200
    return jsonify({'error': 'Activity not found'}), 404
