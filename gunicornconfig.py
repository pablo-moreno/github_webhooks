# Thanks to @sorinsinz

import multiprocessing

bind = '0.0.0.0:4567'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
threads = 50
timeout = 15
max_requests = 1000


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")
