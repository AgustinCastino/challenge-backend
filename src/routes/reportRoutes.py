from flask import Blueprint
from controller import reportController

report = Blueprint('report', __name__)

# GET Endpoints
@report.route('/', methods=['GET'])
def get_report():
    return reportController.createReport()

