# wekan-api

This service provides a RESTful API for a self-hosted [Wekan](https://wekan.io/) installation.

Please note that this is an independent, server-side application that runs *alongside* Wekan, since it *directly accesses* the MongoDB database used by Wekan as a datastore. This application does not attempt to communicate directly with the Wekan service, since Wekan [does not provide a programmatic interface](https://github.com/wekan/wekan/issues/166) for performing actions that can be done in the web interface.

`wekan-api` attempts to address the above problem by providing a JSON-based HTTP API for querying Wekan's datastore with natural, familiar semantics (e.g. with boards, lists, and cards).

**`wekan-api` currently only provides read-only endpoints.**

## API Documentation

Please see the `docs/` directory of this repository for documentation of each available endpoint.

## Installation and Usage

#### Prerequisites

1. You should have access to the MongoDB server used by Wekan (i.e. the host, port, and name of the database).
2. You should have a Python environment available.

#### Development

```bash
$ git clone https://github.com/LINKIWI/wekan-api.git .
$ virtualenv env
$ source env/bin/activate
# Edit config/database.json to specify the Wekan database location.
# You can leave the default settings (localhost:27017/wekan) if you never set a custom one.
$ make bootstrap  # Install dependencies
$ make serve  # Starts the API server at localhost:5000
```

#### Production

The following assumes an environment with Apache and `mod_wsgi`.

```bash
$ git clone https://github.com/LINKIWI/wekan-api.git .
$ virtualenv env
$ source env/bin/activate
# Edit config/database.json to specify the Wekan database location.
# You can leave the default settings (localhost:27017/wekan) if you never set a custom one.
$ make bootstrap  # Install dependencies
```

Add the following (or a variation thereof) to your Apache configuration.

```apache
<VirtualHost *:80>
    ServerName api.wekan.example.com
    DocumentRoot /path/to/wekan-api
    WSGIScriptAlias / /path/to/wekan-api/wekan_api.wsgi
</VirtualHost>
```

To effect changes:

```bash
sudo service apache2 reload
```

See if it works:

```bash
$ curl http://api.wekan.example.com/status
{
  "message": null,
  "status": "OK",
  "success": true
}
```

`wekan-api` does not ship with a service-level authentication mechanism. **It is strongly recommended you secure this virtual host with some authentication layer.** Adding HTTP basic authentication is the most straightforward way to do this. In my personal deployment I use an SSO system with [`apache-auth`](https://github.com/LINKIWI/apache-auth).
