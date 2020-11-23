class HeaderC{
    constructor(){
        this.menudic = {}
        this.subdic= {}
        this.subs = [];
        this.subsubs=[];
        this.menudic["about"]={"HipHop":"about-hiphop.html","R&B":"about-R&B.html"};
        this.menudic["label"]={"저스트뮤직":"justmusic.html","THEBLACKLABEL":"theblack.html","AOMG":"AOMG.html","아메바컬쳐":"amoeba.html","브랜뉴뮤직":"bnm.html","일리네어레코즈":"inr.html","하이라이트레코즈":"hlr.html","UNIVERSIAL":"Universal.html"};
        this.menudic["recom"]={
            "HipHop":{"프라이머리":"recom(Hiphop1).html","2 4 : 2 6":"recom(Hiphop2).html","EAT":"recom(Hiphop3).html","TELEVISION":"recom(Hiphop4).html","EVERYWHERE":"recom(Hiphop5).html","Library Of Soul":"recom(Hiphop6).html"},
            "R&B":{"Afterwork":"recom(R&B1).html","Principle Of My Soul":"recom(R&B2).html","EVERYTHING YOU WANTED":"recom(R&B3).html","FRAMEWORKS":"recom(R&B4).html","Crush on You":"recom(R&B5).html","Realcollabo":"recom(R&B6).html","130 mood : TRBL":"recom(R&B7).html"}
        }
        this.menudic["newal"]={"ELO-GRADATION VOL.3":"newal1.html","SAAY-CLASSIC":"newal2.html","Ja Mezz-GOØDevil":"newal3.html","제이켠-RE;MIND":"newal4.html"}
        this.menudic["reart"]={
            "HipHop":{"TigerJK":"reart(Hiphop)-TigerJK.html","Dok2":"reart(Hiphop)-Dok2.html"},
            "R&B":{"Ra.d":"reart(R&B)-Rad.html","Dean":"reart(R&B)-Dean.html"},
            "Producer":{"GroovyRoom":"reart(Producer)-GroovyRoom.html","Gray":"reart(Producer)-Gray.html"}
        }
        this.menudic["link"]={}


        this.header = document.createElement("header");
        
        var a = document.createElement("a");
        a.setAttribute("href","index.html");
        var h1 = document.createElement("h1");
        var h1text = document.createTextNode("KOREA TRENDY HIPHOP & RNB");
        h1.appendChild(h1text);
        a.appendChild(h1);
        this.header.appendChild(a);

        var h4 = document.createElement("h3");
        var h4text = document.createTextNode(document.getElementsByTagName('title')[0].childNodes[0].nodeValue);
        h4.appendChild(h4text);
        this.header.appendChild(h4);

        this.header.appendChild(document.createElement("br"));
        this.header.appendChild(document.createElement("hr"));

        var nav = document.createElement("nav");

        nav.appendChild(this.menuconstructor("about","About"));
        nav.appendChild(this.menuconstructor("label","대표레이블"));
        nav.appendChild(this.menuconstructor("recom","추천앨범"));
        nav.appendChild(this.menuconstructor("newal","새로운앨범"));
        nav.appendChild(this.menuconstructor("reart","추천아티스트"));
        nav.appendChild(this.menuconstructor("link","노래들으러가기(멜론)","https://www.melon.com/"));

        this.nav = nav;

        this.header.appendChild(nav);
        this.header.appendChild(document.createElement("hr"));
        document.body.appendChild(this.header);
    }

    menuconstructor(id,text,link=null) {
        var div = document.createElement("div");
        div.setAttribute("class","menu");
        div.setAttribute("id",id);
        div.setAttribute("onmouseleave","HeaderI.clear(this)");
        if(link!=null) {
            var span = document.createElement("a");
            span.setAttribute("href",link);    
            span.setAttribute("target","_blank");
        }
        else var span = document.createElement("span");
        span.setAttribute("onclick","HeaderI.submenugen(this)");
        var spantext = document.createTextNode(text);
        span.appendChild(spantext);
        div.appendChild(span);
        return div;
    }

    clear(self){
        this.subs.forEach(sub=>{

            sub.parentNode.removeChild(sub);
        });
        this.subs = [];
    }

    submenugen(self){
        var sel = self.parentNode;
        this.clear(sel);
        for(var key in this.menudic[sel.getAttribute("id")]){
            var mitem = document.createElement("mitem");
            mitem.style.display="block";
            mitem.setAttribute("onclick","HeaderI.subsubmenugen(this)");
            var text = document.createTextNode(key);
            if(typeof(this.menudic[sel.getAttribute("id")][key])==typeof("")){
                var a = document.createElement("a");
                a.setAttribute("href",this.menudic[sel.getAttribute("id")][key]);
                a.appendChild(text);
                mitem.appendChild(a);
            }
            else{
                mitem.setAttribute("id",key);
                mitem.appendChild(text);
            }
            this.subs.push(mitem);
            sel.appendChild(mitem);
        }
    }

    subsubmenugen(self){
        var parent = self.parentNode;
        if(typeof(this.menudic[parent.getAttribute("id")])!=typeof("")){
            if(this.subsubs.length!=0){
                this.subsubs.forEach(sub=>{
                    sub.parentNode.removeChild(sub);
                });
                this.subsubs=[];
            }
            var index = 0;
            for(var key in this.menudic[parent.getAttribute("id")][self.getAttribute("id")]){
                var mitem = document.createElement("mitem");
                mitem.setAttribute("class","sub");
                mitem.style.display="inline-block";
                mitem.style.position="relative";
                var a = document.createElement("a");
                a.setAttribute("href",this.menudic[parent.getAttribute("id")][self.getAttribute("id")][key]);
                var text = document.createTextNode(key);
                a.appendChild(text);
                mitem.appendChild(a);
                self.appendChild(mitem);
                var rect = self.parentNode.getClientRects();
                var mrect=mitem.getClientRects();
                var brect=document.body.getClientRects();
                mitem.style.position="absolute";
                //mitem.style.left+=1+"em";
                mitem.style.top=(mrect[0].top-5+(23*index))+"px";
                index++;
                this.subsubs.push(mitem);
            }
        }
    }
}
HeaderI = new HeaderC();
document.write("<div class=\"mainsec\">")