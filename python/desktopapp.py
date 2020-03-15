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
