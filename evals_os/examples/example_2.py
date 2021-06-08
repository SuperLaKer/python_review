import os

SIGTERM = 15


def pid_of(image):
    matching_proc_images = []
    # 迭代器
    for the_dir in [the_dir for the_dir in os.listdir('/proc') if the_dir.isdigit()]:
        lines = open('/proc/%s/status' % the_dir, 'r').readlines()
        for line in lines:
            if line.startswith('Name:'):
                name = line.split(':', 1)[1].strip()
                if name == image:
                    matching_proc_images.append(int(the_dir))

    return matching_proc_images


for pid in pid_of('tomcat'):
    os.kill(pid, SIGTERM)

if __name__ == '__main__':
    arr = [1, 2, 66, 8]
    for item in [item for item in arr if item < 10]:
        print(item)
