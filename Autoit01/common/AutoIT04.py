


def isclientupdate():
    '''判断包是否需要升级'''
    w_clientupdate = winControl.WinControl(title_update)
    w_clientupdate_choice = winControl.WinControl(title_choice)
    flag = True
    count = 0
    while flag:
        if w_clientupdate.exists():
            clientupdate()
            flag = False
        elif w_clientupdate_choice.exists():
            w_clientupdate_choice.controlClick('Button2')
            clientupdate()
            flag = False
        else:
            time.sleep(1)
            count += 1
            if count == 5:
                clientlogin()
                flag = False