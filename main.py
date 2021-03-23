# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def renameFile():
    count = 0
    # 需要重命名的文件位置
    path = 'E:\\UI\\LottieFiles\\3个小球\\3个小球序列帧\\'
    filelist = os.listdir(path)
    for item in filelist:
    # print('item name is ',item)
        if item.endswith('.png'):
            # 文件名称
            name = "anim_loading_" + str(count) + ".png"
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(path), name)
            try:
                os.rename(src, dst)
                print('rename from %s to %s' % (src, dst))
                count += 1
            except:
                continue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    renameFile()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

