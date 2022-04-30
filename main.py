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
pos_x1 = 699.2
pos_y1 = 52.7
pos_x2 = 7.5
pos_y2 = 8.9
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
    level_area = pygame.draw.rect(screen,(0,0,0),(94.7,46.4,36.3,27.6),1)
    level_point_area = pygame.draw.rect(screen,(0,0,0),(131.3,45.3,52.6,30.5),1)
    gem_area = pygame.draw.rect(screen,(255,255,255),(288.8,43.4,60.3,32.6),1)
    coin_area = pygame.draw.rect(screen,(255,255,255),(427.7,44.3,111.4,30.2),1)
    heart_1 = pygame.draw.rect(screen,(255,255,255),(686.2,52.7,7.5,8.9),1)
    heart_2 = pygame.draw.rect(screen,(255,255,255),(699.2,52.7,7.5,8.9),1)
    heart_3 = pygame.draw.rect(screen,(255,255,255),(711.9,52.7,7.5,8.9),1)
    heart_4 = pygame.draw.rect(screen,(255,255,255),(723,52.7,7.5,8.9),1)
    heart_5 = pygame.draw.rect(screen,(255,255,255),(736.2,52.7,7.5,8.9),1)
    start_button_1 = pygame.draw.rect(screen,(255,255,255),(673.4,507.4,148.2,54.2),1)
    start_button_2 = pygame.draw.rect(screen,(255,255,255),(633.1,485.4,146.8,49.3),1)
    end_coin = pygame.draw.rect(screen,(255,255,255),(751.6,316.5,142.5,61.3),1)
    end_button = pygame.draw.rect(screen,(255,255,255),(319.4,503.2,93.5,60.6),1)
    end_box = pygame.draw.rect(screen,(255,255,255),(428.9,506.2,157.3,51),1)
    end_box_ok = pygame.draw.rect(screen,(255,255,255),(462.9,508.1,80,47.7),1)

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