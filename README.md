# Q-Learning-Model
Flappy Bird Reinforcement Learning (Q-Learning & Beyond)
🚀 An RL-based Flappy Bird agent that learns to survive by optimizing its movements using Q-learning.
Currently trained using a Q-table, with plans to migrate to DQN for better scalability.

📌 Project Overview
This project uses Q-learning to train an agent to play Flappy Bird autonomously.
The goal is to make the model:
✅ Learn from past experiences
✅ Maximize long-term survival
✅ Handle difficult scenarios like extreme pillar gaps
✅ Improve training efficiency and scalability

Current Features
✅ Q-learning implementation with a lookup table
✅ Experience replay stored in XML
✅ Dynamic reward function based on survival and obstacle clearance

📊 Challenges & Setbacks
1️⃣ Incorrect State Proximity Calculation 🧩
🔴 Problem: The agent mistakenly learned from the farthest Q-value instead of the closest, leading to incorrect updates.
✅ Fix: Corrected the proximity function to select the nearest state.

2️⃣ Over-Penalizing Early Training Phases ⛔
🔴 Problem: The agent received 10x harsher punishment in early training, making it too risk-averse.
✅ Fix: Standardized reward scaling across all training phases.

3️⃣ Agent Struggled with Extreme Gaps 🎯
🔴 Problem: The agent performed well on small pillar variations but failed when gaps were drastically high/low.
✅ Fix: Improved state representation by adding bird velocity and increasing discount factor (γ) for better long-term planning.

🔜 Next Steps
🔹 Optimize training efficiency by introducing multi-threading.
🔹 Implement CUDA-based Q-table updates for faster training.
🔹 Migrate from Q-table to Deep Q-Networks (DQN) for scalability.
🔹 Improve generalization to handle unseen pillar variations better.

📝 Lessons Learned
✅ Reinforcement Learning requires deep debugging—mistakes often go unnoticed until training breaks down.
✅ Reward function tuning is critical—wrong scaling can ruin learning stability.
✅ Q-learning struggles with large state-action spaces, requiring optimization techniques like shared instances and function approximation.