# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print('type of input is: %s' % (type(environ)), '\n', environ['PATH_INFO'])
    # environ['PATH_INFO']就是浏览器地址栏里localhost:8000后的部分
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web') # [1:]去掉'/'
    return [body.encode()] # 返回值类型是bytes
