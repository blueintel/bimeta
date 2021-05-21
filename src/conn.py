import grpc
import toml
import ssl


def get_connection(configFile):
    config = toml.load(configFile)

    # do we have keys we need
    main = config.get("bimeta_client")
    if main is None:
        print("Unable to find bimeta_client key in config file. Please see bimeta_config.toml.example")
        exit(1)
    if not "port" in main and not "ipPort" in main:
        print("Unable to find port entry in config file under bimeta_client. Please see bimeta_config.toml.example")
        exit(1)
    if not "host" in main and not "ipAddr" in main:
        print("Unable to find host entry in config file under bimeta_client. Please see bimeta_config.toml.example")
        exit(1)
    if not "apikey" in main:
        print("Unable to find apikey entry in config file under bimeta_client. Please see bimeta_config.toml.example")
        exit(1)

    # set up connection parms
    port = main.get("port")
    if port is None:
        port = main.get("ipPort")
    host = main.get("host")
    if host is None:
        host = main.get("ipAddr")
    key = main["apikey"]
    # get ssl cert for channel...
    cert = ssl.get_server_certificate((host, port))
    cert_bytes = bytes(cert, 'utf-8')
    # Uhura, open a channel
    credentials = grpc.ssl_channel_credentials(cert_bytes)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)
    return channel, key
