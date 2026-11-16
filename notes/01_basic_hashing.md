# Basics of Hashing

**Core Intuition:** Hashing is a technique used to store and retrieve data in the fastest way possible ($O(1)$ on average). It involves "pre-storing" values in a data structure so you can "fetch" them instantly later.


### 1. The Brute Force Problem
* **Scenario:** Given an array, find how many times a number $X$ appears.
* **Naive Approach:** Iterate through the entire array for every query.
* **Complexity:** If there are $Q$ queries and the array size is $N$, the time complexity is $O(Q \times N)$. If $Q$ and $N$ are $10^5$, this results in $10^{10}$ operations, which exceeds the typical 1-second time limit (~$10^8$ operations).

### 2. Array Hashing (Number Hashing)
Instead of searching, we use an index-based array to store frequencies.
* **The Mechanism:**
    1. Create a `hash` array of size `max_element + 1`, initialized to 0.
    2. Iterate through the input array once: `hash[array[i]]++`.
    3. To answer a query for number $X$, simply return `hash[X]`.
* **Constraints:** * Inside `main()`, you can declare an array up to $\approx 10^6$.
    * Globally, you can declare up to $\approx 10^7$.
    * For numbers larger than $10^7$ (e.g., $10^9$), array hashing fails due to memory limits.

### 3. Character Hashing
Characters are mapped to array indices using their **ASCII values**.
* **Lower Case ('a'-'z'):** Use an array of size 26. Index = `character - 'a'`.
* **All Characters:** Use an array of size 256. The character itself acts as the index (auto-casted to its ASCII integer).


### 4. Hashing using STL Maps (C++)
When numbers are too large for arrays, use `std::map` or `std::unordered_map`.

| Feature | `std::map` | `std::unordered_map` |
| :--- | :--- | :--- |
| **Storage** | Sorted Order | Unordered |
| **Time Complexity** | $O(\log N)$ (All cases) | $O(1)$ (Avg/Best), $O(N)$ (Worst) |
| **Internal Implementation** | Red-Black Tree | Hash Table |
| **Key Types** | Almost any (Pairs, Vectors, etc.) | Individual types (Int, String, etc.) |

### 5. Collisions & Division Method
* **Division Method:** Map a large number to a smaller index using modulo: `index = number % array_size`.
* **Linear Chaining:** If two different numbers result in the same index (e.g., $18 \% 10 = 8$ and $28 \% 10 = 8$), they are stored in a "chain" (usually a linked list) at that index.
* **Collision:** When multiple keys map to the same hash index. This is why `unordered_map` can occasionally hit $O(N)$ complexity in the worst-case scenario.


### Pro Tip
* **Interview Strategy:** Always start with `unordered_map` because it is $O(1)$ on average. If you encounter a "Time Limit Exceeded" (TLE) due to a specific test case designed to trigger collisions (the $O(N)$ worst case), switch to a regular `map`.
* **Memory Optimization:** Maps only store the elements that actually appear in the input, whereas array hashing requires space for every potential index up to the maximum element.