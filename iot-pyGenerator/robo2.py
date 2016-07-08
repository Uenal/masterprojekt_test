import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.100'))
channel = connection.channel()
channel.queue_declare(queue='friss_exch')

y = 90
while y < 260:
    channel.basic_publish(
        'friss_exch', 
        'f7636269-bef4-4aa0-aefb-36270a5d4f75', 
        json.dumps([
            {"time": "2016-01-18T18:00:04.120", "id": "f7636269-bef4-4aa0-aefb-36270a5d4f75", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": y, "rad":20, "rotation": 90, "color": ['#f5ff00','#ff0000']},
            {"time": "2016-01-18T18:00:04.120", "id": "f7636269-bef4-4aa0-aefb-36270a5d4f75", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": 70, "y": y, "rad":20, "rotation": 90, "color": ['#f5ff00','#ff0000']}
        ]),
        pika.BasicProperties(content_type="text/plain", delivery_mode=1)
    )
    
    channel.basic_publish(
        'friss_exch', 
        '4e2598d0-f597-4948-abbb-48ffd7b5c3f2', 
        json.dumps([
            {"time": "2016-01-18T18:00:04.120", "id": "4e2598d0-f597-4948-abbb-48ffd7b5c3f2", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 140, "y": y, "rad":20, "rotation": 90, "color": ['#f5ff00','#0a00ff']},
            {"time": "2016-01-18T18:00:04.120", "id": "4e2598d0-f597-4948-abbb-48ffd7b5c3f2", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo2", "x": 140, "y": y, "rad":20, "rotation": 90, "color": ['#f5ff00','#0a00ff']}
        ]),
        pika.BasicProperties(content_type="text/plain", delivery_mode=1)
    )
    
    y = y + 10
    time.sleep(0.2)
    
x = 70
while x < 250:
#    channel.basic_publish(
#        'friss_exch', 
#        'd3a8f31c-4ea8-4be8-ba64-129f4ebfec4f', 
#        json.dumps([
#            {"time": "2016-01-18T18:00:04.120", "id": "d3a8f31c-4ea8-4be8-ba64-129f4ebfec4f", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": x, "y": 260, "rad":20, "rotation": 0, "color": ['#f5ff00','#ff0000']},
#            {"time": "2016-01-18T18:00:04.120", "id": "d3a8f31c-4ea8-4be8-ba64-129f4ebfec4f", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": x, "y": 260, "rad":20, "rotation": 0, "color": ['#f5ff00','#ff0000']}
#        ]),
#        pika.BasicProperties(content_type="text/plain", delivery_mode=1)
#    )
    
    
#    channel.basic_publish(
#        'friss_exch', 
#        'a39beb37-25a3-4fda-b008-d093b582d18d', 
#        json.dumps([
#            {"time": "2016-01-18T18:00:04.120", "id": "a39beb37-25a3-4fda-b008-d093b582d18d", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": x, "y": 260, "rad":20, "rotation": 0, "color": ['#f5ff00','#ff0000']},
#            {"time": "2016-01-18T18:00:04.120", "id": "a39beb37-25a3-4fda-b008-d093b582d18d", "acceleration": [0, 0, 0], "location": "Europe/Berlin", "orientation": [0, 0, 0, 0], "name": "robo1", "x": x, "y": 260, "rad":20, "rotation": 0, "color": ['#f5ff00','#ff0000']}
#        ]),
#        pika.BasicProperties(content_type="text/plain", delivery_mode=1)
#    )
    
    x = x + 10
    time.sleep(0.2)
    
print(" [x] Sent 'Hello World!'")

connection.close()