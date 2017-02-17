"""
  Library for making MQTT remote method calls.

  The purpose of the  MqttClient class is to allow one computer to call a method on an object
  that lives on another computer.  So if your PC wanted to call the arm_up method on an
  instance of your robot, it could!  Example:

  # Assuming imports like these
  import mqtt_remote_method_calls as com
  import robot_controller as robo

  Code running on the EV3:
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

  Code running on the PC:
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    ...(some time later, perhaps when a button is clicked)...
    mqtt_client.send_message("arm_up")

  In this example the PC is connecting to the MQTT broker and only planning to publish
    messages, so the MqttClient constructor is called with no delegate parameter set.
    The EV3 however expects to be subscribing to messages so an object must be given to
    the MqttClient constructor.  That robot object on the EV3 will be the object that is
    called when the PC sends messages.  When the PC sends a message to call the "arm_up"
    method then the EV3 runs the code robot.arm_up() and the arm goes up.

  If the PC instead called a method like this...
    mqtt_client.send_message("drive_time", [600, 1.5])

    then the EV3 would call the method robot.drive_time(600, 1.5)
    It is the responsibility of the developer to implement the method being called. There
    is no magic drive_time method in the Snatch3r class unless you implement it.

  Limitations:
    This communication protocol is only meant for simple methods. It has various limitations.
    - Parameters passed must be simple variable types such as int, str, float
    - The method called should not return anything (it won't get magically passed back)


  Also note that messages can go the other way too. For example:

  Code running on the PC:
    class MyDelegate(object):
        def print_hello(self):
            print("Hello, World!")

        def print_double(self, x):
            print("Double {} is {}.".format(x, 2 * x))

        def print_sum(self, x, y, z):
            print("The sum is", x + y + z)

    pc_delegate = MyDelegate()
    mqtt_client = com.MqttClient(pc_delegate)
    mqtt_client.connect_to_ev3()


  Code running on the EV3:
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    ...(some time later, perhaps sent every second)...
    mqtt_client.send_message("print_hello")
    mqtt_client.send_message("print_sum", [3, 4, 5])
    mqtt_client.send_message("print_double", [4])

  This is, of course, a silly contrived example but the EV3 would make the computer print:
    Hello, World!
    The sum is 12
    Double 4 is 8.

  Notice that when passing only 1 parameter it still had to be a list.

  And finally we'll mention that on the EV3 the object passed in to the MqttClient does NOT have
  to be the robot object.  The most common development pattern for larger project is to use a
  DIFFERENT object (not the robot object) as the delegate for MQTT callback.  For example:

  Code running on the EV3:
    class MyDelegate(object):
        def __init__(self):
            self.robot = robo.Snatch3r()
            self.mqtt_client = None # To be set later.

        def arm_up(self):
            print("Arm up")
            self.robot.arm_up()

        def something_else(self):
            print("Do something interesting")
            m1.do_task1(self.robot, self.mqtt_client)

        def loop_forever(self):
            btn = ev3.Button()
            while not btn.backspace:
                // do stuff
                time.sleep(0.01)
            if self.mqtt_client:
                self.mqtt_client.close()
            self.robot.shutdown()

    def main():
        my_delegate = MyDelegate()
        mqtt_client = com.MqttClient(my_delegate)
        my_delegate.mqtt_client = mqtt_client
        mqtt_client.connect_to_pc()
        my_delegate.loop_forever()
        print("Shutdown complete.")

    main()


  Code running on the PC:
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    ...(some time later, perhaps when a button is clicked)...
    mqtt_client.send_message("arm_up")
    mqtt_client.send_message("something_else")

"""

import json

import collections
import paho.mqtt.client as mqtt

LEGO_NUMBER = 99  # TODO: Set your LEGO_NUMBER


class MqttClient(object):
    """Helper class to make it easier to work with MQTT subscriptions and publications."""

    def __init__(self, delegate=None):
        self.client = mqtt.Client()
        self.delegate = delegate
        self.subscription_topic_name = None
        self.publish_topic_name = None

    def connect_to_ev3(self, mqtt_broker_ip_address="mosquitto.csse.rose-hulman.edu", lego_robot_number=LEGO_NUMBER):
        """ Code running on the PC should use this command to connect to the EV3 robot.
            Connects to the MQTT broker and begins listening for messages from the EV3. """
        self.connect("msg4pc", "msg4ev3", mqtt_broker_ip_address, lego_robot_number)

    def connect_to_pc(self, mqtt_broker_ip_address="mosquitto.csse.rose-hulman.edu", lego_robot_number=LEGO_NUMBER):
        """ Code running on the EV3 should use this command to connect to the student PC.
            Connects to the MQTT broker and begins listening for messages from the PC. """
        self.connect("msg4ev3", "msg4pc", mqtt_broker_ip_address, lego_robot_number)

    def connect(self, subscription_suffix, publish_suffix,
                mqtt_broker_ip_address="mosquitto.csse.rose-hulman.edu", lego_robot_number=LEGO_NUMBER):
        lego_name = "lego" + str(lego_robot_number).zfill(2)
        self.subscription_topic_name = lego_name + "/" + subscription_suffix
        self.publish_topic_name = lego_name + "/" + publish_suffix

        # Callback for when the connection to the broker is complete.
        self.client.on_connect = self._on_connect
        self.client.message_callback_add(self.subscription_topic_name, self._on_message)

        self.client.connect(mqtt_broker_ip_address, 1883, 60)
        print("Connecting to mqtt broker {}".format(mqtt_broker_ip_address), end="")
        self.client.loop_start()

    def send_message(self, function_name, parameter_list=None):
        message_dict = {"type": function_name}
        if parameter_list:
            if isinstance(parameter_list, collections.Iterable):
                message_dict["payload"] = parameter_list
            else:
                # Attempt to bail out users that pass a single item that was a non-list.
                # CONSIDER: Make this a feature and print no message. Just make it work.
                print("The parameter_list {} is not a list. Converting it to a list for you.".format(parameter_list))
                message_dict["payload"] = [parameter_list]
        message = json.dumps(message_dict)
        self.client.publish(self.publish_topic_name, message)

    # noinspection PyUnusedLocal
    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(" ... Connected!")
        else:
            print(" ... Error!!!")
            exit()

        print("Publishing to topic:", self.publish_topic_name)
        self.client.on_subscribe = self._on_subscribe

        # Subscribe to topic(s)
        self.client.subscribe(self.subscription_topic_name)

    # noinspection PyUnusedLocal
    def _on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed to topic:", self.subscription_topic_name)

    # noinspection PyUnusedLocal
    def _on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        # print("Received message:", message)
        if not self.delegate:
            print("Missing a delegate")
            return

        # Attempt to parse the message and call the appropriate function.
        try:
            message_dict = json.loads(message)
        except ValueError:
            print("Unable to decode the received message as JSON")
            return

        if "type" not in message_dict:
            print("Received a messages without a 'type' parameter.")
            return
        message_type = message_dict["type"]
        if hasattr(self.delegate, message_type):
            method_to_call = getattr(self.delegate, message_type)
            # Assumes that the user has the parameters correct.
            if "payload" in message_dict:
                message_payload = message_dict["payload"]
                attempted_return = method_to_call(*message_payload)
            else:
                attempted_return = method_to_call()
            if attempted_return:
                print("The method {} returned a value. That's not really how this library works." +
                      "The value {} was not magically sent back over".format(message_type, attempted_return))
        else:
            print("Attempt to call method {} which was not found.".format(message_type))

    def close(self):
        self.delegate = None
        self.client.loop_stop()
        self.client.disconnect()
