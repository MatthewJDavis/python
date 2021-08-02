# ms_graph_permissions

Simple python script to get the Microsoft Graph role and scope permission details that outputs to terminal or in a markdown table format.

## Requirements

Requires an Azure AD application registered with Directory.Read.All (id: 7ab1d382-f21e-4acd-a863-ba3e13f7da61) application permissions with admin consent granted.

Uses the requests package.

```bash
pip install -r requirements.txt 
```

The application and tenant details should be set via environment variables.

```bash
export CLIENTID=''
export TENANTID=''
 export SECRET=''
```

## Running the program

```bash
python ms_graph_permissions.py
```

```bash
# outputs two file roles.md and scopes.md in markdown table format
python ms_graph_permissions.py --output markdown
```
