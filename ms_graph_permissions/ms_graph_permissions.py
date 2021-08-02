""" Script to get the Microsoft Graph role and scope details including IDs.
    Calls the Microsoft Graph to retrieve the data. Formats and outputs to terminal or two files, roles.md # pylint: disable=line-too-long
    and scopes.md in markdown format.
    Can set to output markdown files with --output markdown arg passed.
 """
import argparse
import os
import requests
from requests.exceptions import HTTPError

MS_GRAPH_APP_ID = '00000003-0000-0000-c000-000000000000'
GRAPH_URL = 'https://graph.microsoft.com'

def token(token_endpoint, token_headers, token_body):
    """ Get bearer access token from AzureAD application """
    try:
        token_response = requests.post(
            url=token_endpoint, headers=token_headers, data=token_body)
        token_response.raise_for_status  # pylint: disable=pointless-statement
        return token_response.json()['access_token']
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


def graph_query(query_url, query_headers):
    """ Send a query to the MS Graph """
    try:
        query_response = requests.get(url=query_url, headers=query_headers)
        query_response.raise_for_status  # pylint: disable=pointless-statement
        return query_response.json()['value'][0]
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')


# def search_roles(query):
#     return [k for k in sorted_roles if f'{query}' in k['value']]


def output_role(role):
    """ Custom output of the role to screen """
    print(f"Name: {role['value']}")
    print(f"ID: {role['id']}")
    print(f"displayName: {role['displayName']}")
    print(f"description: {role['description']}\n")


def output_scope(scope):
    """ Custom output of the scope to screen """
    print(f"Name: {scope['value']}")
    print(f"ID: {scope['id']}")
    print(f"AdminName: {scope['adminConsentDisplayName']}")
    print(f"AdminDescription: {scope['adminConsentDescription']}")
    print(f"UserName: {scope['userConsentDisplayName']}")
    print(f"UserDescription: {scope['userConsentDescription']}")


def output_role_markdown(role):
    """ Return role details in markdown table format """
    return f"| {role['value']} | {role['id']} | {role['displayName']} | {role['description']} |"


def output_scope_markdown(scope):
    """ Return scope details in markdown table format """
    return f"| {scope['value']} | {scope['id']} | {scope['adminConsentDisplayName']} | \
             {scope['adminConsentDescription']} | {scope['userConsentDisplayName']} | {scope['userConsentDescription']} " #pylint: disable=line-too-long


def main():
    """ Main entry point for the script """

    parser = argparse.ArgumentParser(
        description='Get MS Graph Permission details.')

    parser.add_argument(
        '--output', help="Output can be to terminal or to file with markdown. --output markdown")
    args = parser.parse_args()

    os.getenv('SECRET')
    token_endpoint = 'https://login.microsoftonline.com/' + \
        os.getenv('TENANTID') + '/oauth2/token'

    token_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_body = {
        "grant_type": "client_credentials",
        "client_id": os.getenv('CLIENTID'),
        "client_secret": os.getenv('SECRET'),
        "resource": GRAPH_URL
    }
    access_token = token(token_endpoint, token_headers, token_body)
    query_url = f"https://graph.microsoft.com/v1.0/servicePrincipals?$filter=appId eq '{MS_GRAPH_APP_ID}'&$select=appRoles, oauth2PermissionScopes" # pylint: disable=line-too-long

    query_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    graph_response = graph_query(query_url, query_headers)
    sorted_roles = sorted(graph_response['appRoles'],
                          key=lambda role: role['value'])

    sorted_scopes = sorted(graph_response['oauth2PermissionScopes'],
                           key=lambda scope: scope['value'])

    role_title = "| Role Name | ID | Display Name | Description | \n|--- | --- | --- | ---|\n"
    scope_title = "| Scope Name | ID | Admin Display Name | Admin Description | User Display Name | User Description | \n | --- | --- | --- | ---| --- | ----|\n" # pylint: disable=line-too-long

    if args.output == 'markdown':
        with open('roles.md', 'w') as writer:
            writer.write(role_title)
            for role in sorted_roles:
                writer.write(f"{output_role_markdown(role)}\n")

        with open('scopes.md', 'w') as writer:
            writer.write(scope_title)
            for scope in sorted_scopes:
                writer.write(f"{output_scope_markdown(scope)}\n")
    else:
        for role in sorted_roles:
            output_role(role)
        for scope in sorted_scopes:
            output_scope(scope)


if __name__ == "__main__":
    main()
