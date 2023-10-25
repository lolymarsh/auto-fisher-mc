import cv2, numpy as np, time, win32gui, win32api, win32con, win32ui
from PIL import ImageGrab

cv2.startWindowThread()
win = win32gui.FindWindow(None,'Minecraft Forge* 1.20.1 - Multiplayer (3rd-party Server)') # 1378474

win_size = win32gui.GetWindowRect(win)

x, y,width,height = win_size[0], win_size[1], 850, 600

# ฟังก์ชันคลิกขวาค้าง
def HoldRightClick(x, y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, MouseXY)

# ฟังก์ชันปล่อยคลิกขวาค้าง
def ReleaseRightClick(x,y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, MouseXY)

# ฟังก์ชันคลิกขวา
def OneRightClick(x, y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, MouseXY)
    win32gui.SendMessage(win, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, MouseXY)

def FindCV2EIEI(hwnd, width, height):
    try:
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (width, height), dcObj, (0, 0), win32con.SRCCOPY)

        # Convert the screenshot to a NumPy array
        bmpstr = dataBitMap.GetBitmapBits(True)
        image = np.frombuffer(bmpstr, dtype='uint8')
        image.shape = (height, width, 4)

        return image
    except Exception as e:
        print(f"Error capturing screenshot: {str(e)}")
        return None
    finally:
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

