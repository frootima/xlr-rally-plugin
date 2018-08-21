#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from rally.RallyClientUtil import RallyClientUtil

if rallyServer is None:
    print "No server provided."
    sys.exit(1)

if oid is None and owner_username is None and owner_name is None:
    print "One of User Object ID, Username or Name must be provided."
    sys.exit(1)

rally_client = RallyClientUtil.create_rally_client(rallyServer, username, password, oAuthKey)

if owner_username:
    oid = rally_client.get_user_object_id(owner_username=owner_username)
if owner_name:
    oid = rally_client.get_user_object_id(owner_name=owner_name)

properties = "{'owner': '%s'}" % str(oid)

rallyResult = rally_client.update_item(workspace, project, properties, userStoryFormattedId, rally_type)