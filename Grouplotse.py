import paho.mqtt.client as mqtt_client
import random
import requests
import json

class Grouplotse:
    #attributes#methods
    def webhook_file_post(self, webhook_addr, webhook_key, filepath, file_extension):
        """Main Function to send images via Webhook.
        webhook_addr is the URL of your Webhook. webhook_key is the Key.
        Next, specify the file and pass the file extension."""
        try:
            payload = {}
            files = [
                ('file', (f'data{file_extension}', open(f'{filepath}', 'rb')))
            ]
            headers = {
                'Authorization': webhook_key,
            }
            requests.post(webhook_addr, headers=headers, data=payload, files=files)
            print(f'Sending "{filepath}" as POST Message to your Grouplotse')
        except:
            raise Exception("Failed to send message. Key or Webhook Address might be incorrect or your GroupLotse isn't"
                            "configured correctly!")


    def webhook_post(self, webhook_addr, webhook_key, webhook_msg):
        """Main function to send Text via Webhook.
        webhook_addr is the URL of your Webhook. webhook_key is the Key.
        Pass a String to webhook_msg and call the method."""
        webhook_lotse = (webhook_addr+"?key="+webhook_key)

        try:
             requests.post(webhook_lotse, data=json.dumps(webhook_msg), headers={'Content-Type': 'application/json'})
             print(f'Sending "{webhook_msg}" as POST Message to your Grouplotse')
        except:
            raise Exception("Failed to send message. Key or Webhook Address might be incorrect or your GroupLotse isn't"
                            "configured correctly!")


    def mqtt_send(self, topic, username, password, mqttmsg):
        """Main function to send Text message via MQTT.
        The client_id and broker are set to the standard for Grouplotse. Make sure you pass
        the right topic, username and password - followed by your String for 'mqttmsg' and call
        the method to send."""
        client_id = f'python-mqtt-{random.randint(0, 1000)}'
        broker = "mqtt.grouplotse.com"
        port = 1883
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)


        # Set Connecting Client ID
        client = mqtt_client.Client(client_id)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        result = client.publish(topic, mqttmsg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sending {mqttmsg} to topic {topic}")
        else:
            print(f"Failed to send message to topic {topic}")