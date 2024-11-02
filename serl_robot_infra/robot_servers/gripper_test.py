import robotiq_gripper_server_direct

ip = "127.0.0.1"
port = 63352

def log_info(gripper):
    print(f"Pos: {str(gripper.get_current_position()): >3}  "
          f"Open: {gripper.is_open(): <2}  "
          f"Closed: {gripper.is_closed(): <2}  ")

print("Creating gripper...")
gripper = robotiq_gripper_server_direct.RobotiqGripper()
print("Connecting to gripper...")
gripper.connect(ip, port)
print("Activating gripper...")
gripper.activate()

print("Testing gripper...")
gripper.move_and_wait_for_pos(255, 255, 255)
log_info(gripper)
gripper.move_and_wait_for_pos(0, 255, 255)
log_info(gripper)