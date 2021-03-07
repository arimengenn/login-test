import sys,time
def run(teks):
    putih = "\033[0m"
    merah = "\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write('\r%s%s%s%s' % (putih,char.lower(),merah,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.1)
            num += 1
    except: exit()

run("xxxxxx")

4). Teks Animasi Loading
import sys,time
def ub():
        try:
                a = 20
                b = 0
                for c in range(a):
                        a -= 1
                        b += 1
                        sys.stdout.write("\r Loading [%s%s] %s/%s"%("#"*b,"-"*a,b,a)),;sys.stdout.flush()
                        time.sleep(0.1)
        except KeyboardInterrupt:
                sys.exit()
