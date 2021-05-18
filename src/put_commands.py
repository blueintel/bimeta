import os
import conn
import sys
import click

# import utility library
import utils

# import grpc libraries
from protobufs import recipient_pb2
from protobufs import recipient_pb2_grpc
from protobufs import org_pb2
from protobufs import org_pb2_grpc
# pylint: disable=import-error
import grpc
# pylint: enable=import-error


def put_user(config, email, name, org, title, clearance):
    # get the org id
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # make request
    recipient = recipient_pb2.Recipient(
        email=email, recipient_name=name, org_id=org_id, title=title, clearance=clearance
    )
    request = recipient_pb2.CreateRecipientRequest(recipient=recipient)
    # send request
    try:
        response = stub.CreateRecipient(request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response.recipient)


def put_config(config, org, name, file):
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
    request = org_pb2.CreateBimetaOrgConfigRequest(
        bimeta_org_config=org_config)
    # send request
    try:
        response = stub.CreateBimetaOrgConfig(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response.bimeta_org_config)


def put_tag(config, org, email, tags):
    if org == None and email == None:
        click.echo("Either --email or --org must be specified.")
        return

    if org != None and email != None:
        click.echo("Can only specify - -email or --org, not both.")
        return

    # org-wide tags
    if org != None:
        put_org_tag(config, org, tags)
    else:
        put_recipient_tag(config, email, tags)


def put_org_tag(config, org, tags):
    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # break out tags
    tag_list = utils.split_tags(tags)
    for tag_name in tag_list:
        # make request
        org_tag = org_pb2.BimetaOrgTag(
            org_id=org_id,
            tag_name=tag_name,
            tag_value=tag_list[tag_name]
        )
        request = org_pb2.CreateBimetaOrgTagRequest(bimeta_org_tag=org_tag)
        # send request
        try:
            response = stub.CreateBimetaOrgTag(
                request, metadata=[('biapikey', key)])
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
        else:
            utils.print_json(response.bimeta_org_tag)


def put_recipient_tag(config, email, tags):
    # validate email
    recipient_id = utils.get_recipient_id_by_email(config, email)
    if recipient_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # break out tags
    tag_list = utils.split_tags(tags)
    for tag_name in tag_list:
        # make request
        recipient_tag = recipient_pb2.RecipientTag(
            recipient_id=recipient_id,
            tag_name=tag_name,
            tag_value=tag_list[tag_name]
        )
        request = recipient_pb2.CreateRecipientTagRequest(
            recipient_tag=recipient_tag)
        # send request
        try:
            response = stub.CreateRecipientTag(
                request, metadata=[('biapikey', key)])
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
        else:
            utils.print_json(response.recipient_tag)
