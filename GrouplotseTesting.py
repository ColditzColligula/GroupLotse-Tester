import requests
import json
import PySimpleGUI as sg
import os
from huepy import *
import paho.mqtt.client as mqtt_client
import time
import random

sg.theme("LightBrown11")


# MQTT Essentials
broker = ''
port = 0
topic = ""
username = ''
password = ''
client_id = f'python-mqtt-{random.randint(0, 1000)}'


# broker = 'mqtt.grouplotse.com'
# port = 1883
# topic = "inc/19028414"
# username = '37386677'
# password = 'Xfbo1WfgRFe5'
# client_id = f'python-mqtt-{random.randint(0, 1000)}'

print(client_id)
print(broker)
print(port)
print(topic)
print(username)
print(password)

def connect_mqtt():
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
    return client


def publish(client, mqttmsg):
    result = client.publish(topic, mqttmsg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sending `{mqttmsg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def main():
    settingsfile = "grouplotse_tester_webhook.txt"
    isFile = os.path.isfile(settingsfile)


    if not isFile:
        with open("grouplotse_tester_webhook.txt", "w") as glsetwebhook:
            glsetwebhook.write("")
            glsetwebhook.close
        print(info(yellow("Layout Empty")))
        webhooklayout = [
            [sg.Text("Webhook_URL:"), sg.Push(), sg.Input("", key="-WEBHOOK-")],
            [sg.Text("Webhook_Key:"), sg.Push(), sg.Input("", key="-KEY-")],
            [sg.Text("Message:"), sg.Push(), sg.Input("", key="-MESSAGE-")],
            [sg.Button("Send"), sg.Button("Exit")],
        ]

    if isFile:
        with open("grouplotse_tester_webhook.txt", "r+") as glsetwebhook:
            fileread = glsetwebhook.read()
            if not fileread:
                pass
                webhooklayout = [
                    [sg.Text("Webhook_URL:"), sg.Push(), sg.Input("", key="-WEBHOOK-")],
                    [sg.Text("Webhook_Key:"), sg.Push(), sg.Input("", key="-KEY-")],
                    [sg.Text("Message:"), sg.Push(), sg.Input("", key="-MESSAGE-")],
                    [sg.Button("Send"), sg.Button("Exit")],
                ]
            else:
                split_list = fileread.split("#")
                webhook_split = split_list[0]
                webhook_key = split_list[1]
                print(info(yellow("Layout Filled")))
                webhooklayout = [
                    [sg.Text("Webhook_URL:"), sg.Push(), sg.Input(webhook_split, key="-WEBHOOK-")],
                    [sg.Text("Webhook_Key:"), sg.Push(), sg.Input(webhook_key, key="-KEY-")],
                    [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-MESSAGE-", size=(50, 6))],
                    [sg.Button("Send", key="-WEBHOOKSEND-"), sg.Button("Exit", key="-EXIT0-")],
                ]

    mqttlayout = [
        [sg.Text("Server URL:"), sg.Push(), sg.Input("mqtt.grouplotse.com", key="-MQTTBROKER-")],
        [sg.Text("Port:"), sg.Push(), sg.Input("1883", key="-MQTTPORT-")],
        [sg.Text("Topic:"), sg.Push(), sg.Input("inc/19028414", key="-MQTTTOPIC-")],
        [sg.Text("Username:"), sg.Push(), sg.Input("37386677", key="-MQTTUSERNAME-")],
        [sg.Text("Password:"), sg.Push(), sg.Input("Xfbo1WfgRFe5", key="-MQTTPASSWORD-")],
        [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-MQTTMESSAGE-", size=(50, 6))],
        [sg.Button("Send", key="-MQTTSEND-"), sg.Button("Exit", key="-EXIT1-")]
        ]

    #   Tab Group Layout (must contain ONLY tabs)
    tab_group_layout = [[sg.Tab('Webhook', webhooklayout, key='-TAB0-'),
                            sg.Tab('MQTT', mqttlayout, key='-TAB1-'),
                            ]]

    #   The window layout - defines the entire window
    layout = [[sg.Image("gl_logo_banner.png")],
              [sg.TabGroup(tab_group_layout,
                        enable_events=True,
                        key='-TABGROUP-')]]


    window = sg.Window("GroupLotse Buddy", layout)

    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "-EXIT0-" or event == "-EXIT1-"
        ):  # if user closes window or clicks cancel
            break

        if event == "-WEBHOOKSEND-":
            webhook = values["-WEBHOOK-"]
            key = values["-KEY-"]
            webhook_url = webhook + "?key=" + key
            data = values["-MESSAGE-"]
            webhook_post = requests.post(
                webhook_url,
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
            print(good(green(f'Sent "{data}" as POST Message to your Grouplotse')))
            with open("grouplotse_tester_webhook.txt", "w") as glsetwebhook:
                glsetwebhook.write(webhook + "#" + key)  # append data
                print(run(white(f"Saved {webhook}#{key} to list")))
                glsetwebhook.close()

        if event == "-MQTTSEND-":
            global broker, port, topic, username, password
            broker = values["-MQTTBROKER-"]
            port_string = values["-MQTTPORT-"]
            port = (int(port_string))
            topic = values["-MQTTTOPIC-"]
            username_unf = values["-MQTTUSERNAME-"]
            username = str(username_unf)
            password_unf = values["-MQTTPASSWORD-"]
            password = str(password_unf)
            mqttmsg = values["-MQTTMESSAGE-"]

            print(client_id)
            print(broker)
            print(port)
            print(topic)
            print(username)
            print(password)

            client = connect_mqtt()
            print(client)
            publish(client, mqttmsg)

    window.close()

if __name__ == "__main__":
    main()