# cf) https://qiita.com/kkoba84/items/b828229c374a249965a9

import subprocess

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)
