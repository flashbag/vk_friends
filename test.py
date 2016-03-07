from settings import my_id, m_friends_dct
from lib import request_url, make_targets, parts, save_or_load

targets_list = 20071729,35423928,9954958
targets = make_targets(targets_list)

print( "\n" )
print ( "targets:" )
print ( targets )

req_url = request_url('execute.getMutual', 'src=%s&targets=%s' % (my_id, targets), access_token=True)

print( "\n" )
print( req_url )

req_obj = requests.get(req_url)

print( "\n" )
print ( req_obj )

response = req_obj.json()

print( "\n" )
print ( response )

save_or_load(m_friends_dct['file'], True, targets_list)
