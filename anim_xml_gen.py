import sys
import os

# imageName = sys.argv[1]
# num = sys.argv[2]
# order = sys.argv[1]
# duration = sys.argv[2]
# outfile = sys.argv[3]

# order = raw_input("请输入顺序（True正序 False 逆序,默认False）:\n")
# if order.replace(' ', '')=="":
#     order = False
#
# oneshot = raw_input("是否循环（true循环 false不循环,默认true）:\n")
# if oneshot.replace(' ', '')=="":
#     oneshot = "true"
#
# duration = raw_input("请输入duration（默认100）:\n")
# if duration.replace(' ', '')=="":
#     duration = 100
# outfile = raw_input("请输入文件夹:\n")
# outfile = outfile.replace(' ', '')
# while outfile=="":
#     outfile = raw_input("请输入文件夹:\n")
#     outfile = outfile.replace(' ', '')

# 顺序（True正序 False 逆序,默认False）
order = True
# 是否循环（true循环 false不循环,默认true）
oneshot = True
# 请输入duration（默认100）
duration = 40
# 文件夹地址
outfile = "E:\\UI\\LottieFiles\\3个小球\\3个小球序列帧\\"

num = 149
imageName = ""
for rt, dirs, files in os.walk(outfile):
    # num = len(files)
    f = files[int(num / 2)]
    imageName = os.path.splitext(f)[0]
    pos = imageName.rfind("_")
    imageName = imageName[:pos]

# num = int(num)
duration = int(duration)
# order = order == str(True)

xml = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<animation-list xmlns:android=\"http://schemas.android.com/apk/res/android\" android:oneshot=\"%s\">" % oneshot
n = num
while n >= 0:
    if order:
        i = num - n
    else:
        i = n

    if i < 10:
        xml = xml + "\n<item android:drawable=\"@mipmap/%s_%d\" android:duration=\"%d\" />" % (
        imageName, i, duration)
    else:
        xml = xml + "\n<item android:drawable=\"@mipmap/%s_%d\" android:duration=\"%d\" />" % (imageName, i, duration)
    n = n - 1
xml = xml + "\n</animation-list>"

print
xml
with open('%s/anim_matching_loading.xml' % outfile, 'w') as f:
    f.write(xml)
    print("XML写入完成")
