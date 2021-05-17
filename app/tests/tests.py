# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:03
@Author     :liuhuan
@verssion   :v1.0
@effect     :测试文件
"""
import redis

redis_db = redis.Redis(host='localhost', port=6379,
             db=0, password=None, socket_timeout=None,
             socket_connect_timeout=None,
             socket_keepalive=None, socket_keepalive_options=None,
             connection_pool=None, unix_socket_path=None,
             encoding='utf-8', encoding_errors='strict',
             charset=None, errors=None,
             decode_responses=False, retry_on_timeout=False,
             ssl=False, ssl_keyfile=None, ssl_certfile=None,
             ssl_cert_reqs='required', ssl_ca_certs=None,
             ssl_check_hostname=False,
             max_connections=None, single_connection_client=False,
             health_check_interval=0, client_name=None, username=None)

res = redis_db.set("10.10.11.30","youzi")
print(res)