from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import uuid


@dataclass
class Record:
    name: str
    json_data: dict
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))


class DatabaseAccess:

    def __init__(self):
        self.records = []

    def find_record_by_id(self, record_id):
        found_record = [record for record in self.records if record.record_id == record_id]
        return found_record[0]

    def find_record_index_by_id(self, record_id):
        record_index = [index for index, found_record in enumerate(self.records) if found_record.record_id == record_id]
        return record_index[0]

    def find_records_by_name(self, record_name):
        found_records = [found_record for found_record in self.records if found_record.name == str(record_name)]
        return found_records

    def update_record_by_id(self, record_id, name, data):
        index = self.find_record_index_by_id(record_id)
        self.records[index].name = name
        self.records[index].json_data = data

    def list_records(self):
        return self.records

    def add_record(self, name, json_data):
        self.records.append(Record(str(name), json_data))

    def delete_record(self, record_id):
        index = self.find_record_index_by_id(record_id)
        del self.records[index]


def main():
    app = Flask(__name__)
    database = DatabaseAccess()

    @app.route("/welcome")
    @app.route("/welcome/<name>")
    def greetings(name=''):
        return f"<h1>Welcome to this simple REST server {name}.</h1>", 200

    @app.route("/records")
    def records():
        return jsonify(database.list_records()), 200

    @app.route("/record", methods=['GET', 'POST'])
    def record_by_name(database=database):
        record_name = request.args.get('record_name')
        if record_name:
            if request.method == 'POST':
                database.add_record(record_name, request.json)
                return f"Record added {str(record_name)}\n", 200
            if request.method == 'GET':
                return jsonify(database.find_records_by_name(record_name)), 200
        else:
            return 'You must include a record_name as a parameter.', 400

    @app.route("/record/id", methods=['GET', 'PUT', 'DELETE'])
    def record_by_id(database=database):
        record_id = request.args.get('record_id')
        if record_id:
            if request.method == 'GET':
                return jsonify(database.find_record_by_id(record_id)), 200
            if request.method == 'DELETE':
                database.delete_record(record_id)
                return "Record Deleted", 200
            if request.method == 'PUT':
                database.update_record_by_id(record_id, request.args.get('name'), request.json)
                return "Record Updated", 200
        else:
            return 'You must include a record_id as a parameter.', 400

    app.run(debug=True)


if __name__ == '__main__':
    main()



