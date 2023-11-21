import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")          #ここからゲームの初期化
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0                                             #ここまでゲームの初期化
    while True:                                         #ゲームは基本動き続けているので無限ループがある
        for event in pg.event.get():
            if event.type == pg.QUIT: return            #×ボタンを押すとゲームが終了する（ウィンドウが閉じる）
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [100, 400])
        pg.display.update()
        tmr += 1        
        clock.tick(1)


if __name__ == "__main__":                  #大切な部分。初期化と正常終了が明記されている
    pg.init()
    main()
    pg.quit()
    sys.exit()