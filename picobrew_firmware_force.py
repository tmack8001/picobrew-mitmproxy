from mitmproxy import http
from mitmproxy import ctx

def response(flow: http.HTTPFlow) -> None:
    ctx.log.info('script executing ' + flow.request.host + ' - ' + flow.request.path)
    if flow.request.pretty_host == "www.picobrew.com":
        ctx.log.info('adding response header')
        flow.response.headers['intercepted'] = 'mitmproxy'

    # https://www.picobrew.com/Vendors/input.cshtml?type=ZState&token=<token>
    if flow.request.pretty_host == "www.picobrew.com":
        if flow.request.path.startswith("/Vendors/input.cshtml") and "ZState" in flow.request.path:
            ctx.log.info('intercepting and modifying ZState response')        
            if "0.0.119" in flow.request.text:
                ctx.log.info('don\'t allow a server forced downgrade');
                flow.response.content = flow.response.content.replace(b"\"UpdateAddress\":\"https://picobrewcontent.blob.core.windows.net/firmware/zseries/zseries_0_0_116.bin\"", b"\"UpdateAddress\":\"-1\"")
                flow.response.content = flow.response.content.replace(b"\"IsUpdated\":false", b"\"IsUpdated\":true")
            else:
                ctx.log.info('force an upgrade to latest known firmware 0.0.119')
                # TODO (tmack) load firmware from non Picobrew server address
                flow.response.content = flow.response.content.replace(b"\"UpdateAddress\":\"https://picobrewcontent.blob.core.windows.net/firmware/zseries/zseries_0_0_116.bin\"", b"\"UpdateAddress\":\"UpdateAddress\":\"https://picobrewcontent.blob.core.windows.net/firmware/zseries/zseries_0_0_119.bin\"")
                flow.response.content = flow.response.content.replace(b"\"IsUpdated\":true", b"\"IsUpdated\":false")
