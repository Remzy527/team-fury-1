
name="francis onwukwe"
id = "03944"
email ="francisohis@gmail.com"
language = "python"

data = "Hello World,this is {} with  HNGi7 ID HNG-{} and email {} using {} for stage 2 task".format(name,id,email,language)
json_output = json.dumps(data,indent=1)
print(json_output)