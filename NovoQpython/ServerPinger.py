import random
import urllib.request
import ServerConfig


class Pinger:

    def __init__(self):
        self.sets = ServerConfig.Sets()
        self.host = []
        for server in self.sets.KEEP.split('|'):
            if server:
                self.host.append(server)

    def check(self):
        if self.host:
            try:
                request = urllib.request.Request(
                    'http://%s/' % self.host[random.randint(0, len(self.host) - 1)])
                request.add_header('Accept-Encoding', 'identity, *;q=0')
                request.add_header('Connection', 'close')
                proxy_handler = urllib.request.ProxyHandler(
                    {'http': '%s:%s' % ('127.0.0.1', self.sets.LPORT)})
                opener = urllib.request.build_opener(proxy_handler)
                urllib.request.install_opener(opener)
                urllib.request.urlopen(request)
            except:
                pass
