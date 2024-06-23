# editor : banyanrong
# time : 2024/6/23 16:39
from flask import Blueprint, request, jsonify
from app.services.activity_service import ActivityService
from datetime import datetime

activity_bp = Blueprint('activity_bp', __name__)

@activity_bp.route('/activities', methods=['POST'])
def add_activity():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        start_time = datetime.fromisoformat(data.get('start_time'))
        end_time = datetime.fromisoformat(data.get('end_time'))
        location = data.get('location')
        link = data.get('link')
        authorization = data.get("authorization")

        if authorization != 'admin':
            return jsonify({"error": "Unauthorized"}), 404
        new_activity = ActivityService.add_activity(name, description, start_time, end_time, location, link)
        return jsonify({
            "message": "Activity added successfully",
            "activityId": new_activity.activity_id}), 201
    except Exception as e:
        return jsonify({"error": "Unknown error occured"}), 404


@activity_bp.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    try:
        activity = ActivityService.get_activity(activity_id)
        if not activity:
            return jsonify({'error': 'Activity not found'}), 404
        return jsonify(activity.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "Unknown error occured"}), 404


@activity_bp.route('/activities', methods=['GET'])
def get_all_activities():
    try:
        activities = ActivityService.get_all_activities()
        if not activities:
            return jsonify({"error": "No activites found"}), 404
        return jsonify([activity.to_dict() for activity in activities]), 200
    except Exception as e:
        return jsonify({"error": "Unknown error occured"}), 404


@activity_bp.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_time = datetime.fromisoformat(data.get('start_time'))
    end_time = datetime.fromisoformat(data.get('end_time'))
    location = data.get('location')
    link = data.get('link')
    authorization = data.get('authorization')
    try:
        if authorization != 'admin':
            return jsonify({"message": "Unauthorized"}), 404
        updated_activity = ActivityService.update_activity(activity_id, name, description, start_time, end_time, location, link)
        if updated_activity:
            return jsonify({"message": "Activity information updated successfully"}), 200
        return jsonify({'error': 'Activity not found'}), 404
    except:
        return jsonify({"error": "Unknown error occured"}), 404


@activity_bp.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    data = request.get_json()
    authorization = data.get("authorization")

    if authorization != 'admin':
        return jsonify({"message": "Unauthorized"}), 404

    deleted_activity = ActivityService.delete_activity(activity_id)
    if deleted_activity:
        return jsonify({'message': 'Activity deleted successfully'}), 200
    return jsonify({'error': 'Activity not found'}), 404
