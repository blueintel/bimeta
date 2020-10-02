import grpc
import toml
import ssl


def get_connection(configFile):
    config = toml.load(configFile)
    # set up connection parms
    port = config["bimeta_client"]["ipPort"]
    host = config["bimeta_client"]["ipAddr"]
    key = config["bimeta_client"]["apikey"]
    # get ssl cert for channel...
    cert = ssl.get_server_certificate((host, port))
    cert_bytes = bytes(cert, 'utf-8')
    # Uhura, open a channel
    credentials = grpc.ssl_channel_credentials(cert_bytes)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)
    return channel, key
