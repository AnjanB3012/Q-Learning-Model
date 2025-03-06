# Q-Learning-Model
🐦 Reinforcement Learning for Flappy Bird (Q-Learning from Scratch)

🚀 Overview

This project implements a Q-learning agent to play Flappy Bird autonomously. The model learns to navigate obstacles, time jumps, and survive longer through reinforcement learning. Unlike prebuilt AI frameworks, this implementation is from scratch, focusing on manual Q-table updates and optimization.

💡 Features

-> Q-learning implementation with a lookup table.

-> Epsilon-greedy action selection for balanced exploration and exploitation.

-> Experience replay for improving training efficiency.

-> State proximity matching using Euclidean distance.

-> Separate Training and Testing modes for reliable evaluation.

📊 Challenges & Debugging Fixes

1. Fixed Incorrect Q-Value Selection in getMaxQinNodes()

Issue: The agent previously selected actions based on outcome labels instead of Q-values.
Fix: Now correctly selects the action with the highest Q-value.

2. Fixed Over-Reliance on Random Actions in Testing

Issue: The agent was randomly adding new states to the Q-table in test mode, causing unpredictable behavior.
Fix: Disabled random Q-table insertions in test mode, ensuring it only uses learned Q-values.

3. Balanced Exploration & Exploitation

Issue: High epsilon (ε) caused excessive randomness, preventing stable learning.
Fix: Implemented faster epsilon decay so the agent shifts to exploiting learned strategies sooner.

4. Prevented Over-Punishment for Falling

Issue: Overly strong penalties disrupted learning.
Fix: Adjusted reward scaling to maintain a stable learning rate.

5. Fixed Invalid State Lookups in findClosestState()

Issue: The function sometimes returned completely unrelated states, corrupting training.
Fix: Now ensures only valid states are used for lookups.

🚀 Next Steps

-> Optimize reward function for more efficient learning.

-> Train beyond 1,000+ epochs to enhance Q-value convergence.

-> Transition to Deep Q-Networks (DQN) for function approximation.

-> Experiment with different state representations for better generalization.

🔄 Last Updated: March 2025