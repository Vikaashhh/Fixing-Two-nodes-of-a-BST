# 🛠️ Day 92 — GFG 160 Days DSA Challenge
### 🔄 Problem: Fixing Two Nodes of a BST
### 📋 Problem Statement:
In a given Binary Search Tree (BST), exactly two nodes have been swapped by mistake. The goal is to restore the BST without modifying its structure.

## 🧠 Core Approach:
🔹 Inorder Traversal — A valid BST’s inorder should yield a sorted sequence.
🔹 By identifying two anomalies in the sequence, we pinpoint the swapped nodes.
🔹 If nodes are non-adjacent → swap the first and last.
🔹 If adjacent → swap the first and middle.

This elegant approach ensures an in-place fix in O(n) time and O(h) space.

## 📊 Output Summary:
✅ Test Cases Passed: 200 / 200

⚡ Time Taken: 0.41 sec

🎯 Accuracy: 100%

🏆 Points Scored: 8 / 8

📈 Total Score: 357

## 🪄 Reflection:
“Even the most structured systems can go wrong — but with the right traversal, every disorder has a fix.” 🌱

## 🔖 Hashtags:
#gfg160 #geekstreak2025 #Day92
#DSA #BinarySearchTree #InorderTraversal
#CodingJourney #CleanCode #framesbyvikash #1001DaysOfCode
