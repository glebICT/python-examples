def make_robot(name):
    count = 0  # the robot's secret counter

    def introduce():
        print(f"Hi, I am {name}!")

    def next_number():
        nonlocal count
        count += 1
        return count

    def status():
        print(f"{name}'s current number is {count}.")

    return {
        "introduce": introduce,
        "next": next_number,
        "status": status,
    }


robot_a = make_robot("WALL-E")
robot_b = make_robot("EVE")

robot_a["introduce"]()      
robot_a["next"]()           
robot_a["next"]()           
robot_a["status"]()         

robot_b["introduce"]()
robot_b["next"]()
robot_b["status"]()
