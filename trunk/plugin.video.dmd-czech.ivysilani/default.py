# -*- coding: utf-8 -*-
import urllib2,urllib,re,os,time,datetime,json
from parseutils import *
from urlparse import urlparse
import xbmcplugin,xbmcgui,xbmcaddon

__baseurl__ = 'http://www.ceskatelevize.cz/ivysilani'
__dmdbase__ = 'http://iamm.netuje.cz/xbmc/stream/'
_UserAgent_ = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
swfurl='http://img8.ceskatelevize.cz/libraries/player/flashPlayer.swf?version=1.43'
addon = xbmcaddon.Addon('plugin.video.dmd-czech.ivysilani')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id='plugin.video.dmd-czech.ivysilani')
home = __settings__.getAddonInfo('path')
REV = os.path.join( profile, 'list_revision')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
nexticon = xbmc.translatePath( os.path.join( home, 'nextpage.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
page_pole_url = []
page_pole_no = []

def OBSAH():
    addDir('Podle abecedy',__baseurl__+'/podle-abecedy/',2,icon)
    addDir('Podle kategorie',__baseurl__,1,icon)
    #addDir('Podle datumu',__baseurl__+'/podle-data-vysilani/',5,icon)
    addDir('Živé iVysílání',__baseurl__+'/ajax/liveBox.php',4,icon)

def KATEGORIE():
    addDir('Filmy',__baseurl__+'/filmy/',3,icon)
    addDir('Seriály',__baseurl__+'/serialy/',3,icon)
    addDir('Dokumenty',__baseurl__+'/dokumenty/',3,icon)   
    addDir('Sport',__baseurl__+'/sportovni/',3,icon)   
    addDir('Hudba',__baseurl__+'/hudebni/',3,icon)   
    addDir('Zábava',__baseurl__+'/zabavne/',3,icon)   
    addDir('Děti a mládež',__baseurl__+'/deti/',3,icon)   
    addDir('Vzdělání',__baseurl__+'/vzdelavaci/',3,icon)   
    addDir('Zpravodajství',__baseurl__+'/zpravodajske/',3,icon)   
    addDir('Publicistika',__baseurl__+'/publicisticke/',3,icon)   
    addDir('Magazíny',__baseurl__+'/magaziny/',3,icon)   
    addDir('Náboženské',__baseurl__+'/nabozenske/',3,icon)   
    addDir('Všechny',__baseurl__+'/zanr-vse/',3,icon)   

def LIVE_OBSAH(url):
    doc = read_page(url)
    items = doc.find('div', 'clearfix')
    for item in items.findAll('div', 'channel'):
            #name_a = item.find('p')
            try:
                name_a = item.find('a') 
                name = name_a.getText(" ").encode('utf-8')
                url = 'http://www.ceskatelevize.cz'+str(item.a['href'])
                thumb = str(item.img['src'])
            except:
                name = 'Právě teď běží pořad, který nemůžeme vysílat po internetu.'
                thumb = 'http://img7.ceskatelevize.cz/ivysilani/gfx/empty/noLive.png'
            #print name, thumb, url
            addDir(name,url,10,thumb)

def ABC(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    httpdata = response.read()
    response.close()
    match = re.compile('<a class="pageLoadAjaxAlphabet" href="(.+?)" rel="letter=.+?"><span>(.+?)</span></a>').findall(httpdata)
    for link,name in match:
        #print name,__baseurl__+link
        addDir(name,'http://www.ceskatelevize.cz'+link,3,icon)

def CAT_LIST(url):
    doc = read_page(url)
    items = doc.find('div','clearfix programmesList')    
    for item in items.findAll('a'):
        name = item.getText(" ").encode('utf-8')
        link = str(item['href'])
        #print name,__baseurl__+link
        addDir(name,'http://www.ceskatelevize.cz'+link,6,icon)

def DATUM(url):
    addDir(name,link,6,icon)


def VIDEO_LIST(url):
    link = url
    if not re.search('dalsi-casti',url):
        link = url + 'dalsi-casti/'
    doc = read_page(link)
    if re.search('Bonusy',str(doc),re.U):
        bonuslink = url+'bonusy/'
        if re.search('dalsi-casti',url):
            bonusurl = re.compile('(.+?)dalsi-casti/?').findall(url)
            bonuslink = bonusurl[0]+'bonusy/'
        addDir('Bonusy',bonuslink,7,nexticon)
        print 'Bonusy = True - ' + url +'bonusy/'
    items = doc.find('ul','clearfix content')
    if re.search('Ouha',str(items),re.U):
        bonuslink = url+'bonusy/'
        BONUSY(bonuslink)
    for item in items.findAll('li', 'itemBlock clearfix'):
        try:
            name_a = item.find('h3')
            name_a = name_a.find('a')
            name = name_a.getText(" ").encode('utf-8')
            if len(name) < 2:
                name = 'Titul bez názvu'
            popis_a = item.find('p') 
            popis = popis_a.getText(" ").encode('utf-8')
            popis = re.sub('mdash;','-',popis)
            if re.match('Reklama:',popis, re.U):
                popis = 'Titul bez názvu'
            url = 'http://www.ceskatelevize.cz'+str(item.a['href'])
            url = re.sub('porady','ivysilani',url)
            thumb = str(item.img['src'])
            #print name+' '+popis, thumb, url
            addDir(name+' '+popis,url,10,thumb)
        except:
            #print 'Licence pro internetové vysílání již skončila.', thumb, 'http://www.ceskatelevize.cz'
            addDir('Licence pro internetové vysílání již skončila.',link,60,thumb)
               
    try:
        pager = doc.find('div', 'pagingContent')
        act_page_a = pager.find('td','center')
        act_page = act_page_a.getText(" ").encode('utf-8')
        act_page = act_page.split()
        next_page_i = pager.find('td','right')
        #print act_page,next_page_i
        next_url = next_page_i.a['href']
        next_label = 'Další strana (Zobrazena videa '+act_page[0]+'-'+act_page[2]+' ze '+act_page[4]+')'
        #print next_label,next_url
        addDir(next_label,'http://www.ceskatelevize.cz'+next_url,6,nexticon)
    except:
        print 'STRANKOVANI NENALEZENO!'

def BONUSY(link):
    doc = read_page(link)
    items = doc.find('ul','clearfix content')
    if re.search('Ouha',str(items),re.U):
        link = url+'bonusy/'
        BONUSY(link)
    for item in items.findAll('li', 'itemBlock clearfix'):
        name_a = item.find('h3')
        name_a = name_a.find('a')
        name = name_a.getText(" ").encode('utf-8')
        if len(name) < 2:
            name = 'Titul bez názvu'
        url = 'http://www.ceskatelevize.cz'+str(item.a['href'])
        url = re.sub('porady','ivysilani',url)
        thumb = str(item.img['src'])
        #print name, thumb, url
        addDir(name,url,10,thumb)
    try:
        pager = doc.find('div', 'pagingContent')
        act_page_a = pager.find('td','center')
        act_page = act_page_a.getText(" ").encode('utf-8')
        act_page = act_page.split()
        next_page_i = pager.find('td','right')
        #print act_page,next_page_i
        next_url = next_page_i.a['href']
        next_label = 'Další strana (Zobrazena videa '+act_page[0]+'-'+act_page[2]+' ze '+act_page[4]+')'
        #print next_label,next_url
        addDir(next_label,'http://www.ceskatelevize.cz'+next_url,7,nexticon)
    except:
        print 'STRANKOVANI NENALEZENO!'


                
def VIDEOLINK(url,name):
    req = urllib2.Request(url)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    httpdata = response.read()
    response.close()
    match = re.compile('callSOAP\((.+?)\)').findall(httpdata)
    info = re.compile('<meta name="description" content="(.+?)"').findall(httpdata)
    if len(info)<1:
            info = re.compile('<title>(.+?)&mdash').findall(httpdata)
    #RE_PLAYLIST_URL = re.compile('callSOAP\((.+?)\)')
    # Converting text to dictionary
    query = json.loads(match[0])
    # Converting dictionary to text arrays    options[UserIP]=xxxx&options[playlistItems][0][..]....
    strquery = http_build_query(query)
    # Ask a link page XML
    request = urllib2.Request('http://www.ceskatelevize.cz/ajax/playlistURL.php', strquery)
    con = urllib2.urlopen(request)
    # Read lisk XML page
    data = con.read()
    con.close()
    doc = read_page(data)
    items = doc.find('body')
    for item in items.findAll('switchitem'):
        match = re.compile('<switchitem id="(.+?)" base="(.+?)" begin=".+?" duration=".+?" clipbegin=".+?">').findall(str(item))
        for id,base in match:
            base = re.sub('&amp;','&',base)
            if re.search('AD', id, re.U): 
                continue
            video = re.compile('<video src="(.+?)" system-bitrate=".+?" label="(.+?)" enabled=".+?">').findall(str(item))
            for cesta,kvalita in video:
                #rtmp_url = base+' playpath='+cesta+' pageUrl='+url+' swfUrl='+swfurl+' swfVfy=true live=true'
                rtmp_url = base+'/'+cesta
                addLink(kvalita+' '+name,rtmp_url,icon,info[0])
                #print rtmp_url,kvalita+info[0] #vystupni parametry RTMP


def http_build_query(params, topkey = ''):
    from urllib import quote_plus
    
    if len(params) == 0:
       return ""
 
    result = ""

    # is a dictionary?
    if type (params) is dict:
       for key in params.keys():
           newkey = quote_plus (key)
           
           if topkey != '':
              newkey = topkey + quote_plus('[' + key + ']')
           
           if type(params[key]) is dict:
              result += http_build_query (params[key], newkey)

           elif type(params[key]) is list:
                i = 0
                for val in params[key]:
                    if type(val) is dict:
                       result += http_build_query (val, newkey + '[' + str(i) + ']')

                    else:
                       result += newkey + quote_plus('[' + str(i) + ']') + "=" + quote_plus(str(val)) + "&"

                    i = i + 1              

           # boolean should have special treatment as well
           elif type(params[key]) is bool:
                result += newkey + "=" + quote_plus(str(int(params[key]))) + "&"

           # assume string (integers and floats work well)
           else:
                try:
                  result += newkey + "=" + quote_plus(str(params[key])) + "&"       # OPRAVIT ... POKUD JDOU U params[key] ZNAKY > 128, JE ERROR, ALE FUNGUJE TO I TAK
                except:
                  result += newkey + "=" + quote_plus("") + "&"  

    # remove the last '&'
    if (result) and (topkey == '') and (result[-1] == '&'):
       result = result[:-1]       
  
    return result


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param



def addLink(name,url,iconimage,popis):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": popis} )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    
params=get_params()
url=None
name=None
thumb=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        OBSAH()
       
elif mode==1:
        print ""
        KATEGORIE()

elif mode==2:
        print ""+url
        ABC(url)

elif mode==3:
        print ""+url
        CAT_LIST(url)

elif mode==4:
        print ""+url
        LIVE_OBSAH(url)

elif mode==5:
        print ""+url
        DATUM(url)

elif mode==6:
        print ""+url
        VIDEO_LIST(url)

elif mode==7:
        print ""+url
        BONUSY(url)



elif mode==10:
        print ""+url
        VIDEOLINK(url,name)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
