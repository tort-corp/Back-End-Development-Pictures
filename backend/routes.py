from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    """
    Returns:
        200: if status OK
    """
    return jsonify(dict(status="OK")), 200


######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """
    Return
      json: length of data and status 200
      500: No data exists
    """
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    """
    Get all pictures json in data
    Returns:
      json: all pictures json from data and status 200

    """
    return data, 200


######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    """
    Gets specific picture json based on picture id key.
    Returns:
        json: picture json based on id received in request
        404: No picture of that id found
    """
    for picture in data:
        if picture["id"] == id:
            return picture

    return ({"message": "Picture not found"}, 404)


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """
    creates a picture based on request body json and adds it to data
    Returns:
        302: already a picture with that id
        201:
    """
    # request.json parses json only if content type is application/json,
    # otherwise its empty
    new_picture = request.json
    if not new_picture:
        return {"message": "Invalid input parameter"}, 422

    # code to validate new_picture ommited

    # check if picture exists already in data
    for picture in data:
        if new_picture["id"] == picture["id"]:
            return {
                "Message": f"picture with id {new_picture['id']} already present"
            }, 302

    # add picture to data
    data.append(new_picture)
    return new_picture, 201


######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """
    updates a picture based on request body json if picture exists
    Returns:
        201:
        404:
    """
    # request.json parses json only if content type is application/json,
    # otherwise its empty
    new_picture = request.json
    if not new_picture:
        return {"message": "Invalid input parameter"}, 422

    for picture in data:
        if picture["id"] == id:
            index = data.index(picture)
            data[index] = new_picture
            return new_picture, 201

    return {"message": "picture not found"}, 404


######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """
    deletes a person from the data list based on uuid received in request
    Returns:
        404:
        204:
    """

    for picture in data:
        if picture["id"] == id:
            data.remove(picture)
            return "", 204

    return {"message": "picture not found"}, 404
