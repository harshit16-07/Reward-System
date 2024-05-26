
class RecyclableItem:
    def __init__(self, item_type):
        self.item_type = item_type.upper()  
        self.reward = self.get_reward(self.item_type)

    def get_reward(self, item_type):
        rewards = {'A': 0.10, 'B': 0.05, 'C': 0.15}
        return rewards.get(item_type, 0)


class RewardSystem:
    def __init__(self):
        self.items = []
        self.total_reward = 0.0

    def add_item(self, item):
        if item.reward > 0:
            self.items.append(item)
            self.total_reward += item.reward
            print(f"Item of type {item.item_type} added with reward {item.reward:.2f} INR.")
        else:
            print("Invalid item type. Please enter either A, B, or C.")

    def view_rewards(self):
        print(f"Total reward accumulated: {self.total_reward:.2f} INR")

    def reset_system(self):
        self.items = []
        self.total_reward = 0.0
        print("System reset for new user session.")



def main():
    reward_system = RewardSystem()

    while True:
        print("\nOptions:")
        print("1. Add items to system")
        print("2. View total reward")
        print("3. Reset system")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_type = input("Enter item (A, B, C): ").strip()
            item = RecyclableItem(item_type)
            reward_system.add_item(item)
        elif choice == '2':
            reward_system.view_rewards()
        elif choice == '3':
            reward_system.reset_system()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
