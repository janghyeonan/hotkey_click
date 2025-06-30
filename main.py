from pynput import keyboard
import pyautogui

# 좌표 저장용 딕셔너리
saved_coordinates = {
    1: None,  # q키로 저장, 1키로 클릭
    2: None,  # w키로 저장, 2키로 클릭
    3: None,  # e키로 저장, 3키로 클릭
    4: None,  # r키로 저장, 4키로 클릭
    5: None,  # t키로 저장, 5키로 클릭
    6: None,  # y키로 저장, 6키로 클릭
    7: None,  # u키로 저장, 7키로 클릭
    8: None,  # i키로 저장, 8키로 클릭
    9: None,  # o키로 저장, 9키로 클릭
    0: None   # p키로 저장, 0키로 클릭
}

def on_press(key):
    global saved_coordinates
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
        
        # 좌표 저장 키들
        if key.char == '!':
            x, y = pyautogui.position()
            saved_coordinates[1] = (x, y)
            print(f"1번 좌표 저장: {x}, {y}")
        elif key.char == '@':
            x, y = pyautogui.position()
            saved_coordinates[2] = (x, y)
            print(f"2번 좌표 저장: {x}, {y}")
        elif key.char == '#':
            x, y = pyautogui.position()
            saved_coordinates[3] = (x, y)
            print(f"3번 좌표 저장: {x}, {y}")
        elif key.char == '$':
            x, y = pyautogui.position()
            saved_coordinates[4] = (x, y)
            print(f"4번 좌표 저장: {x}, {y}")
        elif key.char == '%':
            x, y = pyautogui.position()
            saved_coordinates[5] = (x, y)
            print(f"5번 좌표 저장: {x}, {y}")
        elif key.char == '^':
            x, y = pyautogui.position()
            saved_coordinates[6] = (x, y)
            print(f"6번 좌표 저장: {x}, {y}")
        elif key.char == '&':
            x, y = pyautogui.position()
            saved_coordinates[7] = (x, y)
            print(f"7번 좌표 저장: {x}, {y}")
        elif key.char == '*':
            x, y = pyautogui.position()
            saved_coordinates[8] = (x, y)
            print(f"8번 좌표 저장: {x}, {y}")
        elif key.char == '(':
            x, y = pyautogui.position()
            saved_coordinates[9] = (x, y)
            print(f"9번 좌표 저장: {x}, {y}")
        elif key.char == ')':
            x, y = pyautogui.position()
            saved_coordinates[0] = (x, y)
            print(f"0번 좌표 저장: {x}, {y}")
        
        # 저장된 좌표 클릭 키들
        elif key.char == '1':
            if saved_coordinates[1] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[1][0], saved_coordinates[1][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"1번 좌표 클릭: {saved_coordinates[1]}")
                except:
                    pass
            else:
                print("1번 좌표가 저장되지 않았습니다.")
        elif key.char == '2':
            if saved_coordinates[2] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[2][0], saved_coordinates[2][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"2번 좌표 클릭: {saved_coordinates[2]}")
                except:
                    pass
            else:
                print("2번 좌표가 저장되지 않았습니다.")
        elif key.char == '3':
            if saved_coordinates[3] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[3][0], saved_coordinates[3][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"3번 좌표 클릭: {saved_coordinates[3]}")
                except:
                    pass
            else:
                print("3번 좌표가 저장되지 않았습니다.")
        elif key.char == '4':
            if saved_coordinates[4] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[4][0], saved_coordinates[4][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"4번 좌표 클릭: {saved_coordinates[4]}")
                except:
                    pass
            else:
                print("4번 좌표가 저장되지 않았습니다.")
        elif key.char == '5':
            if saved_coordinates[5] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[5][0], saved_coordinates[5][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"5번 좌표 클릭: {saved_coordinates[5]}")
                except:
                    pass
            else:
                print("5번 좌표가 저장되지 않았습니다.")
        elif key.char == '6':
            if saved_coordinates[6] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[6][0], saved_coordinates[6][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"6번 좌표 클릭: {saved_coordinates[6]}")
                except:
                    pass
            else:
                print("6번 좌표가 저장되지 않았습니다.")
        elif key.char == '7':
            if saved_coordinates[7] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[7][0], saved_coordinates[7][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"7번 좌표 클릭: {saved_coordinates[7]}")
                except:
                    pass
            else:
                print("7번 좌표가 저장되지 않았습니다.")
        elif key.char == '8':
            if saved_coordinates[8] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[8][0], saved_coordinates[8][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"8번 좌표 클릭: {saved_coordinates[8]}")
                except:
                    pass
            else:
                print("8번 좌표가 저장되지 않았습니다.")
        elif key.char == '9':
            if saved_coordinates[9] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[9][0], saved_coordinates[9][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"9번 좌표 클릭: {saved_coordinates[9]}")
                except:
                    pass
            else:
                print("9번 좌표가 저장되지 않았습니다.")
        elif key.char == '0':
            if saved_coordinates[0] is not None:
                try:
                    current_x, current_y = pyautogui.position()
                    pyautogui.click(saved_coordinates[0][0], saved_coordinates[0][1])
                    pyautogui.moveTo(current_x, current_y)
                    print(f"0번 좌표 클릭: {saved_coordinates[0]}")
                except:
                    pass
            else:
                print("0번 좌표가 저장되지 않았습니다.")

    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    if key == keyboard.Key.ctrl_l:
        return False

print("프로그램 시작")
print("사용법:")
print("q: 현재 마우스 위치를 1번으로 저장")
print("w: 현재 마우스 위치를 2번으로 저장") 
print("e: 현재 마우스 위치를 3번으로 저장")
print("r: 현재 마우스 위치를 4번으로 저장")
print("t: 현재 마우스 위치를 5번으로 저장")
print("y: 현재 마우스 위치를 6번으로 저장")
print("u: 현재 마우스 위치를 7번으로 저장")
print("i: 현재 마우스 위치를 8번으로 저장")
print("o: 현재 마우스 위치를 9번으로 저장")
print("p: 현재 마우스 위치를 0번으로 저장")
print("1: 저장된 1번 좌표 클릭")
print("2: 저장된 2번 좌표 클릭")
print("3: 저장된 3번 좌표 클릭")
print("4: 저장된 4번 좌표 클릭")
print("5: 저장된 5번 좌표 클릭")
print("6: 저장된 6번 좌표 클릭")
print("7: 저장된 7번 좌표 클릭")
print("8: 저장된 8번 좌표 클릭")
print("9: 저장된 9번 좌표 클릭")
print("0: 저장된 0번 좌표 클릭")
print("왼쪽 Ctrl: 프로그램 종료")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

