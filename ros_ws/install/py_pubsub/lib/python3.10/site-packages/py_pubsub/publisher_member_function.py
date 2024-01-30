import rclpy
from rclpy.node import Node
import os
from std_msgs.msg import String
import csv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        pass

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.data = []

        # Set up file change handler
        self.filepath = '/mnt/c/Users/TexSort/Desktop/MasterThesis/materialDetectionTextile/ros_ws/src/materialdetect/materialData.csv'
        self.event_handler = FileChangeHandler(self.read_file)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=os.path.dirname(self.filepath), recursive=False)
        self.observer.start()

        # Read the CSV file
        self.read_file()

    def read_file(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1]
            self.data = list(csv.reader([last_line]))

    def timer_callback(self):
        # Re-read the file every time, so we always get the newest data
        self.read_file()

        if self.data:
            msg = String()
            msg.data = ', '.join(self.data[0])
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    try:
        rclpy.spin(minimal_publisher)
    finally:
        minimal_publisher.observer.stop()
        minimal_publisher.observer.join()

    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()