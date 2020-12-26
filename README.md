# code_test_django

## Project Structure
``` 
code_test
-- code_test # project container
   -- __init__.py # this file implies that the directory is a package
   -- settings.py # the config file of django project
   -- urls.py # the router config file
   -- wsgi.py # access to a WSGI compatible web server to run your project
-- static # some static files
-- templates # some template files
-- weather # app
   -- conf # some config files for this app
      -- city.txt # the city config file
   -- migrations # db migrate file
   -- __init__.py # component files
   -- admin.py # django admin website config
   -- models.py # some models
   -- tests.py # some test cases
   -- views.py # some view functions
-- manage.py # command line tools
``` 

## Operation Instruction
```
# clone 代码
git clone https://github.com/dongjinnan/code_test_django.git

# 安装python3环境
# 安装django
# 进入code_test文件夹下，执行
python manage.py runserver 127.0.0.1:8000

# 浏览器访问http://127.0.0.1:8000/

# 城市的配置文件目录为：code_test_django\code_test\weather\conf\city.txt

# admin manage tool: http://127.0.0.1:8000/admin/
```