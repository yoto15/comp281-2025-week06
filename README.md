# ไฟล์ประกอบการรียน
## วิชา COMP281 เทอม 1/2568
### Week06

### Python language programming
- Install python [Python download](https://www.python.org/downloads/)
- สร้าง Visual Environment
```
python -m venv cg-env
```
- activate Visual Environment ที่สร้าง
```
<path>/cg-env/Scripts/activate.bat
```
เมื่อทำแล้วจะมี (cg-env) ที่ Command Prompt

### Flask web application framework (WSGI : Web Server Gateway Interface)
### อ่านที่ [Flask](https://flask.palletsprojects.com/en/stable/)

- ติดตั้ง flask (web server library)
```
pip install flask python-dotenv
```
### flask template ใน Week06
```
flask
├──static
|	├──app.js
|	├──cg-module.js
|	└──demo.js
├──templates
|	├──demo.html
|	└──index.html
├──.env
└──app.py
```
- รัน flask app (ต้อง activate venv "cg-env" ก่อน)
```
cd <path>/flask/

# รันแบบ python ไฟล์ทั่วไป
python app.py

# รันแบบ flask command จะ auto load config/environment .env file
flash run
```
แล้วไปที่ Web Browser พิมพ์ http://127.0.0.1:5000

### เพิ่มเติมเรื่อง flask
- Flask เป็น Web application framework ของภาษา Python ใช้สำหรับทำเว็บแอปพลิเคชัน ที่มีความสามารถในการเป็น Web Server ในตัวเดียวกัน ทำให้สามารถเขียน frontend และ backend ได้ในตัวเดียวกัน และมีขนาดเล็ก ไม่ใช้ resourece มากนัก
- Flask มีรูปแบบการเขียนที่มีแบบแผนของตัวเอง ซึ่งเราเรียกว่า framework ถึงจะเป็นภาษา Python แต่ก็ต้องเขียนตามแบบแผนที่ถูกวางไว้
- Flask มีการใช้ Template Designer ของ [Jinja](https://jinja.palletsprojects.com/en/stable/) และมี [Template Designer Document](https://jinja.palletsprojects.com/en/stable/templates/) ให้อ่าน
```
พื้นฐาน delimiters ที่เขียนใน html ไฟล์
{{ อ่านตัวแปร/ข้อมูล }}
{% control flow %}
{# comment #}
```
- การเรียกใช้ template จะใช้ render_template() [Docs](https://flask.palletsprojects.com/en/stable/api/#template-rendering)
- หากเราใช้ .env เราต้องรันด้วยคำสั่ง flask run การทำงานจะใช้ package python-dotenv ในการ autoload .env แล้วอ่านค่า config ในนั้นไปใช้งาน สามารถอ่านได้ที่ [Configuration Handling](https://flask.palletsprojects.com/en/stable/config/)
