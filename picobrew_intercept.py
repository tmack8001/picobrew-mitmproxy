from mitmproxy import http
from mitmproxy import ctx

#picobrew_pico_host = "picobrew-pico.local"
picobrew_server = {
  #"host": "tmack.ngrok.io",
  "host": "localhost",
  "scheme": "http",
  #"port": "8080"
  "port": 80
}

def request(flow: http.HTTPFlow) -> None:
  ctx.log( flow.request.pretty_host )
  if flow.request.pretty_host.endswith("picobrew.com"):
    ctx.log( flow.request.path )
    flow.request.host = picobrew_server['host']
    flow.request.port = picobrew_server['port']
    flow.request.scheme = picobrew_server['scheme']
    flow.request.headers['Host'] = picobrew_server['host']
