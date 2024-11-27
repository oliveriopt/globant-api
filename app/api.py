from flask import Blueprint, request, jsonify
from app.models import Department, Job, Employee
from app.db import db
from app.utils import connect_s3, fetch_csv_from_s3

api = Blueprint('api', __name__)

@api.route('/upload_from_s3', methods=['POST'])
def upload_from_s3():
    s3 = connect_s3(request.app.config)
    dataframes = fetch_csv_from_s3(s3, request.json['bucket'], request.json['folder'])
    # Assuming order: departments, jobs, employees
    tables = [Department, Job, Employee]
    for df, table in zip(dataframes, tables):
        db.session.bulk_insert_mappings(table, df.to_dict(orient='records'))
    db.session.commit()
    return jsonify({"status": "success"}), 200

@api.route('/batch_insert', methods=['POST'])
def batch_insert():
    data = request.json
    model_mapping = {'departments': Department, 'jobs': Job, 'employees': Employee}
    table_name = data['table']
    rows = data['rows']
    
    if len(rows) > 1000:
        return jsonify({"error": "Batch size exceeds 1000 rows"}), 400
    
    table = model_mapping.get(table_name)
    if not table:
        return jsonify({"error": "Invalid table name"}), 400
    
    db.session.bulk_insert_mappings(table, rows)
    db.session.commit()
    return jsonify({"status": "success"}), 200
