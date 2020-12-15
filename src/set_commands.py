import os
import conn
import click
import sys

# import utility library
import utils

# import grpc libraries
import recipient_pb2
import recipient_pb2_grpc
import org_pb2
import org_pb2_grpc
# pylint: disable=import-error
import grpc
# pylint: enable=import-error


def set_user(config, id, email, name, org, title, clearance):
    # validate has some data to update
    if email == None and name == None and org == None and title == None and clearance == None:
        click.echo(
            "Must specify at least one of --email, --name, --org, --title, or --clearance.")
        return

    # make update map
    update_map = {}
    if email:
        update_map["email"] = email
    if name:
        update_map["recipient_name"] = name
    if org:
        update_map["org_name"] = org
    if title:
        update_map["title"] = title
    if clearance:
        update_map["clearance"] = clearance
    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # make request
    request = recipient_pb2.UpdateRecipientRequest(
        recipient_id=id, update_map=update_map)
    # send request
    try:
        response = stub.UpdateRecipient(request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response)


def set_config(config, org, name, file):
    contents = None

    # validate file
    if file == "stdin":
        # read file from std in
        contents = sys.stdin.readlines()
    else:
        if os.path.exists(file):
            f = open(file)
            contents = f.read()
            f.close()
    if contents == None:
        click.echo("Unable to read file")
        return

    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # make request
    org_config = org_pb2.BimetaOrgConfig(
        org_id=org_id,
        config_name=name,
        content=contents
    )
    request = org_pb2.UpdateBimetaOrgConfigRequest(
        bimeta_org_config=org_config)
    # send request
    try:
        response = stub.UpdateBimetaOrgConfig(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response.bimeta_org_config)
