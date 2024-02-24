import os
from . import meter_reading
from flask import request, jsonify, send_from_directory
from .models.MeterReading import MeterReading
from .models.MaMeterReading import ma_meter_reading, ma_meter_readings
from datetime import datetime, timedelta, timezone


now = datetime.now()
current_month = now.month
current_year = now.year
basedir = os.path.abspath(os.path.dirname(__file__))
upload_folder = os.path.join(basedir, 'uploads')

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

allowed_extensions = {'jpg', 'png', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


@meter_reading.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(upload_folder, filename)


@meter_reading.route('/', methods=['POST'])
def create_meter_reading():

    print(request.form)
    
    # meter_id = request.form.get('meter_id')
    # user_id = request.form.get('user_id')
    # reading = request.form.get('reading')
    # reading_image = request.form.get('reading_image')
    # reading_date = request.form.get('reading_date')
    # reading_gps_coordinates = request.form.get('reading_gps_coordinates')
    # comments = request.form.get('comments')

    

    reading_image = ''

    if 'reading_image' in request.files:
        reading_image = request.files['reading_image']
        if reading_image and allowed_file(reading_image.filename):
            reading_image.save(os.path.join(upload_folder, reading_image.filename))
            reading_image = reading_image.filename
    
    if not reading_image:
        return jsonify(message="No image found"), 404
    
        
    data = request.form.to_dict()
    # data["reading_date"] = datetime.strptime(data['reading_date'], '%Y-%m-%d %H:%M:%S')
    print(data)
    data['reading_image'] = reading_image
    errors = ma_meter_reading.validate(data)
    if errors:
        return jsonify(errors), 422


    meter_reading = MeterReading(**data)
    info = meter_reading.save()

    return jsonify(info = info), 201


@meter_reading.route('/', methods=['GET'])
def get_all_meter_readings():
    meter_readings = MeterReading.get_all()
    if not meter_readings:
        return jsonify(message='No meter readings found'), 404
    meter_readings_info = ma_meter_readings.dump(meter_readings)
    return jsonify(meter_readings_info), 200


@meter_reading.route('/', methods=['DELETE'])
def delete_all_meter_readings():
    info = MeterReading.delete_all()
    return jsonify(info=info), 200
