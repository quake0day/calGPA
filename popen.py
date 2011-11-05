import popen2,sys
from time import *

def _popen(cmd, timeout = 10, num_retry = 2, logfile = sys.stdout):
    i = 0
    is_timeout = False
    while i <= num_retry:
        print "%dth try"%i, cmd
        sys.stdout.flush()
        i += 1
        t0 = time()
        P = popen2.Popen3(cmd, True)
        prompt = False
        while time() < t0 + timeout and P.poll() == -1:
            sleep(0.1)
        sts = P.poll()
        if sts == -1:
            logfile.write(color_str("command [%s] timeout\n"%(cmd), fg_red))
            if i < num_retry:
                logfile.write(color_str("terminate and try again\n", fg_red))
            logfile.flush()
            is_timeout = True
            os.kill(P.pid, signal.SIGTERM)
        elif sts != 0:
            for l in P.childerr.readlines():
                logfile.write(l)
            if i < num_retry:
                logfile.write("try again\n")
            logfile.flush()
            is_timeout = False
        else:
            is_timeout = False
            break
    logfile.write("return "+str(sts)+"\n")
    sys.stdout.flush()
    if is_timeout:
        return (sts, open("/dev/null", "r"))
    else:
        return (sts, P.fromchild)
