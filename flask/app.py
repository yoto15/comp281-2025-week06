# flask คือ เว็บเฟรมเวิร์กที่ใช้สำหรับพัฒนาเว็บแอปพลิเคชันในภาษา Python
# Flask เป็นเฟรมเวิร์กที่มีขนาดเล็กและเรียบง่าย ทำให้เหมาะสำหรับการพัฒนาเว็บแอปพลิเคชันขนาดเล็กถึงกลาง
# มันมีคุณสมบัติที่ยืดหยุ่นและสามารถปรับแต่งได้ตามความต้องการของผู้พัฒนา
# Flask มีระบบ routing ที่ช่วยในการจัดการ URL และสามารถเชื่อมต่อกับฐานข้อมูลได้อย่างง่ายดาย
# นอกจากนี้ Flask ยังมีระบบ template engine ที่ช่วยในการสร้าง HTML templates ได้อย่างสะดวก
# render_template คือ ฟังก์ชันที่ใช้ในการเรนเดอร์เทมเพลต HTML ใน Flask
# มันจะรับชื่อไฟล์เทมเพลตและตัวแปรที่ต้องการส่งไปยังเทมเพลตนั้น ๆ
# โดยจะทำการแทนที่ตัวแปรในเทมเพลตด้วยค่าที่ส่งมา และส่งผลลัพธ์เป็น HTML กลับไปยังผู้ใช้
# request คือ อ็อบเจกต์ที่ใช้ในการจัดการคำขอ HTTP ใน Flask
# มันมีข้อมูลเกี่ยวกับคำขอที่เข้ามา เช่น URL, เมธอด (GET, POST), ข้อมูลที่ส่งมาในคำขอ (เช่น ฟอร์ม, JSON) และอื่น ๆ
# request สามารถใช้เพื่อดึงข้อมูลจากคำขอที่เข้ามาและทำการประมวลผลตามความต้องการของแอปพลิเคชัน
# jsonify คือ ฟังก์ชันที่ใช้ในการสร้าง JSON response ใน Flask
# มันจะรับข้อมูลที่ต้องการแปลงเป็น JSON และส่งกลับเป็น response ที่มี Content-Type เป็น application/json
# jsonify ใช้สำหรับการตอบสนองคำขอ HTTP ที่ต้องการข้อมูลในรูปแบบ JSON
from flask import Flask, render_template, request, jsonify
# os คือ โมดูลที่ใช้ในการจัดการกับระบบปฏิบัติการใน Python
# มันมีฟังก์ชันและตัวแปรที่ช่วยในการทำงานกับไฟล์และไดเรกทอรี เช่น การสร้าง, ลบ, ย้ายไฟล์, การเข้าถึงตัวแปรสภาพแวดล้อม, และอื่น ๆ
import os
# json, datetime
import json
import datetime

# new Flask application object
# __name__ คือ ตัวแปรที่เก็บชื่อของโมดูลปัจจุบัน
app = Flask(__name__)
# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads' # กำหนดโฟลเดอร์สำหรับอัปโหลดไฟล์
# os.makedirs คือ ฟังก์ชันที่ใช้ในการสร้างไดเรกทอรี (โฟลเดอร์) และไดเรกทอรีย่อย ๆ
# exist_ok=True คือ อาร์กิวเมนต์ที่ใช้เพื่อไม่ให้เกิดข้อผิดพลาดหากไดเรกทอรีนั้นมีอยู่แล้ว
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# กำหนดเส้นทาง (route) สำหรับแอปพลิเคชัน Flask ถ้ามาที่ / (root URL)
# ฟังก์ชัน index จะถูกเรียกเมื่อผู้ใช้เข้าถึง / URL หลักของแอปพลิเคชัน
@app.route('/')
def index():
	# อ่านไฟล์ index.html จากโฟลเดอร์ templates และส่งกลับไปยังผู้ใช้
	# ผ่านการใช้ render_template ฟังก์ชัน
	return render_template('index.html')

# กำหนดเส้นทาง (route) สำหรับแอปพลิเคชัน Flask ถ้ามาที่ /action methods=['POST'] คือการกำหนดให้รองรับเฉพาะคำขอ POST เท่านั้น
# ฟังก์ชัน action จะถูกเรียกเมื่อผู้ใช้ส่งคำขอ POST มาที่ /action
@app.route('/action', methods=['POST'])
def action():
	# ใช้ try-except เพื่อจัดการข้อผิดพลาดที่อาจเกิดขึ้นในระหว่างการประมวลผลคำขอ
	# ถ้ามีข้อผิดพลาดเกิดขึ้น จะส่งกลับข้อความแสดงข้อผิดพลาดและรหัสสถานะ HTTP 500 (Internal Server Error)
	# ถ้าไม่มีข้อผิดพลาด จะส่งกลับข้อมูล JSON ที่ระบุว่าข้อมูลได้รับการประมวลผลสำเร็จ
	# และแสดงข้อมูลที่ได้รับจากคำขอ POST
	try:
		# รับข้อมูล JSON จากคำขอ POST ที่ส่งมา
		# request.get_json() จะดึงข้อมูล JSON จากคำขอและแปลงเป็น Python dict
		# ถ้าไม่มีข้อมูล JSON จะส่งกลับ None
		data = request.get_json()
		if not data:
			# jsonify คือ ฟังก์ชันที่ใช้ในการสร้าง JSON response ใน Flask
			# ถ้าไม่มีข้อมูล JSON จะส่งกลับข้อความแสดงข้อผิดพลาด
			# และรหัสสถานะ HTTP 400 (Bad Request)
			return jsonify({'error': 'No data provided'}), 400

		# output คือ ตัวแปรที่เก็บข้อมูลที่จะส่งกลับไปยังผู้ใช้ รูปแบบนี้เรียกว่า dictionary คล้ายกับ JSON
		output = {
			'message': 'Data received successfully',
			'received_data': data['name']
		}

		# ส่งกลับข้อมูล JSON ที่เก็บในตัวแปร output
		# jsonify จะทำการแปลง output เป็น JSON และส่งกลับไปยังผู้ใช้
		# โดยไม่ต้องระบุ Content-Type เพราะ Flask จะจัดการให้โดยอัตโนมัติ
		return jsonify(output)
	except Exception as e: # exception handling
		# ถ้ามีข้อผิดพลาดเกิดขึ้นในระหว่างการประมวลผลคำขอ
		# จะจับข้อผิดพลาดนั้นและส่งกลับข้อความแสดงข้อผิดพลาด
		# พร้อมกับรหัสสถานะ HTTP 500 (Internal Server Error)
		# str(e) จะดึงข้อความของข้อผิดพลาดที่เกิดขึ้น
		return jsonify({'error': str(e)}), 500

