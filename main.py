import cv2, numpy as np, time, win32gui, win32api, win32con, win32ui, keyboard
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

def ClickLeftAtPoint(window, x, y):
    ClickXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(window,win32con.WM_MOUSEMOVE,None,ClickXY)
    win32gui.SendMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, ClickXY)
    time.sleep(0.1)  
    win32gui.SendMessage(window, win32con.WM_LBUTTONUP, 0, ClickXY)

def CapchaEIEI():
    # รูปที่เจอ
    found_feather = cv2.imread('./images/capcha/found_feater.PNG')
    found_pufferfish = cv2.imread('./images/capcha/found_pufferfish.PNG')
    found_snow_ball = cv2.imread('./images/capcha/found_snow_ball.PNG')
    found_honeycomb = cv2.imread('./images/capcha/found_honeycomb.PNG')
    found_cake = cv2.imread('./images/capcha/found_cake.PNG')
    found_egg = cv2.imread('./images/capcha/found_egg.PNG')
    found_potato = cv2.imread('./images/capcha/found_potato.PNG')
    found_beetroot = cv2.imread('./images/capcha/found_beetroot.PNG')
    found_chicken = cv2.imread('./images/capcha/found_chicken.PNG')
    found_apple = cv2.imread('./images/capcha/found_apple.PNG')
    found_bone = cv2.imread('./images/capcha/found_bone.PNG')
    found_brush = cv2.imread('./images/capcha/found_brush.PNG')
    found_coal = cv2.imread('./images/capcha/found_coal.PNG')
    found_spyglass = cv2.imread('./images/capcha/found_spyglass.PNG')
    found_brick = cv2.imread('./images/capcha/found_brick.PNG')
    found_cod = cv2.imread('./images/capcha/found_cod.PNG')
    found_carrot = cv2.imread('./images/capcha/found_carrot.PNG')
    found_sugar = cv2.imread('./images/capcha/found_sugar.PNG')
    found_diamond = cv2.imread('./images/capcha/found_diamond.PNG')
    found_emerald = cv2.imread('./images/capcha/found_emerald.PNG')
    found_redstone = cv2.imread('./images/capcha/found_redstone.PNG')
    found_book = cv2.imread('./images/capcha/found_book.PNG')
    found_cookie = cv2.imread('./images/capcha/found_cookie.PNG')
    found_bucket = cv2.imread('./images/capcha/found_bucket.PNG')
    found_bamboo = cv2.imread('./images/capcha/found_bamboo.PNG')
    
    # รูปที่เป็นคำตอบ
    click_feather = cv2.imread('./images/capcha/click_feather.PNG')
    click_pufferfish = cv2.imread('./images/capcha/click_pufferfish.PNG')
    click_snow_ball = cv2.imread('./images/capcha/click_snow_ball.PNG')
    click_honeycomb = cv2.imread('./images/capcha/click_honeycomb.PNG')
    click_cake = cv2.imread('./images/capcha/click_cake.PNG')
    click_egg = cv2.imread('./images/capcha/click_egg.PNG')
    click_potato = cv2.imread('./images/capcha/click_potato.PNG')
    click_beetroot = cv2.imread('./images/capcha/click_beetroot.PNG')
    click_chicken = cv2.imread('./images/capcha/click_chicken.PNG')
    click_apple = cv2.imread('./images/capcha/click_apple.PNG')
    click_bone = cv2.imread('./images/capcha/click_bone.PNG')
    click_brush = cv2.imread('./images/capcha/click_brush.PNG')
    click_coal = cv2.imread('./images/capcha/click_coal.PNG')
    click_spyglass = cv2.imread('./images/capcha/click_spyglass.PNG')
    click_brick = cv2.imread('./images/capcha/click_brick.PNG')
    click_cod = cv2.imread('./images/capcha/click_cod.PNG')
    click_carrot = cv2.imread('./images/capcha/click_carrot.PNG')
    click_sugar = cv2.imread('./images/capcha/click_sugar.PNG')
    click_diamond = cv2.imread('./images/capcha/click_diamond.PNG')
    click_emerald = cv2.imread('./images/capcha/click_emerald.PNG')
    click_redstone = cv2.imread('./images/capcha/click_redstone.PNG')
    click_book = cv2.imread('./images/capcha/click_book.PNG')
    click_cookie = cv2.imread('./images/capcha/click_cookie.PNG')
    click_bucket = cv2.imread('./images/capcha/click_bucket.PNG')
    click_bamboo = cv2.imread('./images/capcha/click_bamboo.PNG')

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
        
        fix_honeycomb = cv2.matchTemplate(recapcha_bgr_screenshot, found_honeycomb, cv2.TM_CCOEFF_NORMED)
        min_val7, max_val7, min_loc7, max_loc7 = cv2.minMaxLoc(fix_honeycomb)
        
        click_fix_honeycomb = cv2.matchTemplate(recapcha_bgr_screenshot, click_honeycomb, cv2.TM_CCOEFF_NORMED)
        min_val8, max_val8, min_loc8, max_loc8 = cv2.minMaxLoc(click_fix_honeycomb)
        
        fix_cake = cv2.matchTemplate(recapcha_bgr_screenshot, found_cake, cv2.TM_CCOEFF_NORMED)
        min_val9, max_val9, min_loc9, max_loc9 = cv2.minMaxLoc(fix_cake)
        
        click_fix_cake = cv2.matchTemplate(recapcha_bgr_screenshot, click_cake, cv2.TM_CCOEFF_NORMED)
        min_val10, max_val10, min_loc10, max_loc10 = cv2.minMaxLoc(click_fix_cake)
        
        fix_egg = cv2.matchTemplate(recapcha_bgr_screenshot, found_egg, cv2.TM_CCOEFF_NORMED)
        min_val11, max_val11, min_loc11, max_loc11 = cv2.minMaxLoc(fix_egg)
        
        click_fix_egg = cv2.matchTemplate(recapcha_bgr_screenshot, click_egg, cv2.TM_CCOEFF_NORMED)
        min_val12, max_val12, min_loc12, max_loc12 = cv2.minMaxLoc(click_fix_egg)
        
        fix_potato = cv2.matchTemplate(recapcha_bgr_screenshot, found_potato, cv2.TM_CCOEFF_NORMED)
        min_val13, max_val13, min_loc13, max_loc13 = cv2.minMaxLoc(fix_potato)
        
        click_fix_potato = cv2.matchTemplate(recapcha_bgr_screenshot, click_potato, cv2.TM_CCOEFF_NORMED)
        min_val14, max_val14, min_loc14, max_loc14 = cv2.minMaxLoc(click_fix_potato)
        
        fix_beetroot = cv2.matchTemplate(recapcha_bgr_screenshot, found_beetroot, cv2.TM_CCOEFF_NORMED)
        min_val15, max_val15, min_loc15, max_loc15 = cv2.minMaxLoc(fix_beetroot)
        
        click_fix_beetroot = cv2.matchTemplate(recapcha_bgr_screenshot, click_beetroot, cv2.TM_CCOEFF_NORMED)
        min_val16, max_val16, min_loc16, max_loc16 = cv2.minMaxLoc(click_fix_beetroot)
        
        fix_chicken = cv2.matchTemplate(recapcha_bgr_screenshot, found_chicken, cv2.TM_CCOEFF_NORMED)
        min_val17, max_val17, min_loc17, max_loc17 = cv2.minMaxLoc(fix_chicken)
        
        click_fix_chicken = cv2.matchTemplate(recapcha_bgr_screenshot, click_chicken, cv2.TM_CCOEFF_NORMED)
        min_val18, max_val18, min_loc18, max_loc18 = cv2.minMaxLoc(click_fix_chicken)
        
        fix_apple = cv2.matchTemplate(recapcha_bgr_screenshot, found_apple, cv2.TM_CCOEFF_NORMED)
        min_val19, max_val19, min_loc19, max_loc19 = cv2.minMaxLoc(fix_apple)
        
        click_fix_apple = cv2.matchTemplate(recapcha_bgr_screenshot, click_apple, cv2.TM_CCOEFF_NORMED)
        min_val20, max_val20, min_loc20, max_loc20 = cv2.minMaxLoc(click_fix_apple)
        
        fix_bone = cv2.matchTemplate(recapcha_bgr_screenshot, found_bone, cv2.TM_CCOEFF_NORMED)
        min_val21, max_val21, min_loc21, max_loc21 = cv2.minMaxLoc(fix_bone)
        
        click_fix_bone = cv2.matchTemplate(recapcha_bgr_screenshot, click_bone, cv2.TM_CCOEFF_NORMED)
        min_val22, max_val22, min_loc22, max_loc22 = cv2.minMaxLoc(click_fix_bone)
        
        fix_brush = cv2.matchTemplate(recapcha_bgr_screenshot, found_brush, cv2.TM_CCOEFF_NORMED)
        min_val23, max_val23, min_loc23, max_loc23 = cv2.minMaxLoc(fix_brush)
        
        click_fix_brush = cv2.matchTemplate(recapcha_bgr_screenshot, click_brush, cv2.TM_CCOEFF_NORMED)
        min_val24, max_val24, min_loc24, max_loc24 = cv2.minMaxLoc(click_fix_brush)
        
        fix_coal = cv2.matchTemplate(recapcha_bgr_screenshot, found_coal, cv2.TM_CCOEFF_NORMED)
        min_val25, max_val25, min_loc25, max_loc25 = cv2.minMaxLoc(fix_coal)
        
        click_fix_coal = cv2.matchTemplate(recapcha_bgr_screenshot, click_coal, cv2.TM_CCOEFF_NORMED)
        min_val26, max_val26, min_loc26, max_loc26 = cv2.minMaxLoc(click_fix_coal)
        
        fix_spyglass = cv2.matchTemplate(recapcha_bgr_screenshot, found_spyglass, cv2.TM_CCOEFF_NORMED)
        min_val27, max_val27, min_loc27, max_loc27 = cv2.minMaxLoc(fix_spyglass)
        
        click_fix_spyglass = cv2.matchTemplate(recapcha_bgr_screenshot, click_spyglass, cv2.TM_CCOEFF_NORMED)
        min_val28, max_val28, min_loc28, max_loc28 = cv2.minMaxLoc(click_fix_spyglass)
        
        fix_brick = cv2.matchTemplate(recapcha_bgr_screenshot, found_brick, cv2.TM_CCOEFF_NORMED)
        min_val29, max_val29, min_loc29, max_loc29 = cv2.minMaxLoc(fix_brick)
        
        click_fix_brick = cv2.matchTemplate(recapcha_bgr_screenshot, click_brick, cv2.TM_CCOEFF_NORMED)
        min_val30, max_val30, min_loc30, max_loc30 = cv2.minMaxLoc(click_fix_brick)
        
        fix_cod = cv2.matchTemplate(recapcha_bgr_screenshot, found_cod, cv2.TM_CCOEFF_NORMED)
        min_val31, max_val31, min_loc31, max_loc31 = cv2.minMaxLoc(fix_cod)
        
        click_fix_cod = cv2.matchTemplate(recapcha_bgr_screenshot, click_cod, cv2.TM_CCOEFF_NORMED)
        min_val32, max_val32, min_loc32, max_loc32 = cv2.minMaxLoc(click_fix_cod)

        fix_carrot = cv2.matchTemplate(recapcha_bgr_screenshot, found_carrot, cv2.TM_CCOEFF_NORMED)
        min_val33, max_val33, min_loc33, max_loc33 = cv2.minMaxLoc(fix_carrot)
        
        click_fix_carrot = cv2.matchTemplate(recapcha_bgr_screenshot, click_carrot, cv2.TM_CCOEFF_NORMED)
        min_val34, max_val34, min_loc34, max_loc34 = cv2.minMaxLoc(click_fix_carrot)
        
        fix_sugar = cv2.matchTemplate(recapcha_bgr_screenshot, found_sugar, cv2.TM_CCOEFF_NORMED)
        min_val35, max_val35, min_loc35, max_loc35 = cv2.minMaxLoc(fix_sugar)
        
        click_fix_sugar = cv2.matchTemplate(recapcha_bgr_screenshot, click_sugar, cv2.TM_CCOEFF_NORMED)
        min_val36, max_val36, min_loc36, max_loc36 = cv2.minMaxLoc(click_fix_sugar)
        
        fix_diamond = cv2.matchTemplate(recapcha_bgr_screenshot, found_diamond, cv2.TM_CCOEFF_NORMED)
        min_val37, max_val37, min_loc37, max_loc37 = cv2.minMaxLoc(fix_diamond)
        
        click_fix_diamond = cv2.matchTemplate(recapcha_bgr_screenshot, click_diamond, cv2.TM_CCOEFF_NORMED)
        min_val38, max_val38, min_loc38, max_loc38 = cv2.minMaxLoc(click_fix_diamond)
        
        fix_emerald = cv2.matchTemplate(recapcha_bgr_screenshot, found_emerald, cv2.TM_CCOEFF_NORMED)
        min_val39, max_val39, min_loc39, max_loc39 = cv2.minMaxLoc(fix_emerald)
        
        click_fix_emerald = cv2.matchTemplate(recapcha_bgr_screenshot, click_emerald, cv2.TM_CCOEFF_NORMED)
        min_val40, max_val40, min_loc40, max_loc40 = cv2.minMaxLoc(click_fix_emerald)
        
        fix_redstone = cv2.matchTemplate(recapcha_bgr_screenshot, found_redstone, cv2.TM_CCOEFF_NORMED)
        min_val41, max_val41, min_loc41, max_loc41 = cv2.minMaxLoc(fix_redstone)
        
        click_fix_redstone = cv2.matchTemplate(recapcha_bgr_screenshot, click_redstone, cv2.TM_CCOEFF_NORMED)
        min_val42, max_val42, min_loc42, max_loc42 = cv2.minMaxLoc(click_fix_redstone)
        
        fix_book = cv2.matchTemplate(recapcha_bgr_screenshot, found_book, cv2.TM_CCOEFF_NORMED)
        min_val43, max_val43, min_loc43, max_loc43 = cv2.minMaxLoc(fix_book)
        
        click_fix_book = cv2.matchTemplate(recapcha_bgr_screenshot, click_book, cv2.TM_CCOEFF_NORMED)
        min_val44, max_val44, min_loc44, max_loc44 = cv2.minMaxLoc(click_fix_book)
        
        fix_cookie = cv2.matchTemplate(recapcha_bgr_screenshot, found_cookie, cv2.TM_CCOEFF_NORMED)
        min_val45, max_val45, min_loc45, max_loc45 = cv2.minMaxLoc(fix_cookie)
        
        click_fix_cookie = cv2.matchTemplate(recapcha_bgr_screenshot, click_cookie, cv2.TM_CCOEFF_NORMED)
        min_val46, max_val46, min_loc46, max_loc46 = cv2.minMaxLoc(click_fix_cookie)
        
        fix_bucket = cv2.matchTemplate(recapcha_bgr_screenshot, found_bucket, cv2.TM_CCOEFF_NORMED)
        min_val47, max_val47, min_loc47, max_loc47 = cv2.minMaxLoc(fix_bucket)
        
        click_fix_bucket = cv2.matchTemplate(recapcha_bgr_screenshot, click_bucket, cv2.TM_CCOEFF_NORMED)
        min_val48, max_val48, min_loc48, max_loc48 = cv2.minMaxLoc(click_fix_bucket)
        
        fix_bamboo = cv2.matchTemplate(recapcha_bgr_screenshot, found_bamboo, cv2.TM_CCOEFF_NORMED)
        min_val49, max_val49, min_loc49, max_loc49 = cv2.minMaxLoc(fix_bamboo)
        
        click_fix_bamboo = cv2.matchTemplate(recapcha_bgr_screenshot, click_bamboo, cv2.TM_CCOEFF_NORMED)
        min_val50, max_val50, min_loc50, max_loc50 = cv2.minMaxLoc(click_fix_bamboo)

        if max_val1 >= 0.8:
            print("Found Feather")
            target_x = x + max_loc2[0] 
            target_y = y + max_loc2[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val3 >= 0.8:
            print("Found Pufferfish")
            target_x = x + max_loc4[0]
            target_y = y + max_loc4[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            print("Clicked...")
            time.sleep(2)
        if max_val5 >= 0.8:
            print("Found Snowball")
            target_x = x + max_loc6[0] 
            target_y = y + max_loc6[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val7 >= 0.8:
            print("Found Honeycomb")
            target_x = x + max_loc8[0]
            target_y = y + max_loc8[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val9 >= 0.8:
            print("Found cake")
            target_x = x + max_loc10[0]
            target_y = y + max_loc10[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val11 >= 0.8:
            print("Found egg")
            target_x = x + max_loc12[0] 
            target_y = y + max_loc12[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val13 >= 0.8:
            print("Found potato")
            target_x = x + max_loc14[0]
            target_y = y + max_loc14[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val15 >= 0.8:
            print("Found beetroot")
            target_x = x + max_loc16[0] 
            target_y = y + max_loc16[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val17 >= 0.8:
            print("Found chicken")
            target_x = x + max_loc18[0] 
            target_y = y + max_loc18[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val19 >= 0.8:
            print("Found apple")
            target_x = x + max_loc20[0] 
            target_y = y + max_loc20[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val21 >= 0.8:
            print("Found bone")
            target_x = x + max_loc22[0]
            target_y = y + max_loc22[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val23 >= 0.8:
            print("Found brush")
            target_x = x + max_loc24[0] 
            target_y = y + max_loc24[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val25 >= 0.8:
            print("Found coal")
            target_x = x + max_loc26[0] 
            target_y = y + max_loc26[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val27 >= 0.8:
            print("Found spyglass")
            target_x = x + max_loc28[0] 
            target_y = y + max_loc28[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val29 >= 0.8:
            print("Found brick")
            target_x = x + max_loc30[0] 
            target_y = y + max_loc30[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val31 >= 0.8:
            print("Found cod")
            target_x = x + max_loc32[0] 
            target_y = y + max_loc32[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val33 >= 0.8:
            print("Found carrot")
            target_x = x + max_loc34[0] 
            target_y = y + max_loc34[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val35 >= 0.8:
            print("Found sugar")
            target_x = x + max_loc36[0] 
            target_y = y + max_loc36[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
        if max_val37 >= 0.8:
            print("Found diamond")
            target_x = x + max_loc38[0] 
            target_y = y + max_loc38[1] - 5 
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val39 >= 0.8:
            print("Found emerald")
            target_x = x + max_loc40[0] 
            target_y = y + max_loc40[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val41 >= 0.8:
            print("Found redstone")
            target_x = x + max_loc42[0] 
            target_y = y + max_loc42[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val43 >= 0.8:
            print("Found book")
            target_x = x + max_loc44[0]
            target_y = y + max_loc44[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val45 >= 0.8:
            print("Found cookie")
            target_x = x + max_loc46[0] 
            target_y = y + max_loc46[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val47 >= 0.8:
            print("Found bucket")
            target_x = x + max_loc48[0] 
            target_y = y + max_loc48[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        if max_val49 >= 0.8:
            print("Found bamboo")
            target_x = x + max_loc50[0] 
            target_y = y + max_loc50[1] - 25
            ClickLeftAtPoint(win, target_x, target_y)
            print("Clicked...")
            time.sleep(2)
        else:
            break

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
            time.sleep(2)
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
