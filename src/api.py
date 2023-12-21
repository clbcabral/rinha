from flask import Flask, jsonify, request
from psycopg2.pool import SimpleConnectionPool
import os


pool = SimpleConnectionPool(1, 20, 
                            user=os.environ.get('POSTGRES_USER'), 
                            password=os.environ.get('POSTGRES_PASSWORD'), 
                            host='db', 
                            port='5432', 
                            database=os.environ.get('POSTGRES_DB'))

if pool:
    print('conectado!')

pool.closeall()

app = Flask(__name__)
# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def pessoas():
    
    if request.method == 'POST':
         print('foi post!')

    if request.method == 'GET':
         print('foi get!')
    
    # print(request.is_json)
    # data = request.get_json()
    # print(data)
    # return jsonify({
    #     "a"        :  1,
    #     "b"        :  2,
    # })
    return 'okokok'


if __name__ == '__main__':
     app.run(port='8000')