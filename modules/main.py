a

?�g?6?@sddlZddlZddlZddlZddlZddlZddlZddl
Z
ddlZ	ddl
m
Z
ddl
m
Z
m
Z
mZmZmZddlmZddlmZddl
mZdd
lmZddlmZmZdd	lmZdd
lmZdd
lm Z dd
l!m"Z"dd
lm#Z#m$Z$dd
l%m&Z&ede
e
ed?Z'e?(?Z)e)j*ddd?dd??Z+dd?Z,e'?-e?.dg??eed?dd??Z/e'?-e?.d??dd??Z0e'?-e?.dg??eed?d d??Z/d!d"?Z1e2d#k?re3d$?d%d&?Z4d'd(?Z5e?6?Z7zFz$e7?8e4??e7?8e5??e7?9?Wne:?y?Yn0We7?;?n
e7?;?0dS))?N)?
progress_bar)?API_ID?API_HASH?	BOT_TOKEN?
WEBHOOK?PORT)?
ClientSession)?listen)?getstatusoutput)?web)?Client?
filters)?
Message)?	FloodWait)?StickerEmojiInvalid)?
message)?InlineKeyboardButton?InlineKeyboardMarkup)?king?bot)Zapi_idZapi_hashZ	bot_token?/T)Z
allow_headc?s
t?d?S)Nz$https://github.com/textleech001/text-leech-bot)r
Z
json_response)Z
request?r?m2.py?root_route_handler!src?stjdd?}|?t?|S)Ni���)Zclient_max_size)r
Z
ApplicationZ
add_routes?routes)Z
web_apprrr?
web_server&s

r?start?r?mc?s6|jtjttddd?gtddd?gg?d?IdHdS)
Nu5�? King Project�?  ✜zhttps://t.me/KingProject24)?urlu+🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋zhttps://t.me/KingProjectSupport)Z
reply_markup)?
reply_textrZ
START_TEXTrrrrrr?
account_login,s��
?��r!?stopc?s0|?dd?IdHtjtjtjgtj?R?dS)Nu$�? 𝐒𝐭𝐨𝐩𝐩𝐞𝐭 ♦T)r ?os?execl?sys?
executable?argv)?_rrrr?restart_handler=sr)Zuploadc1?s?	|?d?IdH}|?|jj?IdH}|??IdH}|?d?IdHd|jj??}zjt|d??}|?
?}
Wd?n1sz0Y|
?d?}
g}|
D]}	|?	|	?dd
??q�t
?
|?Wn(|?d?IdHt
?
|?YdS0|?
d	t
|??d
??IdH|?|jj?IdH}
|
j
}
|
?d?IdH|?
d
?IdH|?|jj?IdH}
|
j
}
|
?d?IdH|?
tj?IdH|?|jj?IdH}
|
j
}|
?d?IdHzh|d
k?r�d
}nT|d
k?r�d}nD|dk?r�d}n4|dk?r�d}n$|dk?r�d}n|dk?rd}nd}Wnt?y d}Yn0|?
tj?IdH|?|jj?IdH}|j
}|?d?IdHd}|dk?rr|}n|}|?
tj?IdH|?|jj?IdH}}|j
}|?d?IdH|??IdH|j
}|?d??s�|?d??r�td|?d??d}n|d kt
|?d
k?rd
}nt|
?}?zRt|d
t
|??D?]8}	||	d
?d!d"??d#d$??d%d&??d'd&?}d|}d(|v?r:t?4IdH��}|j|d)d*d+d,d+d-d.d/d0d1d2d3d4d5d6?
d7?4IdH?8}|?
?IdH}t?d8|??d
?}Wd?IdH?q
1IdH?s0YWd?IdH?q1IdH?s.0Yn�d9|v?rftjd:|??d;d<id7???d=}n�d>|v?s�d?|v?s�d9|v?s�d@|v?r�dAd<dBdCdDdEdFdGdH?}d=|?ff} tjdI|| dJ?}!|!??d=}nJdK|v?r�|?dL?dM}"dN|"dO}n$dP|v?r|?dL?dM}"dQ|"dR}||	dS?dTd&??dUd&??dLd&??dVd&??dWd&??dXd&??dYd&??dZd&??d[d&??d\d&??d]d&?? ?}#t!|??"d^??d_|#dd`???}$da|v?r�db|?dc|?dd?}%ndb|?de|?df?}%dg|v?r�dh|$?di|?dj|?dk?
}&n�da|v?rdl|?dm|?dn|$?dk?
}&n�do|v?r<dp|%?dq|?dn|$?dk?
}&n�dr?sLds|v?rfdp|%?dt|?dn|$?dk?
}&n\|%duk?szdv|v?r�dp|%?dt|?dn|$?dk?
}&n.dw?s�dx|v?r�dy}&ndp|%?dz|?dn|$?dk?
}&?zJd{t!|??"d^??d||#?d}|
?d~|?d{?	}'d{t!|??"d^??d||#?d|
?d~|?d{?	}(d�|v?
r�zLt#?||$?IdH})|j$|jj|)|(d��IdH}*|d
7}t
?
|)?t%?&d
?WnVt'?
y?}+z<|?t!|+??IdHt%?&|+j(?WYd}+~+W?q2WYd}+~+n
d}+~+00?nDdw|v?r�zbdh|$?d�|?dk?}&|&?d��},t
?)|,?|j$|jj|$?dw?|(d��IdH}*|d
7}t
?
|$?dw??WnVt'?y?}+z<|?t!|+??IdHt%?&|+j(?WYd}+~+W?q2WYd}+~+n
d}+~+00n~d�|$?d�|?d�|?d��
}-|?|-?IdH}.t#?*||&|$?IdH}/|/}0|.?d?IdHt#?+|||'|0||$|.?
IdH|d
7}t%?&d
?WnZt?	yh}+z@|?d�t!|+??d�|$?d�|???IdHWYd}+~+?q2WYd}+~+n
d}+~+00?q2Wn6t?	y?}+z|?|+?IdHWYd}+~+n
d}+~+00|?d��IdHdS)�Nu(sᴇɴᴅ ᴍᴇ .ᴛx�? ғɪʟ�?  ⏍Tz
./downloads/?r?
z://?uG�? 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.u8ɪɴ ᴛx�? ғɪʟ�? ᴛɪᴛʟ�? ʟɪɴ�? 🔗** **uo**

sᴇɴᴅ ғʀᴏᴍ  ᴡʜᴇʀ�? ʏᴏᴜ ᴡᴀɴ�? ᴛᴏ ᴅᴏᴡɴʟᴏᴀ�? ɪɴɪᴛᴀʟ ɪs 1uz�? 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞Z144Z
256x144Z240Z
426x240Z360Z
640x360Z480Z
854x480Z720Z1280x720Z1080Z	1920x1080ZUNu�? ⁪⁬⁮⁮⁮ZRobinz
http://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpgZnoz
file/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1?z/view?usp=sharingZ	visioniasz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9z
en-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/ZiframeZnavigatez
cross-site?1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")
ZAcceptzAccept-Languagez
Cache-ControlZ
ConnectionZPragmaZ
Refererz
Sec-Fetch-Destz
Sec-Fetch-Modez
Sec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)?
headersz(https://.*?playlist.m3u8.*?)\"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=?
x-access-tokenZ\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9rztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comz
Mobile-Androidz1.4.37.1Z18Z5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30Zgzip)ZHostr0z
user-agentz
app-versionz
api-versionz	device-idz
device-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)r/?paramsz/utkarshapp.mpdr�����z$https://apps-s3-prod.utkarshapp.com/z/utkarshapp.comz
/master.mpdz&https://d26g5bnklkwsh4.cloudfront.net/z
/master.m3u8r?	?:?+?#?|?@?*?.ZhttpsZhttp?z) ?<Zyoutuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z
]/bv[height<=z
]+ba/b/bv+baZacecwplyz
yt-dlp -o "z" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "?"z yt-dlp -i -f "bestvideo[height<=z=]+bestaudio" --no-keep-video --remux-video mkv --no-warning "z" -o "z
player.vimeoz
yt-dlp -f "z/+bestaudio" --no-keep-video --remux-video mkv "Zm3u8Z
livestreamz%" --no-keep-video --remux-video mkv "?0?
unknownz.pdf?downloadZpdfzC+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "z**z. u.mkv

