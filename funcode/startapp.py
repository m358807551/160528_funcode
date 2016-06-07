import sys
import os
from PyQt4.QtCore import *

def readFile(path):
    '''readFile.
    '''
    f = QFile(path)
    f.open(QFile.ReadOnly)
    inf = f.readAll()
    print inf 
    f.close()
    return inf

def writeFile(path, inf):
    '''
    '''
    f = QFile(path)
    f.open(QFile.WriteOnly | QFile.Text)
    f.writeData(inf)
    f.close()

def transform(come, to, replace):
    '''copy file from 'come' to 'to', and replace the specfic words.
    '''
    inf = readFile(come)

    for old, new in replace.items():
        inf.replace(QByteArray(old), QByteArray(new))

    writeFile(to, inf)

def setSettings():
    from funcode import settings
    
    global sAppName
    settings.INSTALLED_APPS = list(settings.INSTALLED_APPS)
    settings.INSTALLED_APPS.append('app_%s' % sAppName)
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS)

    settingNames = dir(settings)
    settingNames = [settingName for settingName in settingNames if settingName[0].isupper()]
    
    context = QStringList() 
    context.append('import os')
    for settingName in settingNames:
        exec("value = settings.%s" % settingName) 
        if type(value) == type(''):
            context.append("%s = '%s'" % (settingName, str(value)))
        else:
            context.append('%s = %s' % (settingName, str(value)))
    context = context.join('\r\n')

    writeFile('funcode/settings.py', context)

sAppName = sys.argv[1]
os.system('python manage.py startapp app_%s' % sAppName)
print 'create app successfull'

setSettings()
print 'add app to settings successful'

transform('temp\models.py', 'app_%s/models.py' % sAppName, {'MODEL':"M%s"%sAppName})
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
print 'migrate database successful'

transform('temp/views.py', 'app_%s/views.py' % sAppName, {'MODEL':"M%s"%sAppName, 'APP':sAppName})
print 'create views successful'

def setUrls():
    inf = readFile('funcode/urls.py')
    inf.prepend("from app_%s import views as app_%s_views\r\n" % (sAppName, sAppName))
    print inf.right(6)
    inf.remove(inf.size()-7, 10) # remove ')'
    inf.append("    url(r'^%s/index/', app_%s_views.index),\r\n" % (sAppName, sAppName))
    inf.append("    url(r'^%s/judge/', app_%s_views.judge),\r\n" % (sAppName, sAppName))
    inf.append("    )")
    writeFile('funcode/urls.py', inf)

setUrls()
print 'set urls successful'
