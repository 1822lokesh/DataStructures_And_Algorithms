#  🔎 Linear Search

Linear Search is a simple searching algorithm that checks each element in the list one by one until the target element is found or the list ends.

### Steps
1. Start from the first element.
2. Compare with the target.
3. If found, return the index.
4. If not found, return -1.

### Time Complexity
- Best Case: O(1)
- Worst Case: O(n)
- Average Case: O(n)
- Space Complexity: O(1)

### Example
Array: [10, 20, 30, 40, 50]  
Target: 30  
Output: Element found at index 2


Code: [linear_search.py](./linear_search.py)


## 🔎 Binary Search

Binary Search is a searching algorithm that works on **sorted arrays** (ascending or descending).  

Instead of checking elements one by one (like Linear Search), it **divides the search space in half** at each step.  
This makes it much faster than Linear Search.  

---

### ⚙️ How it Works (Step-by-Step)

Suppose we want to search for `30` in this sorted array:  

[10, 20, 30, 40, 50]


1. Start with **low = 0** and **high = n-1** → (0, 4).  
2. Find the **mid index**:  


mid = (low + high) // 2

→ (0+4)//2 = 2  
3. Check `arr[mid]`:  
- If `arr[mid] == target`, return index.  
- If `arr[mid] > target`, search the **left half**.  
- If `arr[mid] < target`, search the **right half**.  
4. Repeat until `low > high` (means element not found).  

👉 In our case:  
`mid = 2` → `arr[2] = 30` → ✅ Found at index **2**.  

---

### ⏱ Time Complexity

- **Best Case:** O(1) → target is the middle element.  
- **Worst Case:** O(log n) → keep dividing until one element left.  
- **Average Case:** O(log n)  
- **Space Complexity:**  
- Iterative → O(1)  
- Recursive → O(log n) (stack calls)  

👉 Code: [binary_search.py](./binary_search.py)

---

## 📂 Summary
- **Linear Search** → works on any list, but slow for large data.  
- **Binary Search** → requires a sorted list, but much faster (logarithmic time).  