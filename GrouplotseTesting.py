import PySimpleGUI as sg
import os
from huepy import *
from Grouplotse import Grouplotse
import webbrowser

sg.theme("LightBrown11")


def main():
    webhookfile = "grouplotse_tester_webhook.txt"
    iswebhookFile = os.path.isfile(webhookfile)

    mqttfile = "grouplotse_tester_mqtt.txt"
    ismqttFile= os.path.isfile(mqttfile)


    if not iswebhookFile:
        with open("grouplotse_tester_webhook.txt", "w") as glsetwebhook:
            glsetwebhook.write("")
            glsetwebhook.close
        print(info(yellow("Layout Empty")))
        webhooklayout = [
            [sg.Text("Webhook_URL:"), sg.Push(), sg.Input("", key="-WEBHOOK-")],
            [sg.Text("Webhook_Key:"), sg.Push(), sg.Input("", key="-KEY-")],
            [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-WHMESSAGE-", size=(50, 6))],
            [sg.Button("Send", key="-WEBHOOKSEND-"), sg.Button("Exit", key="-EXIT0-")],
        ]

    if iswebhookFile:
        with open("grouplotse_tester_webhook.txt", "r+") as glsetwebhook:
            fileread = glsetwebhook.read()
            if not fileread:
                pass
                webhooklayout = [
                    [sg.Text("Webhook_URL:"), sg.Push(), sg.Input("", key="-WEBHOOK-")],
                    [sg.Text("Webhook_Key:"), sg.Push(), sg.Input("", key="-KEY-")],
                    [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-WHMESSAGE-", size=(50, 6))],
                    [sg.Button("Send", key="-WEBHOOKSEND-"), sg.Button("Exit", key="-EXIT0-")],
                ]
            else:
                split_list = fileread.split("#")
                webhook_split = split_list[0]
                webhook_key = split_list[1]
                print(info(yellow("Layout Filled")))
                webhooklayout = [
                    [sg.Text("Webhook_URL:"), sg.Push(), sg.Input(webhook_split, key="-WEBHOOK-")],
                    [sg.Text("Webhook_Key:"), sg.Push(), sg.Input(webhook_key, key="-KEY-")],
                    [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-WHMESSAGE-", size=(50, 6))],
                    [sg.Button("Send", key="-WEBHOOKSEND-"), sg.Button("Exit", key="-EXIT0-")],
                ]







    if not ismqttFile:
        with open("grouplotse_tester_mqtt.txt", "w") as glsetmqtt:
            glsetmqtt.write("")
            glsetmqtt.close
        print(info(yellow("Layout Empty")))
        mqttlayout = [
            [sg.Text("Server URL:"), sg.Push(), sg.Input("http://mqtt.grouplotse.com", key="-MQTTBROKER-")],
            [sg.Text("Port:"), sg.Push(), sg.Input("1883", key="-MQTTPORT-")],
            [sg.Text("Topic:"), sg.Push(), sg.Input("", key="-MQTTTOPIC-")],
            [sg.Text("Username:"), sg.Push(), sg.Input("", key="-MQTTUSERNAME-")],
            [sg.Text("Password:"), sg.Push(), sg.Input("", key="-MQTTPASSWORD-")],
            [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-MQTTMESSAGE-", size=(50, 6))],
            [sg.Button("Send", key="-MQTTSEND-"), sg.Button("Exit", key="-EXIT1-")]
        ]

    if ismqttFile:
        with open("grouplotse_tester_mqtt.txt", "r+") as glsetmqtt:
            fileread = glsetmqtt.read()
            if not fileread:
                pass
                mqttlayout = [
                    [sg.Text("Server URL:"), sg.Push(), sg.Input("http://mqtt.grouplotse.com", key="-MQTTBROKER-")],
                    [sg.Text("Port:"), sg.Push(), sg.Input("1883", key="-MQTTPORT-")],
                    [sg.Text("Topic:"), sg.Push(), sg.Input("", key="-MQTTTOPIC-")],
                    [sg.Text("Username:"), sg.Push(), sg.Input("", key="-MQTTUSERNAME-")],
                    [sg.Text("Password:"), sg.Push(), sg.Input("", key="-MQTTPASSWORD-")],
                    [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-MQTTMESSAGE-", size=(50, 6))],
                    [sg.Button("Send", key="-MQTTSEND-"), sg.Button("Exit", key="-EXIT1-")]
                ]
            else:
                split_list = fileread.split("#")
                topic = split_list[2]
                username = split_list[3]
                password = split_list[4]
                print(info(yellow("Layout Filled")))
                mqttlayout = [
                    [sg.Text("Server URL:"), sg.Push(), sg.Input("mqtt.grouplotse.com", key="-MQTTBROKER-")],
                    [sg.Text("Port:"), sg.Push(), sg.Input("1883", key="-MQTTPORT-")],
                    [sg.Text("Topic:"), sg.Push(), sg.Input(topic, key="-MQTTTOPIC-")],
                    [sg.Text("Username:"), sg.Push(), sg.Input(username, key="-MQTTUSERNAME-")],
                    [sg.Text("Password:"), sg.Push(), sg.Input(password, key="-MQTTPASSWORD-")],
                    [sg.Text("Message:"), sg.Push(), sg.Multiline(key="-MQTTMESSAGE-", size=(50, 6))],
                    [sg.Button("Send", key="-MQTTSEND-"), sg.Button("Exit", key="-EXIT1-")]
                ]


    aboutlayout = [[sg.Multiline("GroupLotse is a virtual assistant that enables quick clarification of responsibilities\n"
                           " and precise device control. Your team can be actively involved in all decision-making\n"
                   " processes. Furthermore, it is also possible to fully automate all processes.\n"
                    "\n\nYour team can interact with GroupLotse via the common communication and collaboration\n"
                   " platforms Slack, Microsoft Teams and Telegram. This ensures that GroupLotse can be productively\n"
                   " integrated into workflows and that all relevant information is available at all times. To achieve\n"
                   " this, GroupLotse is simply integrated into your existing channels and chat groups.\n",
                            expand_y=True), sg.Button("", image_filename="gl_icon.png", key='-WEBSITEBUTTON-')]]


    #   Tab Group Layout (must contain ONLY tabs)
    tab_group_layout = [[sg.Tab('Webhook', webhooklayout, key='-TAB0-'),
                            sg.Tab('MQTT', mqttlayout, key='-TAB1-'),
                         sg.Tab('About', aboutlayout, key='-TABAB-')
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
            data = values["-WHMESSAGE-"]

            Grouplotse.webhook_post(Grouplotse, webhook, key, data)

            with open("grouplotse_tester_webhook.txt", "w") as glsetwebhook:
                glsetwebhook.write(webhook + "#" + key)  # append data
                print(run(white(f"Saved {webhook}#{key} to list")))
                glsetwebhook.close()

        if event == "-MQTTSEND-":
            broker = values["-MQTTBROKER-"]
            port_string = values["-MQTTPORT-"]
            port = (int(port_string))
            topic = values["-MQTTTOPIC-"]
            username_unf = values["-MQTTUSERNAME-"]
            username = str(username_unf)
            password_unf = values["-MQTTPASSWORD-"]
            password = str(password_unf)
            mqttmsg = values["-MQTTMESSAGE-"]

            Grouplotse.mqtt_send(Grouplotse, topic, username, password, mqttmsg)

            with open("grouplotse_tester_mqtt.txt", "w") as glsetmqtt:
                glsetmqtt.write("http://mqtt.grouplotse.com#1883"+"#"+topic+"#"+username+"#"+password)
                print(f"Saved {topic}#{username}#{password} to list")
                glsetmqtt.close()

        if event == "-WEBSITEBUTTON-":
            webbrowser.open("https://grouplotse.com/")


    window.close()

if __name__ == "__main__":
    main()