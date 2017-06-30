import mmap

def file_to_strings(filename):
    """
    binary file to strings
    :param filename:
    :return:
    """
    fd = None
    __data__ = None
    try:
        fd = open(filename, 'rb')
        file_no = fd.fileno()
        if hasattr(mmap, 'MAP_PRIVATE'):
            # Unix
            __data__ = mmap.mmap(file_no, 0, mmap.MAP_PRIVATE)
        else:
            # Windows
            __data__ = mmap.mmap(file_no, 0, access=mmap.ACCESS_READ)
    except IOError as excp:
        exception_msg = '{0}'.format(excp)
        if exception_msg:
            exception_msg = ': %s' % exception_msg
        raise Exception('Unable to access file \'{0}\'{1}'.format(filename, exception_msg))
    finally:
        if fd:
            fd.close()
            return __data__
        else:
            return None
