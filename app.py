import os
from flask import (
    Flask,
    jsonify,
    request,
    abort
)
from flask_migrate import Migrate
from flask_cors import CORS
from models import setup_db, db, Traveller, Venue
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)

    CORS(app)

    @app.route('/')
    def get_greeting():
        return jsonify({
            'success': True,
            'message': 'done the FSND!!'
        })

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/travellers', methods=['GET'])
    @requires_auth("get:travellers")
    def get_all_travellers():
        travellers = Traveller.query.order_by(Traveller.id).all()
        travellers = [traveller.format() for traveller in travellers]

        return jsonify({
            'success': True,
            'travellers': travellers
        }), 200

    @app.route('/travellers/<int:id>', methods=['GET'])
    @requires_auth('get:travellers-info')
    def get_specific_traveller(payload, id):
        traveller = Traveller.query.filter_by(id=id).one_or_none()
        if traveller is None:
            abort(404)
        return jsonify({
            'success': True,
            'traveller': traveller.format()
        })

    @app.route('/travellers', methods=['POST'])
    @requires_auth('post:travellers')
    def post_traveller(payload):
        if request.method == "POST":
            body = request.get_json()
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            traveller = Traveller(name=name, age=age, gender=gender)
            traveller.insert()

            return jsonify({
                'success': True,
                'created_traveller': traveller.name,
                'total_travellers': len(Traveller.query.all())
            })

    @app.route('/travellers/<int:id>', methods=['PATCH'])
    @requires_auth('patch:travellers')
    def patch_traveller(payload, id):
        if request.method == "PATCH":
            body = request.get_json()

            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            traveller = Traveller.query.filter_by(id=id).one_or_none()

            if traveller is None:
                abort(404)

            traveller.name = name
            traveller.age = age
            traveller.gender = gender
            traveller.update()

            return jsonify({
                'success': True,
                'patched_traveller': id,
                'total_travellers': len(Traveller.query.all())
            })

    @app.route('/travellers/<int:id>', methods=['DELETE'])
    @requires_auth('delete:travellers')
    def delete_traveller(payload, id):
        traveller = Traveller.query.filter_by(id=id).one_or_none()

        if traveller is None:
            abort(404)

        traveller.delete()

        return jsonify({
            'success': True,
            'deleted': id,
            'total_travellers': len(Traveller.query.all())
        }), 200

    @app.route('/venues', methods=['GET'])
    @requires_auth('get:venues')
    def get_all_venues(payload):
        venues = Venue.query.order_by(Venue.id).all()
        venues = [venue.format() for venue in venues]

        return jsonify({
            'success': True,
            'venues': venues
        }), 200

    @app.route('/venues/<int:id>', methods=['GET'])
    @requires_auth('get:venues-info')
    def get_specific_venue(payload, id):
        venue = Venue.query.filter_by(id=id).one_or_none()
        if venue is None:
            abort(404)

        return jsonify({
            'success': True,
            'venue': venue.format()
        })

    @app.route('/venues/<int:id>', methods=['DELETE'])
    @requires_auth('delete:venues')
    def delete_venue(payload, id):
        venue = Venue.query.filter_by(id=id).one_or_none()

        if venue is None:
            abort(404)

        venue.delete()

        return jsonify({
            'success': True,
            'deleted': id,
            'total_venues': len(Venue.query.all())
        }), 200

    @app.route('/venues', methods=['POST'])
    @requires_auth('post:venues')
    def post_venue(payload):
        if request.method == "POST":
            body = request.get_json()

            vname = body.get('vname', None)
            visit_year = body.get('visit_year', None)
            duration = body.get('duration', None)

            venue = Venue(
                vname=vname,
                visit_year=visit_year,
                duration=duration)
            venue.insert()

            return jsonify({
                'success': True,
                'created_venue': venue.id,
                'total_venues': len(Venue.query.all())
            }), 200

    @app.route('/venues/<int:id>', methods=['PATCH'])
    @requires_auth('patch:venues')
    def patch_venue(payload, id):
        if request.method == "PATCH":
            venue = Venue.query.filter_by(id=id).one_or_none()
            if venue is None:
                abort(404)
            body = request.get_json()
            vname = body.get('vname', None)
            visit_year = body.get('visit_year', None)
            duration = body.get('duration', None)

            venue.vname = vname
            venue.visit_year = visit_year
            venue.duration = duration

            venue.update()

            return jsonify({
                'success': True,
                'updated_venue': id,
                'total_venues': len(Venue.query.all())
            })

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 422

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
