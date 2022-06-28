from flask import Blueprint, jsonify, request
from app.models.board import Board
from app import db

boards_bp = Blueprint('boards_bp', __name__, url_prefix='/boards')

@boards_bp.route('', method=['GET'])
def get_all_boards():
    boards = Board.query.all()

    response_body = [board.to_json() for board in boards]

    return jsonify(response_body), 200


@boards_bp.route('', method=['POST'])
def post_new_board():
    new_board_request = request.get_json()
    new_board = Board(title=new_board_request['title'], owner=new_board_request['owner'])
    db.session.add(new_board)
    db.session.commit()

    rsp = {'message': 'New board created with id:{new_board.board_id}'}
    return rsp, 201

