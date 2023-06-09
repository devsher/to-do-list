# -*- coding: utf-8 -*-
"""To Do list

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13stebAZxF1v3T0Cd8sbj3Rwl7mwqktmH
"""



to_do_list = []

while True:
    print("1: 할 일 추가")
    print("2: 할 일 삭제")
    print("3: 할 일 목록 보기")
    print("4: 종료")
    
    try:
        choice = int(input("선택: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue
    
    if choice == 1:
        task = input("할 일을 입력하세요: ")
        to_do_list.append(task)
        print("할 일이 추가되었습니다.")
    elif choice == 2:
        task = input("삭제할 할 일을 입력하세요: ")
        if task in to_do_list:
            to_do_list.remove(task)
            print("할 일이 삭제되었습니다.")
        else:
            print("해당 할 일을 찾을 수 없습니다.")
    elif choice == 3:
        print("할 일 목록:")
        for task in to_do_list:
            print("- " + task)
    elif choice == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")

