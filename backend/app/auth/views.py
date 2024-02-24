from . import auth, user
from flask import jsonify, request
from .models.User import User
from .models.MaUser import ma_user, ma_users
from .models.MaLoginUser import ma_login_user
from app import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timezone
from .models.TokenBlocklist import TokenBlocklist


@auth.route('/login', methods=['POST'])
def login():
    """
    Login a user

    Returns: Json of logged in user
    """
    data = request.get_json()
    if not data:
        return jsonify(message="No input data provided"), 400
    errors = ma_login_user.validate(data)
    if errors:
        print(errors)
        return jsonify(errors), 422

    user = User.get_user_by_email(data['email'])
    if not user:
        return jsonify(message="User not found"), 404

    if not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify(message="Incorrect password"), 401

    access_token = create_access_token(identity=user.email)
    # access_token = access_token.encode('utf-8')

    my_user = ma_user.dump(user)

    return jsonify(
        access_token=access_token,
        user=my_user
    ), 200


@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Protected route

    Returns: Json of logged in user
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@auth.route("/logout", methods=["DELETE"])
@jwt_required()
def modify_token():
    """
    Logout a user

    Returns: String "JWT revoked"
    """
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)

    TokenBlocklistInfo = TokenBlocklist(jti=jti, created_at=now)
    TokenBlocklistInfo.save()

    return jsonify(msg="JWT revoked"), 200


@user.route('/', methods=['GET'])
def get_all_users():
    """
    Get all users

    Returns: Json of all users
    """
    users = User.get_all()
    if not users:
        return jsonify(message="No users found"), 404
    return jsonify(ma_users.dump(users)), 200


@user.route('/', methods=['POST'])
def create_user():
    """
    Create a user

    Returns: Json of created user
    """
    data = request.get_json()
    if not data:
        return jsonify(message="No input data provided"), 400
    errors = ma_user.validate(data)
    if errors:
        return jsonify(errors), 422

    # Hash the password before creating the User object
    hashed_password = bcrypt.generate_password_hash(
        data['password']).decode('utf-8')
    data['password'] = hashed_password

    user = User(**data)
    if not user.save():
        return jsonify(message="Username already exists"), 409
    return jsonify(ma_user.dump(user)), 201


@user.route('/<int:id>', methods=['GET'])
def get_user(id):
    """
    Get a user

    Args:
        id: User id

    Returns: Json of user
    """
    user = User.get_by_id(id)
    if not user:
        return jsonify(message="User not found"), 404
    return jsonify(ma_user.dump(user)), 200


@user.route('/role/supervisors', methods=['GET'])
def get_supervisors():
    """
    Get all supervisors

    Returns: Json of all supervisors
    """
    users = User.get_by_role("supervisor")
    if not users:
        return jsonify(message="No supervisors found"), 404
    return jsonify(ma_users.dump(users)), 200


@user.route('/role/workers', methods=['GET'])
def get_workers():
    """
    Get all workers

    Returns: Json of all workers
    """
    users = User.get_by_role("worker")
    if not users:
        return jsonify(message="No workers found"), 404
    return jsonify(ma_users.dump(users)), 200
