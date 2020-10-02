import os
import conn
import click
import datetime

# import utility library
import utils

# import grpc libraries
import org_pb2
import org_pb2_grpc
import recipient_pb2
import recipient_pb2_grpc
import github_pb2
import github_pb2_grpc

# pylint: disable=import-error
import grpc
# pylint: enable=import-error


def get_user(config, org, email, id):
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)

    # get user by org
    if email != None:
        # make request
        request = recipient_pb2.ReadRecipientByEmailRequest(
            email=email
        )
        # send request
        try:
            user = stub.ReadRecipientByEmail(
                request, metadata=[('biapikey', key)])
            utils.print_json(user)
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
            return
    elif id != None:
        # make request
        request = recipient_pb2.ReadRecipientByIDRequest(
            recipient_id=id
        )
        # send request
        try:
            user = stub.ReadRecipientByID(
                request, metadata=[('biapikey', key)])
            utils.print_json(user)
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
            return
    elif org != None:
        # validate org
        org_id = utils.get_org_id_by_name(config, org)
        if org_id == -1:
            return
        # make request
        request = recipient_pb2.ListRecipientsByOrgRequest(
            org_id=org_id
        )
        # send request
        try:
            users = stub.ListRecipients(request, metadata=[('biapikey', key)])
            for user in users:
                utils.print_json(user)
        except grpc.RpcError as e:
            utils.print_grpc_errors(e)
            return
    else:
        click.echo("One of email, id, or org must be specified")


def get_config(config, org, name):
    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)

    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # make request
    request = org_pb2.ReadBimetaOrgConfigRequest(
        org_id=org_id,
        config_name=name
    )
    # send request
    try:
        response = stub.ReadBimetaOrgConfig(
            request, metadata=[('biapikey', key)])
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
    else:
        utils.print_json(response.bimeta_org_config)


def get_tag(config, org, email):
    if org == None and email == None:
        click.echo("Either --email or --org must be specified.")
        return

    if org != None and email != None:
        click.echo("Can only specify - -email or --org, not both.")
        return

    # org-wide tags
    if org != None:
        get_org_tag(config, org)
    else:
        get_recipient_tag(config, email)


def get_org_tag(config, org):
    # validate org
    org_id = utils.get_org_id_by_name(config, org)
    if org_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = org_pb2_grpc.BimetaOrgServiceStub(channel)
    # make request
    request = org_pb2.ListBimetaOrgTagRequest(org_id=org_id)
    # send request
    try:
        response = stub.ListBimetaOrgTag(request, metadata=[('biapikey', key)])
        for tag in response:
            utils.print_json(tag.bimeta_org_tag)
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)


def get_recipient_tag(config, email):
    # validate email
    recipient_id = utils.get_recipient_id_by_email(config, email)
    if recipient_id == -1:
        return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = recipient_pb2_grpc.RecipientServiceStub(channel)
    # make request
    request = recipient_pb2.ListRecipientTagRequest(recipient_id=recipient_id)
    # send request
    try:
        response = stub.ListRecipientTag(request, metadata=[('biapikey', key)])
        for tag in response:
            utils.print_json(tag.recipient_tag)
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)


def get_github(config, org, begin, end, viewed):
    # set default start/end date
    to_tm = datetime.datetime.utcnow()
    from_tm = to_tm - datetime.timedelta(hours=24)
    # if date provided, time to work with them
    if begin != None:
        try:
            from_tm = datetime.datetime.fromisoformat(begin)
        except:
            click.echo(
                f"Unable to convert {begin} (does it match ISO format?)")
            return
    if end != None:
        try:
            to_tm = datetime.datetime.fromisoformat(end)
        except:
            click.echo(
                f"Unable to convert {begin} (does it match ISO format?)")
            return

    # open grpc channel
    channel, key = conn.get_connection(config)
    # connect to grpc stub
    stub = github_pb2_grpc.GithubServiceStub(channel)
    # make request
    request = github_pb2.ListAlertsRequest(
        org=org,
        viewed=viewed,
        startdate=from_tm.isoformat(),
        enddate=to_tm.isoformat()
    )
    utils.print_json(request)
    # send request
    try:
        response = stub.ListAlerts(request, metadata=[('biapikey', key)])
        for alert in response:
            utils.print_json(alert.Alerts)
    except grpc.RpcError as e:
        utils.print_grpc_errors(e)