def CapchaEIEI():
    # รูปที่เจอ
    found_feather = cv2.imread('./images/capcha/found_feater.PNG')
    found_pufferfish = cv2.imread('./images/capcha/found_pufferfish.PNG')
    found_snow_ball = cv2.imread('./images/capcha/found_snow_ball.PNG')
    # รูปที่เป็นคำตอบ
    click_feather = cv2.imread('./images/capcha/click_feather.PNG')
    click_pufferfish = cv2.imread('./images/capcha/click_pufferfish.PNG')
    click_snow_ball = cv2.imread('./images/capcha/click_snow_ball.PNG')

    while True:
        # print("Searching...")
        game_recapcha_screenshot = np.array(ImageGrab.grab(bbox=(x, y, x + width, y + height)))
        recapcha_bgr_screenshot = cv2.cvtColor(game_recapcha_screenshot, cv2.COLOR_RGB2BGR)

        fix_feather = cv2.matchTemplate(recapcha_bgr_screenshot, found_feather, cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(fix_feather)

        click_fix_feather = cv2.matchTemplate(recapcha_bgr_screenshot, click_feather, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(click_fix_feather)

        fix_pufferfish = cv2.matchTemplate(recapcha_bgr_screenshot, found_pufferfish, cv2.TM_CCOEFF_NORMED)
        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(fix_pufferfish)

        click_fix_pufferfish = cv2.matchTemplate(recapcha_bgr_screenshot, click_pufferfish, cv2.TM_CCOEFF_NORMED)
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(click_fix_pufferfish)

        fix_snow_ball = cv2.matchTemplate(recapcha_bgr_screenshot, found_snow_ball, cv2.TM_CCOEFF_NORMED)
        min_val5, max_val5, min_loc5, max_loc5 = cv2.minMaxLoc(fix_snow_ball)

        click_fix_snowball = cv2.matchTemplate(recapcha_bgr_screenshot, click_snow_ball, cv2.TM_CCOEFF_NORMED)
        min_val6, max_val6, min_loc6, max_loc6 = cv2.minMaxLoc(click_fix_snowball)

        print(max_val5)

        if max_val1 >= 0.7:
            print("Found Feather")
            target_x = x + max_loc2[0] + 15
            target_y = y + max_loc2[1] + 15
            ClickXY = win32api.MAKELONG(target_x, target_y)
            win32gui.SendMessage(win, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, ClickXY)
            win32gui.SendMessage(win, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, ClickXY)
            print("Clicked...")
            time.sleep(2)
        if max_val3 >= 0.7:
            print("Found Pufferfish")
            target_x = x + max_loc4[0] + 15
            target_y = y + max_loc4[1] + 15
            ClickXY = win32api.MAKELONG(target_x, target_y)
            win32gui.SendMessage(win, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, ClickXY)
            win32gui.SendMessage(win, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, ClickXY)
            print("Clicked...")
            time.sleep(2)
        if max_val5 >= 0.7:
            print("Found Snowball")
            target_x = x + max_loc6[0] + 15
            target_y = y + max_loc6[1] + 15
            print(target_x)
            print(target_y)
            ClickXY = win32api.MAKELONG(target_x, target_y)
            win32gui.SendMessage(win, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, ClickXY)
            win32gui.SendMessage(win, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, ClickXY)
            print("Clicked...")
            time.sleep(2)

try:
    for i in range(2, 0, -1):
        print(f"Auto Fisher Starting in {i}")
        time.sleep(1)

    # อ่านรูปภาพที่ต้องการค้นหา
    template = cv2.imread('./images/splashing.PNG')
    found_template = cv2.imread('./images/found.PNG')
    starting_holdrightclick_template = cv2.imread('./images/startholdclick.PNG')
    found_redbar_template = cv2.imread('./images/redbar.PNG')
    found_redbar2_template = cv2.imread('./images/redbar2.PNG')
    found_redbar3_template = cv2.imread('./images/redbar3.PNG')
    found_failed_template = cv2.imread('./images/failed.PNG')
    found_sucess_template = cv2.imread('./images/success.PNG')
    main_capcha_template = cv2.imread('./images/maincapcha.PNG')
    
    while True:
        # ดึงภาพหน้าจอของเกม Minecraft ตามขอบเขตที่กำหนด
        game_screenshot = FindCV2EIEI(win,850,600)
        # game_screenshot = np.array(ImageGrab.grab(bbox=(x, y, x + width, y + height)))
        bgr_screenshot = cv2.cvtColor(game_screenshot, cv2.COLOR_RGB2BGR)
       
        # ค้นหารูปภาพที่ต้องการบนหน้าจอ
        result = cv2.matchTemplate(bgr_screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # found_template
        result2 = cv2.matchTemplate(bgr_screenshot, found_template, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

        # starting_holdrightclick_template
        result3 = cv2.matchTemplate(bgr_screenshot, starting_holdrightclick_template, cv2.TM_CCOEFF_NORMED)
        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)

        # found_redbar_template
        result4 = cv2.matchTemplate(bgr_screenshot, found_redbar_template, cv2.TM_CCOEFF_NORMED)
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)

        # found_redbar2_template
        result5 = cv2.matchTemplate(bgr_screenshot, found_redbar2_template, cv2.TM_CCOEFF_NORMED)
        min_val5, max_val5, min_loc5, max_loc5 = cv2.minMaxLoc(result5)

        # found_redbar3_template
        result6 = cv2.matchTemplate(bgr_screenshot, found_redbar3_template, cv2.TM_CCOEFF_NORMED)
        min_val6, max_val6, min_loc6, max_loc6 = cv2.minMaxLoc(result6)

        main_capcha = cv2.matchTemplate(bgr_screenshot, main_capcha_template, cv2.TM_CCOEFF_NORMED)
        min_val9, max_val9, min_loc9, max_loc9 = cv2.minMaxLoc(main_capcha)

        # โชว์จอเกม
        cv2.imshow('Minecraft Screenshot', bgr_screenshot)

        if max_val9 >= 0.5:
            print("Found Capcha")
            ReleaseRightClick(x,y, win)
            CapchaEIEI()
            time.sleep(2)
        elif max_val < 0.45:  # ตรวจสอบว่ารูปภาพไม่ถูกพบ
            print("Splashing not found. Right-clicking...")
            ReleaseRightClick(x,y, win)
            OneRightClick(x,y, win)  # คลิกขวาหากไม่พบรูปภาพ
            time.sleep(1)  # รอสั้นๆ ก่อนที่จะค้นหาอีกครั้ง
        elif max_val2 >= 0.6:
            print("Found Fish Right-clicking...")
            OneRightClick(x,y, win)
            time.sleep(2)
            print("Starting Level 1 Right-clicking...")
            HoldRightClick(x,y, win)
        elif max_val3 >= 0.6:
            print("Starting Level 2 Right-clicking...")
            HoldRightClick(x,y, win)
        elif max_val4 >= 0.45:
            print("Found Redbar Level 1 Released Right-clicking...")
            ReleaseRightClick(x,y, win)
            time.sleep(3)
            HoldRightClick(x,y, win)
        elif max_val5 >= 0.5:
            print("Found Redbar Level 2 Released Right-clicking...")
            ReleaseRightClick(x,y, win)
            time.sleep(3)
            HoldRightClick(x,y, win)
        elif max_val6 >= 0.5:
            print("Found Redbar Level 3 Released Right-clicking...")
            ReleaseRightClick(x,y, win)
            time.sleep(3)
            HoldRightClick(x,y, win)

        cv2.waitKey(1)
        
except KeyboardInterrupt:
    print("หยุดโปรแกรม")
    cv2.destroyAllWindows()
