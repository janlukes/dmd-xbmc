# -*- coding: utf-8 -*-
import urllib2,urllib,re,os
from parseutils import *
import xbmcplugin,xbmcgui,xbmcaddon
__dmdbase__ = 'http://iamm.netuje.cz/emulator/joj/image/'
_UserAgent_ = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon = xbmcaddon.Addon('plugin.video.dmd-czech.joj')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id='plugin.video.dmd-czech.joj')
home = __settings__.getAddonInfo('path')
REV = os.path.join( profile, 'list_revision')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
nexticon = xbmc.translatePath( os.path.join( home, 'nextpage.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )

def OBSAH():
    addDir('Publicistika','http://www.joj.sk',1,icon)
    addDir('Seriály','http://www.joj.sk',2,icon)
    addDir('Zábava','http://www.joj.sk',3,icon)    
def OBSAH_PUB():
    addDir('Črepiny *','http://crepiny.joj.sk/crepiny-s-hviezdickou-archiv.html',4,__dmdbase__+'crepiny-s-hviezdickou.jpg')
    addDir('Exclusiv','http://www.joj.sk/exclusiv/exclusiv-archiv.html',4,__dmdbase__+'exclusiv.jpg')
    addDir('Krimi noviny','http://krimi.joj.sk/krimi-noviny-archiv.html',4,__dmdbase__+'krimi-noviny.jpg')
    addDir('Najlepšie počasie','http://www.joj.sk/najlepsie-pocasie/najlepsie-pocasie-archiv.html',4,__dmdbase__+'najlepsie-pocasie.jpg')
    addDir('Noviny','http://www.joj.sk/relacia-noviny/noviny-archiv.html',4,__dmdbase__+'noviny_01.jpg.jpg')
    addDir('Noviny o 12:00','http://www.joj.sk/noviny-o-12-00/noviny-o-12-00-archiv.html',4,__dmdbase__+'noviny-o-12-00.jpg.jpg')
    addDir('Noviny o 17:00','http://www.joj.sk/noviny-o-17-00/noviny-o-17-00-archiv.html',4,'http://c.static.joj.sk/uploads/tx_media/thumbs/310x175/noviny-o-17-00_79970.jpg')
    addDir('Promi noviny','http://www.joj.sk/promi-noviny/promi-noviny-archiv.html',4,__dmdbase__+'promi-noviny.jpg')
    addDir('Prvé noviny','http://www.joj.sk/prve-noviny/prve-noviny-archiv.html',4,__dmdbase__+'prve-noviny.jpg')
    addDir('Šport','http://www.joj.sk/relacia-sport/sport-archiv.html',4,__dmdbase__+'sport.jpg')
def OBSAH_SER():
    addDir('Aféry','http://afery.joj.sk/afery-epizody.html',4,__dmdbase__+'afery.jpg')
    addDir('Ako som prežil','http://www.joj.sk/ako-som-prezil/ako-som-prezil-epizody.html',4,'http://media.televize.cz/film/n1p7zky90ogv.jpg')
    addDir('Dr.Ludský','http://www.joj.sk/dr-ludsky/dr-ludsky-epizody.html',4,__dmdbase__+'dr-ludsky.jpg')
    addDir('Hoď svišťom','http://hodsvistom.joj.sk/hod-svistom-epizody.html',4,'http://img.csfd.cz/posters/30/300577_1.jpg')
    addDir('Keby bolo keby','http://www.joj.sk/keby-bolo-keby/keby-bolo-keby-epizody.html',4,__dmdbase__+'kbk.jpg')
    addDir('Mafstory','http://mafstory.joj.sk/mafstory-epizody.html',4,__dmdbase__+'mafstory.jpg')
    addDir('Panelák','http://panelak.joj.sk/panelak-epizody.html',4,__dmdbase__+'panelak.jpg')
    addDir('Profesionáli','http://profesionali.joj.sk/profesionali-epizody.html',4,__dmdbase__+'profesionali.jpg')
    addDir('Prvé oddelenie','http://www.joj.sk/prve-oddelenie/prve-oddelenie-epizody.html',4,__dmdbase__+'prve-oddelenie.jpg')

def OBSAH_ZAB():
    addDir('Ano, šéfe!','http://anosefe.joj.sk/anosefe-epizody.html',4,__dmdbase__+'anosefe.jpg')
    addDir('Bordelári','http://www.bordelari.sk/bordelari-archiv.html',4,'http://a.static.joj.sk/uploads/tx_media/thumbs/306x172/bordelari_79969.jpg')
    addDir('ČS má Talent','http://www.csmatalent.cz/video-cz.html',6,__dmdbase__+'talent.jpg')
    addDir('Hladá sa milionár','http://www.joj.sk/hlada-sa-milionar/hlada-sa-milionar-archiv.html',4,__dmdbase__+'hlada-sa-milionar.jpg')
    addDir('Chutíš mi','http://www.chutismi.sk/chutis-mi-archiv.html',4,__dmdbase__+'chutismi.jpg')
    addDir('Farmár hľadá ženu 2','http://www.farmarhladazenu.sk/epizody.html',8,'http://t2.gstatic.com/images?q=tbn:ANd9GcRRJbqnrXcT-Ius3Qo29sc-KPVKuNkVjRq5zx51P3FSdpzLL0VD')
    addDir('Kapor na torte','http://www.joj.sk/kapor-na-torte-den-prvy/kapor-na-torte-den-prvy-archiv.html',4,__dmdbase__+'kapor-na-torte.jpg')
    addDir('Kutyil s.r.o','http://www.joj.sk/kutyil/kutyil-epizody.html',4,__dmdbase__+'kutyil-logo.jpg')
    addDir('Lampa','http://plus.joj.sk/lampa/lampa-tv-archiv.html',4,__dmdbase__+'lampa.jpg')
    addDir('Mama ožeň ma','http://www.mamaozenma.sk/mama-ozen-ma-epizody.html',7,'http://reality-show.panacek.com/wp-content/2015-mama_ozen_ma2.jpg')
    addDir('Nebožies','http://plus.joj.sk/neboziec/epizody.html',4,'http://a.static.joj.sk/uploads/tx_media/thumbs/310x175/logo_77360.jpg')
    addDir('Nové bývanie','http://novebyvanie.joj.sk/nove-byvanie-archiv.html',4,__dmdbase__+'nove-byvanie.jpg')
    addDir('Sedem','http://www.joj.sk/sedem/sedem-archiv.html',4,__dmdbase__+'sedem.jpg')
    addDir('Odsůdené','http://www.joj.sk/odsudene/odsudene-epizody.html',4,__dmdbase__+'odsudene.jpg')
    addDir('Sůdna sieň','http://www.joj.sk/sudna-sien/sudna-sien-archiv.html',4,__dmdbase__+'sudna-sien.jpg')
    addDir('Šéfka','http://www.sefka.sk/epizody.html',5,__dmdbase__+'sefka-logo.jpg')
    addDir('Tajný sen','http://www.joj.sk/tajny-sen/tajny-sen-archiv.html',4,__dmdbase__+'tajny-sen.jpg')


    
def LIST(url):
    #self.core.setSorting('NONE')
    req = urllib2.Request(url)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    httpdata = response.read()
    response.close()
    match = re.compile('<td><strong><a href="(.+?)">(.+?)</a>').findall(httpdata)
    for link,name in match:
        addDir(name,link,10,icon)
    try:
        doc = read_page(url)
        items = doc.find('ul', 'x-pager')
        print items
        for item in items.findAll('a'):
            page = item.text.encode('utf-8') 
            if re.match('Nasledujúca', page, re.U):
                next_url = item['href']
                addDir('Další strana',next_url,4,nexticon)
    except:
        print 'strankovani nenalezeno'

def LIST_2(url):
    #self.core.setSorting('NONE')
    doc = read_page(url)
    items = doc.find('div', 'b-body c')
    for item in items.findAll('li'):
        try:
            name = item.a['title'].encode('utf-8')
        except:
            name = 'Bezejmenný titul'
        url = str(item.a['href']) 
        thumb = str(item.img['src'])   
        addDir(name,'http://www.sefka.sk/'+url,10,thumb)

def LIST_3(url):
    doc = read_page(url)
    items = doc.find('ul', 'l c')
    for item in items.findAll('li'):
        try:
            name = item.a['title'].encode('utf-8')
        except:
            name = 'Bezejmenný titul'
        url = str(item.a['href']) 
        thumb = str(item.img['src'])   
        addDir(name,'http://www.csmatalent.cz/'+url,11,thumb)
    try:
        items = doc.find('ul', 'b-box b-pager-x c')
        dalsi = items.find('li', 'next')
        if len(dalsi) != 0:
            next_url = str(dalsi.a['href']) 
            addDir('>> Další strana >>','http://www.csmatalent.cz/'+next_url,6,nexticon)
    except:
        print 'strankovani nenalezeno'

def LIST_4(url):
    doc = read_page(url)
    items = doc.find('ul', 'l c')
    for item in items.findAll('li'):
        try:
            name = item.a['title'].encode('utf-8')
        except:
            name = 'Bezejmenný titul'
        url = str(item.a['href']) 
        thumb = str(item.img['src'])   
        addDir(name,'http://www.mamaozenma.sk/'+url,10,thumb)
    try:
        items = doc.find('ul', 'b-box b-pager-x c')
        dalsi = items.find('li', 'next')
        if len(dalsi) != 0:
            next_url = str(dalsi.a['href']) 
            addDir('>> Další strana >>','http://www.mamaozenma.sk/'+next_url,7,nexticon)
    except:
        print 'strankovani nenalezeno'

def LIST_5(url):
    doc = read_page(url)
    items = doc.find('ul', 'l c')
    for item in items.findAll('li','i'):
        try:
            name = item.a['title'].encode('utf-8')
        except:
            name = 'Bezejmenný titul'
        url = str(item.a['href']) 
        thumb = str(item.img['src'])   
        addDir(name,'http://www.farmarhladazenu.sk/'+url,10,'http://www.farmarhladazenu.sk/'+thumb)
    try:
        items = doc.find('ul', 'b-box b-pager-x c')
        dalsi = items.find('li', 'next')
        if len(dalsi) != 0:
            next_url = str(dalsi.a['href']) 
            addDir('>> Další strana >>','http://www.farmarhladazenu.sk/'+next_url,8,nexticon)
    except:
        print 'strankovani nenalezeno'
                
def VIDEOLINK(url,name):
    req = urllib2.Request(url)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    httpdata = response.read()
    response.close()
    try:
        basepath = re.compile('basePath: "(.+?)"').findall(httpdata)
        videoid = re.compile('videoId: "(.+?)"').findall(httpdata)
        pageid = re.compile('pageId: "(.+?)"').findall(httpdata)
        if len (pageid[0]) != 0:
          playlisturl = basepath[0]+'services/Video.php?clip='+videoid[0]+'pageId='+pageid[0]
        else:
          playlisturl = basepath[0]+'services/Video.php?clip='+videoid[0]
        print playlisturl
        req = urllib2.Request(playlisturl)
        req.add_header('User-Agent', _UserAgent_)
        response = urllib2.urlopen(req)
        doc = response.read()
        response.close()
        title = re.compile('title="(.+?)"').findall(doc)
        thumb = re.compile('large_image="(.+?)"').findall(doc)
        joj_file = re.compile('<file type=".+?" quality="(.+?)" id="(.+?)" label=".+?" path="(.+?)"/>').findall(doc)
        for kvalita,serverno,cesta in joj_file:
            name = str.swapcase(kvalita)+ ' - ' + title[0]
            server = 'n0'+serverno+'.joj.sk'
            tcurl = 'rtmp://'+server
            swfurl = 'http://www.joj.sk/fileadmin/templates/swf/JojPlayer.swf?no_cache=176146'
            port = '1935'
            rtmp_url = tcurl+' playpath='+cesta+' pageUrl='+url+' swfUrl='+swfurl+' swfVfy=true'
            addLink(name,rtmp_url,thumb[0],name)
    except:
        basepath = re.compile('basePath=(.+?)&amp').findall(httpdata)
        basepath = re.sub('%3A',':',basepath[0])
        basepath = re.sub('%2F','/',basepath)
        print basepath
        videoid = re.compile('videoId=(.+?)&amp').findall(httpdata)
        playlisturl = basepath+'services/Video.php?clip='+videoid[0]
        req = urllib2.Request(playlisturl)
        req.add_header('User-Agent', _UserAgent_)
        response = urllib2.urlopen(req)
        doc = response.read()
        response.close()
        title = re.compile('title="(.+?)"').findall(doc)
        joj_file = re.compile('<file type=".+?" quality="(.+?)" id="(.+?)" label=".+?" path="(.+?)"/>').findall(doc)
        for kvalita,serverno,cesta in joj_file:
            name = str.swapcase(kvalita)+ ' - ' + title[0]
            server = 'n0'+serverno+'.joj.sk'
            tcurl = 'rtmp://'+server
            swfurl = basepath+'fileadmin/templates/swf/csmt_player.swf?no_cache=171307'
            port = '1935'
            rtmp_url = tcurl+' playpath='+cesta+' pageUrl='+url+' swfUrl='+swfurl+' swfVfy=true'
            addLink(name,rtmp_url,icon,name)
def TALENT(url,name):
    req = urllib2.Request(url)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    httpdata = response.read()
    response.close()
    basepath = re.compile('basePath: "(.+?)"').findall(httpdata)
    videoid = re.compile('videoId: "(.+?)"').findall(httpdata)
    playlisturl = basepath[0]+'services/Video.php?clip='+videoid[0]
    req = urllib2.Request(playlisturl)
    req.add_header('User-Agent', _UserAgent_)
    response = urllib2.urlopen(req)
    doc = response.read()
    response.close()
    thumb = re.compile('thumb="(.+?)"').findall(doc)
    joj_file = re.compile('<file type=".+?" quality="(.+?)" id="(.+?)" label=".+?" path="(.+?)"/>').findall(doc)
    for kvalita,serverno,cesta in joj_file:
        titul = str.swapcase(kvalita)+ ' - ' + name
        server = 'n0'+serverno+'.joj.sk'
        tcurl = 'rtmp://'+server
        swfurl = 'http://b.static.csmatalent.sk/fileadmin/templates/swf/CsmtPlayer.swf?no_cache=168842'
        port = '1935'
        rtmp_url = tcurl+' playpath='+cesta+' pageUrl='+url+' swfUrl='+swfurl+' swfVfy=true'
        addLink(titul,rtmp_url,thumb[0],titul)



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
        OBSAH_PUB()

elif mode==2:
        print ""
        OBSAH_SER()

elif mode==3:
        print ""
        OBSAH_ZAB()

elif mode==4:
        print ""+url
        LIST(url)

elif mode==5:
        print ""+url
        LIST_2(url)

elif mode==6:
        print ""+url
        LIST_3(url)        

elif mode==7:
        print ""+url
        LIST_4(url) 

elif mode==8:
        print ""+url
        LIST_5(url)
        
elif mode==10:
        print ""+url
        VIDEOLINK(url,name)
elif mode==11:
        print ""+url
        TALENT(url,name)
xbmcplugin.endOfDirectory(int(sys.argv[1]))