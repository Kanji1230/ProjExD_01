import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")       #ゲームの初期化    左上のタイトルを設定する部分
    screen = pg.display.set_mode((800, 600))                #windowの大きさを指定(800, 600) displayモジュールの中のset_mode()
    clock  = pg.time.Clock()                                #while文の中のclock.tick()で利用している。引数はフレームレート
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")            #imageモジュールのなかのload関数を利用して画像を読み込んでいる。戻り値はsurfaceクラス。練習1
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 4, 1.0), pg.transform.rotozoom(kk_img, 8, 1.0), pg.transform.rotozoom(kk_img, 12, 1.0), pg.transform.rotozoom(kk_img, 16, 1.0), pg.transform.rotozoom(kk_img, 12, 1.0), pg.transform.rotozoom(kk_img, 8, 1.0), pg.transform.rotozoom(kk_img, 4, 1.0)]  #こうかとんsurfaceのリスト。練習3
    tmr = 0
    while True:                                         #無限ループ
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        screen.blit(bg_img, [-x , 0]) 
        screen.blit(pg.transform.flip(bg_img, True, False), [1600 - x, 0])
        screen.blit(bg_img, (3200 - x, 0))
        screen.blit(kk_imgs[tmr % 4], (300, 200))                        #bg_imgをblit(貼り付けて)いる。座標をべた書きすると移動しない。.get.
        pg.display.update()                                 #blitしたらapdateする。基本的にはwhile分の最後に入る
        tmr += 1        
        clock.tick(20)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()