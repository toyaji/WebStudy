# 초경량 서버 운용을 위한 모듈임 - 개발 및 연구용 서버로 사용할 수 있음
import bottle

@bottle.route('/')
def home_server():
    return 'Hello Paul'

@bottle.route('/secondpage')
def second_page():
    return "This is Second"

bottle.debug(True)
bottle.run(host='Localhost', port=8000)