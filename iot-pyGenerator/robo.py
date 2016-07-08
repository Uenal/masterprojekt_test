import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.100'))
channel = connection.channel()
channel.queue_declare(queue='friss_exch')

channel.basic_publish(
    'friss_exch', 
    '146acbde-e555-48f1-83a3-e23b1ea618ce', 
    json.dumps([
        {"time": "2016-01-18T18:00:04.120", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 90, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.140", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 100, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.160", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 110, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.180", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 120, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.200", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 130, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.220", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 140, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.240", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 150, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.260", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": 160, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.280", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 72, "y": 170, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.300", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 74, "y": 180, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.320", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 76, "y": 190, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.340", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 78, "y": 200, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.360", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 80, "y": 210, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.380", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 82, "y": 220, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.400", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 84, "y": 230, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.420", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 86, "y": 240, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.440", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 88, "y": 250, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.460", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 90, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.480", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 95, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.500", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 100, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.520", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 110, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.540", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 120, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.560", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 130, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.580", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 140, "y": 260, "rad":20, "color": ['#f5ff00','#ff0000']},
        {"time": "2016-01-18T18:00:04.120", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 82, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.140", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 84, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.160", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 86, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.180", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 88, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.200", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 90, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.220", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 92, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.240", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 94, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.260", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 96, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.280", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 98, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.300", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 100, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.320", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 102, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.340", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 104, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.360", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 106, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.380", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 108, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.400", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 110, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.420", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 250, "y": 115, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.440", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 260, "y": 120, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.460", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 270, "y": 125, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.480", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 280, "y": 130, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.500", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 290, "y": 132, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.520", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 300, "y": 144, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.540", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 310, "y": 145, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.560", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 320, "y": 145, "rad":20, "color": ['#3fb80d','#1c25e1']},
        {"time": "2016-01-18T18:00:04.580", "id": "146acbde-e555-48f1-83a3-e23b1ea618ce", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 330, "y": 145, "rad":20, "color": ['#3fb80d','#1c25e1']}
    ]),
    pika.BasicProperties(content_type="text/plain", delivery_mode=1)
)

print(" [x] Sent 'Hello World!'")

connection.close()