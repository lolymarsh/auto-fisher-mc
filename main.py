import cv2, sys, numpy as np, pyautogui, time, win32gui, win32api, win32con

# ฟังก์ชันคลิกขวาค้าง
def right_click_and_hold(x, y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, MouseXY)

# ฟังก์ชันปล่อยคลิกขวาค้าง
def release_right_click(x,y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, MouseXY)

# ฟังก์ชันคลิกขวา
def one_right_click(x, y, win):
    MouseXY = win32api.MAKELONG(x, y)
    win32gui.SendMessage(win, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, MouseXY)
    win32gui.SendMessage(win, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, MouseXY)

try:
    for i in range(5, 0, -1):
        print(f"Auto Fisher Starting in {i}")
        time.sleep(1)

    cv2.startWindowThread()
    win = win32gui.FindWindow(None,'Minecraft Forge* 1.20.1 - Multiplayer (3rd-party Server)') # 1378474

    if win == 0:
        print("Window not found. Exiting...")
        sys.exit(1)

    win_size = win32gui.GetWindowRect(win)

    x, y,width,height = win_size[0], win_size[1], 850, 600

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

    game_region = (x, y, width, height)
    # win32api.SetCursorPos((x, y))
    
    while True:
        # ดึงภาพหน้าจอปัจจุบัน
        screenshot = np.array(pyautogui.screenshot())

        # ดึงภาพหน้าจอของเกม Minecraft ตามขอบเขตที่กำหนด
        game_screenshot = screenshot[y:y + height, x:x + width]
       
        # ค้นหารูปภาพที่ต้องการบนหน้าจอ
        result = cv2.matchTemplate(game_screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # found_template
        result2 = cv2.matchTemplate(game_screenshot, found_template, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

        # starting_holdrightclick_template
        result3 = cv2.matchTemplate(game_screenshot, starting_holdrightclick_template, cv2.TM_CCOEFF_NORMED)
        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)

        # found_redbar_template
        result4 = cv2.matchTemplate(game_screenshot, found_redbar_template, cv2.TM_CCOEFF_NORMED)
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)

        # found_redbar2_template
        result5 = cv2.matchTemplate(game_screenshot, found_redbar2_template, cv2.TM_CCOEFF_NORMED)
        min_val5, max_val5, min_loc5, max_loc5 = cv2.minMaxLoc(result5)

        # found_redbar3_template
        result6 = cv2.matchTemplate(game_screenshot, found_redbar3_template, cv2.TM_CCOEFF_NORMED)
        min_val6, max_val6, min_loc6, max_loc6 = cv2.minMaxLoc(result6)

        main_capcha = cv2.matchTemplate(game_screenshot, main_capcha_template, cv2.TM_CCOEFF_NORMED)
        min_val9, max_val9, min_loc9, max_loc9 = cv2.minMaxLoc(main_capcha)
        # โชว์จอเกม
        # cv2.imshow('Minecraft Screenshot', game_screenshot)
        if max_val9 >= 0.5:
            print("Found Capcha")
            release_right_click(x,y, win)
            time.sleep(2)
        elif max_val < 0.45:  # ตรวจสอบว่ารูปภาพไม่ถูกพบ
            print("Splashing not found. Right-clicking...")
            release_right_click(x,y, win)
            one_right_click(x,y, win)  # คลิกขวาหากไม่พบรูปภาพ
            time.sleep(1)  # รอสั้นๆ ก่อนที่จะค้นหาอีกครั้ง
        elif max_val2 >= 0.6:
            print("Found Fish Right-clicking...")
            one_right_click(x,y, win)
            time.sleep(2)
            print("Starting Level 1 Right-clicking...")
            right_click_and_hold(x,y, win)
        elif max_val3 >= 0.6:
            print("Starting Level 2 Right-clicking...")
            right_click_and_hold(x,y, win)
        elif max_val4 >= 0.45:
            print("Found Redbar Level 1 Released Right-clicking...")
            release_right_click(x,y, win)
            time.sleep(3)
            right_click_and_hold(x,y, win)
        elif max_val5 >= 0.5:
            print("Found Redbar Level 2 Released Right-clicking...")
            release_right_click(x,y, win)
            time.sleep(3)
            right_click_and_hold(x,y, win)
        elif max_val6 >= 0.5:
            print("Found Redbar Level 3 Released Right-clicking...")
            release_right_click(x,y, win)
            time.sleep(3)
            right_click_and_hold(x,y, win)

        cv2.waitKey(1)
        
except KeyboardInterrupt:
    print("หยุดโปรแกรม")
    cv2.destroyAllWindows()
