import time
import os

def run_figlet_command():
    text_to_display = "bitcoin mining program..."
    image = "bitcoin.jpg"
    figlet_command = f"jp2a --height=28 {image} && figlet {text_to_display}"
    
    try:
        os.system(figlet_command)
    except Exception as e:
        print(f"Error executing figlet command: {e}")

def simulate_mining():
    for i in range(1, 99999):  # Simulate mining for 5 iterations
        print(f"Hackers who succeeded in hacking are happily mining. sweet, sweet~ {i}...")
        # Insert actual mining logic or visualization here
        time.sleep(0.5)  # Simulate mining time

if __name__ == "__main__":
    run_figlet_command()
    time.sleep(3)
    simulate_mining()
