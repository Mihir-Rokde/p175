import matplotlib .pyplot as plt
import psutil as p
app_name_dict={}
count=0
for process in p.process_iter():
    count=count+1
    if count <=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name : ",name,"--cpu_usage : ",cpu_usage)
        app_name_dict.update({name:cpu_usage})
keymax=max(app_name_dict,key=app_name_dict.get)
print(keymax)
keymin=min(app_name_dict,key=app_name_dict.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)

app=app_name_dict.values()
max_app=max(app)
print(max_app)
min_app=min(app)
print(min_app)
mm_list=[max_app,min_app]
print(mm_list)
plt.figure(figsize=(15,7))
plt.xlabel("mm_cpu_consumption")
plt.ylabel("usage")
plt.bar(name_list,mm_list,width=0.6,color=("blue","red","green","orange","yellow","pink"))
plt.show()
        
