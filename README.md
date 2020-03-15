# ELEMENTS PROJECT

> * alias b-dae="bitcoind -datadir=/media/otsarri/nodedisk/elements/network/bitcoindir"
> * alias b-cli="bitcoin-cli -datadir=/media/otsarri/nodedisk/elements/network/bitcoindir"
> * alias alice-e1-dae="/media/otsarri/nodedisk/elements/src/elementsd -datadir=/media/otsarri/nodedisk/elements/network/elementsdir1"
> * alias alice-e1-cli="/media/otsarri/nodedisk/elements/src/elements-cli -datadir=/media/otsarri/nodedisk/elements/network/elementsdir1"
> * alias bob-e2-dae="/media/otsarri/nodedisk/elements/src/elementsd -datadir=/media/otsarri/nodedisk/elements/network/elementsdir2"
> * alias bob-e2-cli="/media/otsarri/nodedisk/elements/src/elements-cli -datadir=/media/otsarri/nodedisk/elements/network/elementsdir2"
> * alias e1-qt="/media/otsarri/nodedisk/elements/src/qt/elements-qt -datadir=/media/otsarri/nodedisk/elements/network/elementsdir1"
> * alias e2-qt="/media/otsarri/nodedisk/elements/src/qt/elements-qt -datadir=/media/otsarri/nodedisk/elements/network/elementsdir2"

## Start bitcoin daemon

> * b-dae
> * b-cli -getinfo

## Start elements daemons

> * alice-e1-dae
> * bob-e2-dae

## Desktop application (Python)

Set up and Activate virtualenv:

    virtualenv venv
    source venv/bin/activate

Use pip to install python-bitcoinrpc within the environment:

    pip3 install python-bitcoinrpc

Create a new file named desktopapp.py and paste the code below into it.

        from __future__ import print_function
        from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

        rpc_port = 18884
        rpc_user = 'user1'
        rpc_password = 'password1'

        try:
            rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
            
            result = rpc_connection.getwalletinfo()
            
            print(result["balance"]["bitcoin"])
        except JSONRPCException as json_exception:
            print("A JSON RPC Exception occured: " + str(json_exception))
        except Exception as general_exception:
            print("An Exception occured: " + str(general_exception))

Execute:
    python3 desktopapp.py

When finished, deactivate vitualenv:
    deactivate

## Web application (Python)

Install Flask web application framework:

    pip3 install Flask

Create a new file named webapp.py and paste the code below into it.

from flask import Flask
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

    app = Flask(__name__)
    
    @app.route("/")
    def elements():
        rpc_port = 18884
        rpc_user = 'user1'
        rpc_password = 'password1'

        try:
            rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
        
            result = rpc_connection.getwalletinfo()
        
        except JSONRPCException as json_exception:
            return "A JSON RPC Exception occured: " + str(json_exception)
        except Exception as general_exception:
            return "An Exception occured: " + str(general_exception)

        return str(result['balance']['bitcoin'])
    
    if __name__ == "__main__":
        app.run()

Start the web server and execute the code:

    FLASK_APP=webapp.py flak run
