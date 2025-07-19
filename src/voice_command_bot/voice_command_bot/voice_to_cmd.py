#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import speech_recognition as sr  # Library to recognize your voice

class VoiceCommandNode(Node):
    def __init__(self):
        super().__init__('voice_command_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('🎤 Voice Command Node Started')

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.listen_loop()

    def listen_loop(self):
        while rclpy.ok():
            with self.microphone as source:
                print("🎙️ Speak a command (e.g., 'go forward'):")
                self.recognizer.adjust_for_ambient_noise(source)
                print("🔧 Adjusted for ambient noise. Now listening...")
                audio = self.recognizer.listen(source)
                print("📥 Audio received. Trying to recognize...")

            try:
                command = self.recognizer.recognize_google(audio).lower()
                print(f"✅ You said: {command}")
                self.send_command(command)
            except sr.UnknownValueError:
                print("❌ Could not understand your voice")
            except sr.RequestError as e:
                print(f"⚠️ Could not reach the speech recognition service: {e}")


    def send_command(self, command):
        msg = Twist()

        if 'forward' in command:
            msg.linear.x = 0.2
        elif 'back' in command:
            msg.linear.x = -0.2
        elif 'left' in command:
            msg.angular.z = 0.5
        elif 'right' in command:
            msg.angular.z = -0.5
        elif 'stop' in command:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        else:
            print("⚠️ Unknown command")
            return

        self.publisher_.publish(msg)
        self.get_logger().info(f'🔊 Command sent: {command}')

def main(args=None):
    rclpy.init(args=args)
    node = VoiceCommandNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

