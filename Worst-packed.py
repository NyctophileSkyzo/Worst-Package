#i/urs/bin/python3.11
try:
    __Minh_x_Uyen__=locals()
    __DATE_OBF__ = '2024-04-23 - Admin (UTC)'
    __Mode_ENC__  = '3.11.6 -> (HIGH - main) - version: 1.0.2'
    __OBFUSCATION_BY__ = 'MinhNguyen2412_x_NgocUyen1907'
    __OBEJCTPROGRAM__ = __import__('builtins').eval
    class PyObject:
        def PythonCodeObject(code: int) -> int:return code*2
        def Obfuscator(code_, _code: (...,)) -> (...,):__Minh_x_Uyen__[code_] = _code;return __Minh_x_Uyen__[code_]
        def Windows(code):
            code_ = []
            while code:
                Minh_Nguyen = __import__('_bz2').BZ2Decompressor()
                try:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Minh_Nguyen.unused_data
            return b"".join(code_)
        def KaliLinux(code, format=__import__('_lzma').FORMAT_AUTO, memlimit=None, filters=None):
            code_ = []
            while True:
                Ngoc_Uyen = __import__('_lzma').LZMADecompressor(format, memlimit, filters)
                try:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Ngoc_Uyen.unused_data
                if not code:break
            return b"".join(code_)
    __OBEJCTPROGRAM__(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except (Exception, KeyboardInterrupt, OSError, ImportError) as e:__import__('logging').error(__import__('traceback').format_exc())