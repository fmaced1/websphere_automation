import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

appName = sys.argv[0]
nodeName = sys.argv[1]
serverName = sys.argv[2]
path2app = sys.argv[3]

class deploy():
  
  def __init__(self, appName, nodeName, serverName, path2app):
    self.appName = appName
    self.nodeName = nodeName
    self.serverName = serverName
    self.path2app = path2app

  def stopApplication(self):
    
    print '\n Stop Application'
    print 'appName: '+self.appName
    print 'Get details from app: ['+self.appName+']'
    self.getDetailsFromApp()

    try:
      AdminControl.invoke(self.appMgr, 'stopApplication', self.appName)
    except:
      print 'Error - %s' % sys.exc_info()

  def startApplication(self):

    print '\n --> Start Application'
    print ' appName: '+self.appName

    #print 'Get details from app: ['+self.appName+']'
    #getDetailsFromApp()

    print 'Lets start ['+self.appName+']'
    try:
      #AdminControl.invoke(self.appMgr, 'startApplication', self.appName)
      AdminControl.invoke(AdminControl.queryNames('type=ApplicationManager,process='+self.serverName+',*'),'startApplication',self.appName)
    except:
      print 'Error - %s' % sys.exc_info()

  def getDetailsFromApp(self):
    
    print '\n --> Get Details From App: '
    print ' nodeName: '+self.nodeName+'\n appName: '+self.appName+'\n serverName: '+self.serverName+' path to app: '+self.path2app

    try:
      self.appMgr = AdminControl.queryNames('type=ApplicationManager,node='+self.nodeName+',process='+self.serverName+',*')
      self.appDetails = AdminControl.completeObjectName('type=Application,name='+self.appName+',*')
      print ' --> appMgr: '+self.appMgr+'\n appDetails: '+self.appDetails
    
      if len(self.appDetails) > 0:
        print '['+self.appName+'] is started lets stop'
        stopApplication()

    except:
      print 'Error - %s' % sys.exc_info()


  def deployApp(self):
    
    print '\n --> Deploy App:'
    print ' appName: '+self.appName+'\n path to app: '+self.path2app
    
    try:
      AdminApp.install(self.path2app, ['-MapWebModToVH', [['.*', '.*', 'default_host']]])
      AdminConfig.save()
    except:
      print 'Error to deploying the app: '+self.appName+' with path '+self.path2app+'.'


d = deploy(appName, nodeName, serverName, path2app)
#d.getDetailsFromApp()
#d.stopApplication()
d.deployApp()
d.startApplication()