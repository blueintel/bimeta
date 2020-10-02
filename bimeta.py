#pylint: disable=function-redefined
import click
import os
import conn

#import commands
import get_commands
import put_commands
import set_commands
import del_commands

# global variables
__config = f"{os.getcwd()}/bimeta_config.toml"   # config file location

# set up arguments for "app"


@click.group()
@click.option('--config', help="Filename of the configuration file. Default is\nbimeta_config.toml in the executable directory",
              default=f"{os.getcwd()}/bimeta_config.toml")
def cli(config):
    global __config

    """Bimeta Client Application"""
    __config = config


# Set up arguments for "PUT" commands
@cli.group()
def put():
    """Put Commands"""
    pass


@put.command()
@click.option('--email', '-e', help='Email address of user', required=True)
@click.option('--name', '-n', help='Name of new user', required=True)
@click.option('--org', '-o', help='Name of organization user belongs to', required=True)
@click.option('--title', '-t', help='Title of user', required=True)
@click.option('--clearance', '-c', type=click.Choice(["black", "red", "amber", "green", "white"]), help='Clearance of user', required=True)
def user(email, name, org, title, clearance):
    """Create new user"""
    global __config
    put_commands.put_user(__config, email, name, org, title, clearance)


@put.command()
@click.option('--org', '-o', help='Name of organization', required=True)
@click.option('--name', '-n', help='Name of configuration file', required=True)
@click.option('--file', '-f', help='Filename of configuration file. (use stdin as the filename\nto read the configuration file from stdin)', required=True)
def config(org, name, file):
    """Create configuration"""
    global __config
    put_commands.put_config(__config, org, name, file)


@put.command()
@click.option('--org', '-o', help='Name of organization to add comma delimited tag(s) to\n(mutually exclusive with --email)')
@click.option('--email', '-e', help='Email of user to add comma delimited tags to(mutually\nexclusive with --org)')
@click.option('--tags', '-t', help='Comma delimited list of tags to add to org/user in the\nformat "tagname1=value1,tagname2=value2,..."', required=True)
def tag(org, email, tags):
    """Create/update tags for orgs/users"""
    global __config
    put_commands.put_tag(__config, org, email, tags)


# Set up arguments for "GET" commands
@cli.group()
def get():
    """Get commands"""
    pass


@get.command()
@click.option('--org', '-o', help='Get all users belonging to org')
@click.option('--email', '-e', help='Get information about user with the specified email')
@click.option('--id', '-i', type=int, help='Get information about user with the specified id')
def user(org, email, id):
    """Get user information"""
    global __config
    get_commands.get_user(__config, org, email, id)


@get.command()
@click.option('--org', '-o', help='Get configuration belonging to org', required=True)
@click.option('--name', '-n', help='Get configuration with the specified name', required=True)
def config(org, name):
    """Get configuration information"""
    global __config
    get_commands.get_config(__config, org, name)


@get.command()
@click.option('--org', '-o', help='Get all tags belonging to org')
@click.option('--email', '-e', help='Get all tags belonging to user with the specified email')
def tag(org, email):
    """Get tags"""
    global __config
    get_commands.get_tag(__config, org, email)


@get.command()
@click.option('--org', '-o', help='Get alerts for this org; defaults to user org', default="")
@click.option('--start', '-s', help='Starting date for alerts. In ISO format "YYYY-MM-DDTHH:MM:SS"')
@click.option('--end', '-e', help='Ending date for alerts defaults to now. In ISO format "YYYY-MM-DDTHH:MM:SS"')
@click.option('--viewed', '-v', type=bool, help='Include previously viewed alerts', default=False, is_flag=True)
def github_alerts(org, start, end, viewed):
    """Get github search alerts"""
    global __config
    get_commands.get_github(__config, org, start, end, viewed)


# Set up arguments for "GET" commands
@cli.group()
def set():
    """Set commands"""
    pass


@set.command()
@click.option('--id', '-i', type=int, help='Numeric ID of user to be updated', required=True)
@click.option('--email', '-e', help='Email address of user')
@click.option('--name', '-n', help='Name of user')
@click.option('--org', '-o', help='Name of organization user belongs to')
@click.option('--title', '-t', help='Title of user')
@click.option('--clearance', '-c', type=click.Choice(["black", "red", "amber", "green", "white"]), help='Clearance of user')
def user(id, email, name, org, title, clearance):
    """Update an existing user. Must use id to update user fields."""
    global __config
    set_commands.set_user(__config, id, email, name, org, title, clearance)


@set.command()
@click.option('--org', '-o', help='Name of organization', required=True)
@click.option('--name', '-n', help='Name of configuration file', required=True)
@click.option('--file', '-f', help='Filename of configuration file', required=True)
def config(org, name, file):
    """"Update configuration"""
    global __config
    set_commands.set_config(__config, org, name, file)


# Set up arguments for "GET" commands
@cli.group("del")
def del_():
    """Delete commands"""
    pass


@del_.command()
@click.option('--email', '-e', help='Email of user to delete', required=True)
def user(email):
    """Delete a user"""
    global __config
    del_commands.del_user(__config, email)


@del_.command()
@click.option('--org', '-o', help='Org whose configuration to delete', required=True)
@click.option('--name', '-n', help='Name of configuration to delete', required=True)
def config(org, name):
    """Delete configuration information"""
    global __config
    del_commands.del_config(__config, org, name)


@del_.command()
@click.option('--org', '-o', help='Org whose tag to delete. Mutually exclusive with --email')
@click.option('--email', '-e', help='Email of user whose tag to delete. Mutually exclusive\nwith --org')
@click.option('--name', '-n', help='Name(s) of tag to delete(comma delimited)', required=True)
def tag(org, email, name):
    """Delete tag information"""
    global __config
    del_commands.del_tag(__config, org, email, name)


# pylint: disable=no-value-for-parameter)
if __name__ == '__main__':
    cli()
