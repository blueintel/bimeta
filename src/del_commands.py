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


def del_user(config, email):
    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # make request
    request = recipient_pb2.DeleteRecipientByEmailRequest(email=email)
    # send request
    try:
        response = stub.DeleteRecipientByEmail(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response)


def del_config(config, org, name):
    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # make request
    request = org_pb2.DeleteBimetaOrgConfigRequest(
        org_id=org_id, config_name=name)
    # send request
    try:
        response = stub.DeleteBimetaOrgConfig(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response)


def del_tag(config, org, email, name):
    if org == None and email == None:
        click.echo("Either --email or --org must be specified.")
        return

    if org != None and email != None:
        click.echo("Can only specify - -email or --org, not both.")
        return

    # split up tag names
    tags = utils.split_tag_names(name)

    # org-wide tags
    if org != None:
        del_org_tag(config, org, tags)
    else:
        del_recipient_tag(config, email, tags)


def del_org_tag(config, org, tags):
    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    for tag_name in tags:
        # make request
        request = org_pb2.DeleteBimetaOrgTagRequest(
            org_id=org_id,
            tag_name=tag_name
        )
        # send request
        try:
            response = stub.DeleteBimetaOrgTag(
                request, metadata=[('biapikey', key)])
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
        else:
            utils.print_json(response)


def del_recipient_tag(config, email, tags):
    # validate email
    recipient_id = utils.get_recipient_id_by_email(config, email)
    if recipient_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    for tag_name in tags:
        # make request
        request = recipient_pb2.DeleteRecipientTagRequest(
            recipient_id=recipient_id,
            tag_name=tag_name
        )
        # send request
        try:
            response = stub.DeleteRecipientTag(
                request, metadata=[('biapikey', key)])
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
        else:
            utils.print_json(response)
