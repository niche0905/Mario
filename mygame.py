import game_framework
import pico2d

# 추가할 스테이트 임포트
import logo_state

pico2d.open_canvas()
game_framework.run(logo_state)
pico2d.close_canvas()