# DEMO: กำหนดเส้นทาง (route) สำหรับแอปพลิเคชัน Flask ถ้ามาที่ /demo
@app.route('/demo')
def demo():
	# อ่านไฟล์ demo.html จากโฟลเดอร์ templates และส่งกลับไปยังผู้ใช้
	# ผ่านการใช้ render_template ฟังก์ชัน
	return render_template('demo.html')

# DEMO: กำหนดเส้นทาง (route) สำหรับแอปพลิเคชัน Flask ถ้ามาที่ /send methods=['POST'] คือการกำหนดให้รองรับเฉพาะคำขอ POST เท่านั้น
@app.route('/send', methods=['POST'])
def send():
	# ใช้ try-except เพื่อจัดการข้อผิดพลาดที่อาจเกิดขึ้นในระหว่างการประมวลผลคำขอ
	try:
		# รับข้อมูล JSON จากคำขอ POST ที่ส่งมา
		data = request.get_json()
		if not data:
			return jsonify({'error': 'No data provided'}), 400

		# บันทึก name, message เพิ่มลง logs.json
		filename = 'logs.json'
		# ถ้าไฟล์ logs.json ไม่มีอยู่ จะสร้างไฟล์ใหม่
		if not os.path.exists(filename):
			with open(filename, 'w') as f:
				json.dump([], f) # สร้างไฟล์ JSON ว่าง ๆ
		# อ่านข้อมูลจากไฟล์ logs.json
		with open(filename, 'r') as f:
			logs = json.load(f) # อ่านข้อมูล JSON จากไฟล์ เป็น Python list/dict
		
		# เพิ่มข้อมูลใหม่ลงใน logs
		logs.append({
			'timestamp': datetime.datetime.now().isoformat(),  # บันทึกเวลาปัจจุบัน
			'name': data.get('name', '---'),  # ถ้าไม่มี name จะใช้ 'Unknown'
			'message': data.get('message', '')  # ถ้าไม่มี message จะใช้ค่าว่าง
		})

		# เขียนข้อมูล logs กลับไปยังไฟล์ logs.json
		with open(filename, 'w') as f:
			json.dump(logs, f)

		# output คือ ตัวแปรที่เก็บข้อมูลที่จะส่งกลับไปยังผู้ใช้ รูปแบบนี้เรียกว่า dictionary คล้ายกับ JSON
		output = {
			'status': 'success',
			'logs': logs  # ส่งกลับข้อมูล logs ทั้งหมด
		}

		return jsonify(output)
	except Exception as e:
		# ถ้ามีข้อผิดพลาดเกิดขึ้นในระหว่างการประมวลผลคำขอ
		return jsonify({'error': str(e)}), 500

# DEMO: กำหนดเส้นทาง (route) สำหรับแอปพลิเคชัน Flask ถ้ามาที่ /logs
@app.route('/logs')
def logs():
	# อ่านไฟล์ logs.json และส่งกลับข้อมูลทั้งหมดในรูปแบบ JSON
	filename = 'logs.json'
	if not os.path.exists(filename):
		return jsonify({'error': 'Logs file not found'}), 404

	try:
		with open(filename, 'r') as f:
			logs = json.load(f)  # อ่านข้อมูล JSON จากไฟล์ เป็น Python list/dict
		# output คือ ตัวแปรที่เก็บข้อมูลที่จะส่งกลับไปยังผู้ใช้ รูปแบบนี้เรียกว่า dictionary คล้ายกับ JSON
		output = {
			'status': 'success',
			'logs': logs  # ส่งกลับข้อมูล logs ทั้งหมด
		}

		return jsonify(output)  # ส่งกลับข้อมูล logs ทั้งหมด
	except Exception as e:
		return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
# เช็คว่าโมดูลนี้ถูกเรียกใช้งานโดยตรงหรือไม่ ถ้าใช่ จะรันแอปพลิเคชัน Flask
# app.run() จะเริ่มต้นเซิร์ฟเวอร์ Flask และทำให้แอปพลิเคชันพร้อมรับคำขอ
# debug=True จะเปิดโหมดดีบัก ซึ่งจะช่วยในการพัฒนาและแก้ไขข้อผิดพลาด
if __name__ == '__main__':
	# Run the Flask application
	app.run(host="0.0.0.0", debug=True)