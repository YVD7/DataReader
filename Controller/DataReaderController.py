from flask import Flask, request
from DataReader.Service.DataReaderService import DataReaderService
data_reader_app = Flask(__name__)

@data_reader_app.route("/DataReader", methods=["POST"])
def data_reader():
    key = request.get_json()
    drs = DataReaderService()
    print(key)
    return drs.data_reader(key['ticker'])

# if __name__=="__main__":
#     data_reader_app.run(port=8080)