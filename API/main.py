from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from API.PredictGlare import predict_glare

app = Flask(__name__)
api = Api(app);

detect_glare_args = reqparse.RequestParser();
detect_glare_args.add_argument("latitude", type=float, help="Latitude of the observer")
detect_glare_args.add_argument("longitude", type=float, help="Longitude of the observer")
detect_glare_args.add_argument("epoch", type=float, help="Epoch Timestamp")
detect_glare_args.add_argument("orientation", type=float, help="Orientation of the observer")

class post_predict_glare(Resource):
    def post(self):
        args = detect_glare_args.parse_args();
        return jsonify({"glare":predict_glare().detect_glare(latitude=args["latitude"], longitude=args["longitude"], epoch=args["epoch"], orientation=args["orientation"])})

api.add_resource(post_predict_glare,"/detect_glare")
if __name__ == "__main__":
    app.run(debug=True)  # avoid in prod environment


