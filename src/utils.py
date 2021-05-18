import os
import conn
import sys
import click

# import grpc libraries
# pylint: disable=import-error
import grpc
from google.protobuf.json_format import MessageToJson
# pylint: enable=import-error
# pylint: enable=import-error
from protobufs import org_pb2
from protobufs import org_pb2_grpc
from protobufs import recipient_pb2
from protobufs import recipient_pb2_grpc


def print_grpc_errors(e):
    # ouch!
    # lets print the gRPC error message
    # which is "Length of `Name` cannot be more than 10 characters"
    print(e.details())
    # lets access the error code, which is `INVALID_ARGUMENT`
    # `type` of `status_code` is `grpc.StatusCode`
    # status_code = e.code()
    # should print `INVALID_ARGUMENT`
    # print(status_code.name)
    # should print `(3, 'invalid argument')`
    # print(status_code.value)
    # want to do some specific action based on the error?
    # if grpc.StatusCode.INVALID_ARGUMENT == status_code:
    #     # do your stuff here
    #     pass


def get_org_id_by_name(config, orgname):
    # build request
    request = org_pb2.ReadBimetaOrgByNameRequest(
        org_name=orgname
    )

    # open channel
    channel, key = conn.get_connection(config)
    # connect to stub
    org_client = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # make request
    try:
        response = org_client.ReadBimetaOrgByName(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        print_grpc_errors(e)
        return -1
    else:
        return response.bimeta_org.id


def get_recipient_id_by_email(config, email):
    # open channel
    channel, key = conn.get_connection(config)
    # connect to stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # build request
    request = recipient_pb2.ReadRecipientByEmailRequest(
        email=email
    )
    # submit request
    try:
        response = stub.ReadRecipientByEmail(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        print_grpc_errors(e)
        return -1
    else:
        return response.recipient.id


def print_json(message):
    json = ""
    # Removes all 3 types of line breaks
    try:
        json = MessageToJson(message)
    except:
        print(f"Unable to format result as json:\n{message}")
        return

    json = json.replace("\r", "")
    json = json.replace("\n", "")
    click.echo(json)


# Method tags a list such as tag1=value1,tag2=value2,tag3=value3
#  and returns a dictionary where dict[tag1] = value1, etc.
def split_tags(tags):
    final_list = {}

    if tags == None:
        return final_list
    first = tags.split(',')
    for item in first:
        second = item.split('=')
        if len(second) == 2:
            final_list[second[0].strip()] = second[1].strip()
    return final_list


# Method tags a string such as tag1,tag2,tag3
#  and returns a list [tag1, tag2, tag3]
def split_tag_names(tags):
    final_list = []

    if tags == None:
        return final_list
    first = tags.split(',')
    for item in first:
        final_list.append(item.strip())
    return final_list
