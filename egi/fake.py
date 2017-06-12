#!/usr/bin/python
# -*- coding: cp1251 -*- 
import simple as internal
import sys

Error = internal.Eggog
ms_localtime = internal.ms_localtime


def Print(*args, **kwargs):
    write = sys.stdout.write
    write(" Netstation [fake]: ")
    for arg in args: write(repr(arg))
    for (k, v) in kwargs.iteritems(): write("%s=%s" % (k, v))
    write('\n')


def make_fit(k):
    n = len(k)
    d = n - 4
    if d > 0:
        return k[0:4]
    else:
        return (k + ' ' * abs(d))


class Netstation:
    def __init__(self):
        Print('__init__()')
        self.objectExists = True

    def checkExists(self):
        if self.objectExists:
            pass
        else:
            raise RuntimeError(
                'There is no (fake) connection to Netstation, make sure you Initialized or Re-Initialized one.')

    def enumerate_responses(self):
        self.checkExists()
        n_available = 0
        for i in xrange(n_available):
            data = self._get()
            yield data

    def process_responces(self):
        self.checkExists()
        for resp in self.enumerate_responses():
            pass
        Print('process_responces()')

    def initialize(self, str_address, port_no):
        self.checkExists()
        Print('initialize( %s, %s )' % (str_address, port_no))

    def finalize(self, seconds_timeout=2):
        self.checkExists()
        Print('finalize( timeout: %s seconds )' % (seconds_timeout,))
        print " egi: stopping ... "
        self.objectExists = 0
        self = None

    def BeginSession(self):
        self.checkExists()
        Print('BeginSession()')

    def EndSession(self):
        self.checkExists()
        Print('EndSession()')

    def StartRecording(self):
        self.checkExists()
        Print('StartRecording()')

    def StopRecording(self):
        self.checkExists()
        Print('StopRecording()')

    def _SendAttentionCommand(self):
        pass

    def _SendLocalTime(self, ms_time=None):
        pass

    def sync(self, timestamp=None):
        self.checkExists()
        Print('sync( %s = %s)' % ('timestamp', timestamp))

    def send_event(self, key, timestamp=None, label=None, description=None, table=None, pad=False):
        self.checkExists()
        if pad == True:
            key = make_fit(str(key))
            if table:
                newTable = {}
                for i in table:
                    table[make_fit(str(i))] = table.pop(i)
        kwargs = {
            'key': key,
            'timestamp': timestamp,
            'label': label,
            'description': description,
            'table': table,
            'pad': pad
            }
        Print('send_event() : ', kwargs)

    def send_timestamped_event(self, key, label=None, description=None, table=None, pad=False):
        self.checkExists()
        if pad == True:
            key = make_fit(str(key))
            if table:
                newTable = {}
                for i in table:
                    table[make_fit(str(i))] = table.pop(i)
        kwargs = {
            'key': key,
            'timestamp': internal.ms_localtime(),
            'label': label,
            'description': description,
            'table': table,
            'pad': pad
            }
        Print('send_event() : ', kwargs)


if __name__ == "__main__":
    print __doc__
    print "\n === \n"
    print "module dir() listing: ", dir()
