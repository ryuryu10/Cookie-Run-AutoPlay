import pygame
import win32api
import win32con
import win32gui
import keyboard


#---------------------FOR PYGAME----------------------
def Get_Game_Window():
    hwnd = win32gui.FindWindow(None,"BlueStacks App Player")
    windowrect = win32gui.GetWindowRect(hwnd)
    x = windowrect[0] - 5
    y = windowrect[1]
    width = windowrect[2] - x
    height = windowrect[3] - y
    #print(x, y, width, height)
    #1000, 593
    return x, y, width, height
    

def Track_Game():
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], -1, Get_Game_Window()[0], Get_Game_Window()[1], 0, 0, 0x0001)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((Get_Game_Window()[2], Get_Game_Window()[3]), pygame.NOFRAME)
hack_running = True
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)
white = (255,255,255)

overlay_font = pygame.font.SysFont(None, 30)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
pos_x1 = 200
pos_y1 = 200
pos_x2 = 200
pos_y2 = 200
switched = 1
while hack_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hack_running = False

    Track_Game() #Make sure overlay follows AC
    screen.fill(fuchsia)  # Transparent background fuchsia
    #pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))

    #PYGAME TEXT UPDATES:
    local_text = overlay_font.render("Cook2Run", True, (255, 255, 255))
    local2_text = overlay_font.render("__________________", True, (255, 0, 0))
    x_text = overlay_font.render("X: ", True, (255, 0, 0))
    y_text = overlay_font.render("Y: ", True, (255, 0, 0))
    z_text = overlay_font.render("Z: ", True, (255, 0, 0))
    level_area = pygame.draw.rect(screen,(255,255,255),(94.7,46.4,36.3,27.6),1)
    level_point_area = pygame.draw.rect(screen,(255,255,255),(131.3,45.3,52.6,30.5),1)
    gem_area = pygame.draw.rect(screen,(255,255,255),(288.8,43.4,60.3,32.6),1)
    coin_area = pygame.draw.rect(screen,(255,255,255),(427.7,44.3,111.4,30.2),1)



    a = pygame.draw.rect(screen,(255,255,255),(pos_x1,pos_y1,pos_x2,pos_y2),1)
    print(pos_x1,pos_y1,pos_x2,pos_y2)
    if keyboard.is_pressed("q"):
        if switched == 1:
            switched = 0
        else :
            switched = 1

    if keyboard.is_pressed("a"):
        if switched == 1:
            pos_x1 -= 0.1
        else:
            pos_x2 -= 0.1

    if keyboard.is_pressed("d"):
        if switched == 1:
            pos_x1 += 0.1
        else:
            pos_x2 += 0.1

    if keyboard.is_pressed("w"):
        if switched == 1:
            pos_y1 -= 0.1
        else:
            pos_y2 -= 0.1

    if keyboard.is_pressed("s"):
        if switched == 1:
            pos_y1 += 0.1
        else:
            pos_y2 += 0.1

    #OVERLAY DRAWS:
    screen.blit(local_text, (15,40))
    screen.blit(local2_text, (15,42))
    screen.blit(x_text, (15,65))
    screen.blit(y_text, (15,85))
    screen.blit(z_text, (15,105))
    pygame.display.update()

    if keyboard.is_pressed("k"): #Press K to exit hack.
        hack_running = False
        pygame.quit()
        quit()