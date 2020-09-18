import multiprocessing
import os

bind = os.getenv('SVC_BIND', '0.0.0.0:3000')
workers = int(os.getenv('SVC_CONCURRENCY', 1))
threads = int(os.getenv('SVC_THREADS', 10))