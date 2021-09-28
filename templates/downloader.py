import urllib.request
import os
import shutil

lesson_dir = "blob:https://tfc.tv/15119a73-a31a-4479-bf20-f3e0553b2c0b"
try:
    shutil.rmtree(lesson_dir)
except:
    print("ok")

os.makedirs(lesson_dir)
os.chdir(lesson_dir)

for lesson, dwn_link in enumerate(my_lessons):
    print("downloading lesson  %d.. " % (lesson), dwn_link)
    file_name = '%04d.mp4' % lesson
    f = open(file_name, 'ab')
    for x in range(0, 1200):
        try:
            rsp = urllib.request.urlopen(dwn_link + "_%04d.ts" % (x) )
        except:
            break
        file_name = '%d.mp4' % lesson
        print("downloading  %d.ts" % (x))
        f.write(rsp.read())
    f.close()



print("done good luck!! ==================  ")