

docker run --name test -h test -p 9043:9043 -p 9443:9443 -d ibmcom/websphere-traditional:profile
https://ip172-18-0-38-bk9ahlt35dvg00e32s8g-9043.direct.labs.play-with-docker.com:9043/ibm/console/logon.jsp
https://localhost:9043/ibm/console/login.do?action=secure
https://192.168.99.100:9043/ibm/console/login.do?action=secure
/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh
username: wsadmin
passwd: $(docker exec -it test cat /tmp/PASSWORD)

AdminApp.install('fullpath/yourApp.ear', ['-MapWebModToVH', [['.*', '.*', 'default_host']]])
AdminConfig.save()

## Restart
AdminControl.invoke(AdminControl.queryNames('WebSphere:*,type=Server,node=%s,process=%s' % ('DefaultNode01', 'server1')), 'restart')
## Stop
AdminControl.invoke(AdminControl.queryNames('WebSphere:*,type=Server,node=%s,process=%s' % ('DefaultNode01', 'server1')), 'stop')
# now your server is stopped, you can do any cleanup
# and then start the server with NodeAgent
## Start
AdminControl.invoke(AdminControl.queryNames('WebSphere:*,type=NodeAgent,node=%s' % 'DefaultNode01'), 'launchProcess', ['server1'], ['java.lang.String'])