Batch Name  » u

Downloaded By » u.pdf

Batch Name  » Zdrive)Z
chat_idZdocumentZ
captionz
.pdf" "z -R 25 --fragment-retries 25uZ**❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »

📝 𝐍𝐚𝐦𝐞 » u!
�? 𝐐𝐮𝐥𝐢𝐭𝐲 » u

🔗 𝐔𝐑𝐋 »** `?`uZ�? 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝
u
�? 𝐍𝐚𝐦𝐞 » u
�? 𝐋𝐢𝐧𝐤 » uE�? 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞),r r	Zchat?idr@?delete?open?read?split?appendr#?removeZedit?len?textrZ
Q1_TEXT?	ExceptionZ
C1_TEXTZ
T1_TEXT?
startswithr
?int?range?
replacer?get?re?search?group?requests?json?strip?str?zfill?helperZ
send_document?time?sleepr?x?systemZ
download_videoZsend_vid)1rrZeditable?inputr\?path?fZ
contentZlinks?iZinput0Zraw_textZinput1Z	raw_text0Zinput2Z	raw_text2?resZinput3Z	raw_text3Z
highlighterZMRZinput6rZ	raw_text6Zthumb?count?VrZ
sessionZresprJr/r1ZresponserBZname1?nameZytf?cmdZccZcc1Zka?copy?eZ
download_cmdZShow?progZres_file?filenamerrrr!Cs?


&



�












�???�

??


�b
�??�???
?

?







�?????
??	?
?
?� 



((

�



*


�

(
�
,&c?sVtrRt?IdH}t?|?}|??IdHt?|dt?}|?
?IdHtdt???dS)Nz
0.0.0.0zWeb server started on port )	rrr
Z	AppRunnerZsetupZ
TCPSiter
r?print)ZappZrunnerZsiterrr?main@s





rl?__main__u?
   KING�? �?  PROJECT c?st??IdHdS?N)rrrrrr?	start_botSsroc?st?IdHdSrn)rlrrrr?	start_webVsrp)<r#rQr%rUrZZ
asynciorT?
subprocessZcorerYZutilsr?varsrrrrr
Z
aiohttprZ
pyromodr	r
r
Zpyrogramr
r
Z
pyrogram.typesr
Zpyrogram.errorsrZ*pyrogram.errors.exceptions.bad_request_400rZ!pyrogram.types.messages_and_mediarrrZstylerrZ
RouteTableDefrrPrrZ
on_messageZ
commandr!r)rl?__name__rkrorpZ
get_event_loopZloopZ
create_taskZ
run_forever?KeyboardInterruptr"rrrr?<module>s`













}

�






