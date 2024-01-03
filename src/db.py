import os, uuid
from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row

conninfo = 'postgresql://%s:%s@%s/%s' % (
    os.environ.get('POSTGRES_USER'), 
    os.environ.get('POSTGRES_PASSWORD'),
    os.environ.get('POSTGRES_HOST'),
    os.environ.get('POSTGRES_DB'),
)
pool_size = int(os.environ.get('DB_POOL_SIZE'))

pool = ConnectionPool(conninfo = conninfo, min_size = pool_size, max_size = pool_size)
pool.wait()

def create_pessoa(data):
    id = str(uuid.uuid4())
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            data['id'] = id
            sql = 'INSERT INTO PESSOA (id, apelido, nome, nascimento, stack) VALUES (%(id)s, %(apelido)s, %(nome)s, %(nascimento)s, %(stack)s)'
            cursor.execute(sql, data)
            return id

def get_pessoa(id):
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            sql = "SELECT id, apelido, nome, to_char(nascimento, 'yyyy-mm-dd') as nascimento, stack FROM PESSOA WHERE id = %s"
            cursor.execute(sql, (id,))
            return cursor.fetchone()

def search_pessoa(term):
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            sql = "SELECT id, apelido, nome, to_char(nascimento, 'yyyy-mm-dd') as nascimento, stack FROM PESSOA WHERE termos like %(term)s LIMIT 50"
            cursor.execute(sql, {'term': '%{}%'.format(term)})
            return cursor.fetchall()

def count_pessoa():
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            sql = "SELECT count(1) FROM PESSOA"
            cursor.execute(sql)
            return cursor.fetchone()[0]