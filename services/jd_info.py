'''import os,time,re




localtime = time.localtime(time.time())

time_str =  time.strftime("%Y-%m-%d",localtime)

docker_log_path = '/var/lib/docker/containers/'
jd_usr = os.listdir(docker_log_path)




def get_jd():
    co_list = []
    for i in jd_usr:
        temp_str = ''
        with open(docker_log_path + i + os.sep + i +'-json.log') as f:
            f = f.readlines()
            for line in range(len(f)):
                if (time_str in f[line]) and ("[jd_bean_change.js]" in f[line]) and ('【账号1🆔】' in f[line]):
                    count = 1
                    while count:
                        try:
                            fnss = f[line-1+count]
                        except:
                            break
                        temp_str += re.findall('jd_bean_change.js]: (.+?)stream',f[line-1+count])[0].replace(' ','')[:-5] + '\n'
                        if '【京东红包】' in f[line+count+-1]:
                            break
                        count += 1
                    co_list.append(temp_str)
    return co_list'''
