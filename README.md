# reward-system
## Overview
This project simulates an automated collection and reward system for recyclable items. Users can add items, view the total rewards, and reset the system. The system accepts different types of recyclable items and calculates rewards based on the item type.

## How to Set Up and Run the Project
### Installation
1. **Clone the repository:**
   git clone https://github.com/harshit16-07/reward-system.git

 2.**Navigate into the cloned repository directory:**
    cd reward-system
    
3.**Run the script:**
    python reward_system.py
**Usage**
When you run the script, you will see the following options:
1. Add items to system
2. View total reward
3. Reset system
4. Exit

Choose an option by entering the corresponding number.

If you choose to add an item (option 1), you will be prompted to enter the item either A, B or C.

View the total reward accumulated by choosing option 2.

Reset the system for a new user session by choosing option 3.

Exit the program by choosing option 4.

### Code Structure
**reward_system.py**: The main script that contains the implementation of the Recyclable Reward System.

**RecyclableItem**: A class representing a recyclable item with a type and reward value.

**RewardSystem**: A class that manages the collection of items and calculation of total rewards.

**main()**: A function that provides a command-line interface for user interactions.

### Assumptions and Design Decisions
The system accepts three types of recyclable items: A, B, and C.

The reward values are predefined as follows:

Type A: INR 0.10

Type B: INR 0.05

Type C: INR 0.15

The item type input is case-insensitive (i.e., 'a', 'b', 'c' are treated the same as 'A', 'B', 'C').

The user interface is implemented as a command-line interface (CLI) for simplicity.

Invalid item types are handled gracefully by informing the user and not updating the reward.
   
