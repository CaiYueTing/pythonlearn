from flask import jsonify, Blueprint
from app.role.models import Role

ROLE = Blueprint('role', __name__, url_prefix='/api/v1/roles')


@ROLE.route('/<role_id>',  methods=["GET"])
def getRole(role_id):
    role = Role.getRoleById(role_id)
    if role is None:
        return jsonify({"error": {"message": "wrong role id"}})

    return jsonify({"data": {"id": role.id, "role": role.role}}), 200