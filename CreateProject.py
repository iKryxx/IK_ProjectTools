import sys, time, os, zipfile, subprocess
name = sys.argv[1]
Include = sys.argv[2]

# argument check (empty ones are already checked in the bash script)
if(Include == "1" or Include == "0"):
    pass
else:
    print("incorrect usage of the -b Parameter. Please provide either 0 or 1")
    exit()
cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

#decompress
with zipfile.ZipFile(dir_path+"/Template/Template.zip","r") as zip_ref:
    zip_ref.extractall(cwd)
    os.rename(cwd + "/qwj1kwL5CPvBeVEzlVoQqRUnJyPAcDLP", cwd + "/" + name)
time.sleep(1)

#rename
with open(cwd + '/premake5.lua', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('qwj1kwL5CPvBeVEzlVoQqRUnJyPAcDLP', name)

with open(cwd + '/premake5.lua', 'w') as file:
  file.write(filedata)



if(Include == "1"):
    clone = subprocess.Popen(["git", "clone", "https://github.com/iKryxx/ik_lib"], stdout=subprocess.PIPE)
    clone.communicate()[0]
    move = subprocess.Popen(["mv", cwd+"/ik_lib/utils", "./"], stdout=subprocess.PIPE)
    move.communicate()[0]
    delete = subprocess.Popen(["rm", "-rf", cwd+"/ik_lib"], stdout=subprocess.PIPE)
    delete.communicate()[0]

#premake and make call come in the bash script after this



