from popen import _popen

a = _popen('ps aux')
print a[1].read()
