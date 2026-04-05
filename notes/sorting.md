# 1. Selection Sort
**Core Intuition:** "Select the minimum and swap." You repeatedly find the smallest element from the unsorted part and place it at the beginning.

### Strategic Breakdown
* **The Mechanism:**
    1. Find the minimum element in the range `[i...n-1]`.
    2. Swap that minimum with the element at index `i`.
    3. Increment `i` and repeat until the array is sorted.
* **The "Aha!" Moment:** After every iteration `i`, the first `i+1` elements are sorted and will never be touched again.

### Complexity Analysis
* **Time Complexity:** $O(n^2)$ for Best, Average, and Worst cases. The inner loop always runs to find the minimum.
* **Space Complexity:** $O(1)$ (In-place sorting).

### Pro Tip
* **Stability:** Selection sort is **not stable** by default. It can change the relative order of equal elements because it performs long-distance swaps.
* **Loop Logic:** The outer loop only needs to run up to `n-2`. When the second-to-last element is placed, the last one is automatically sorted.

---

# 2. Bubble Sort
**Core Intuition:** "Push the maximum to the last." Repeatedly swap adjacent elements if they are in the wrong order.

### Strategic Breakdown
* **The Mechanism:**
    1. Compare adjacent elements `(j, j+1)`.
    2. If `arr[j] > arr[j+1]`, swap them.
    3. After one full pass, the largest element "bubbles up" to the last position.
    4. Repeat for the remaining unsorted portion.
* **Optimization:** Use a `didSwap` flag. If no swaps occur during a pass, the array is already sorted—**break early**.

### Complexity Analysis
* **Worst/Average Time:** $O(n^2)$ (Array is reverse sorted).
* **Best Time (Optimized):** $O(n)$ (Array is already sorted). **Crucial for interviews.**
* **Space Complexity:** $O(1)$.

### Pro Tip
* **Optimization is Key:** Always mention the `didSwap` flag optimization. It shows you care about the "Best Case" scenario and constant-time improvements.
* **Stability:** Bubble Sort is **stable** because it only swaps if an element is strictly greater, preserving the relative order of equal values.

---

# Insertion Sort: Comprehensive Notes

Insertion sort is an intuitive sorting algorithm that builds a sorted array one element at a time. It is particularly efficient for small data sets or arrays that are already partially sorted.



## 1. How it Works (The Logic)
The algorithm conceptually maintains a **sorted** and an **unsorted** partition within the same array. It takes one element from the unsorted side and "drifts" it to its correct position in the sorted side.

* **Starting Point:** The first element (`index 0`) is always considered sorted by itself [00:31:57].
* **The Process:**
    1.  Pick the next element (let's call it the "target").
    2.  Compare the target with the element to its left.
    3.  If the left element is larger, **swap** them [00:33:13].
    4.  Continue swapping to the left until the target finds an element smaller than itself or reaches the start of the array [00:34:35].
    5.  Repeat until the end of the array is reached.

## 2. Dry Run Example
**Initial Array:** `[14, 9, 15, 12, 6]`

* **Iteration 1:** `14` is sorted.
* **Iteration 2 (Target 9):** Compare `9` and `14`. Swap. 
    * Result: `[9, 14, 15, 12, 6]` [00:32:19]
* **Iteration 3 (Target 15):** Compare `15` and `14`. $15 > 14$, so no swap.
    * Result: `[9, 14, 15, 12, 6]` [00:32:43]
* **Iteration 4 (Target 12):** * `12` vs `15` $\rightarrow$ Swap.
    * `12` vs `14` $\rightarrow$ Swap.
    * `12` vs `9` $\rightarrow$ Stop.
    * Result: `[9, 12, 14, 15, 6]` [00:32:49]
* **Iteration 5 (Target 6):** `6` swaps with `15`, `14`, `12`, and `9` until it reaches the front.
    * Final Result: `[6, 9, 12, 14, 15]` [00:34:35]

## 3. Code Implementation
This implementation uses a nested loop structure. The outer loop selects the element, and the inner `while` loop handles the shifting logic [00:36:48].

```cpp
void insertion_sort(int arr[], int n) {
    // Outer loop runs from 0 to n-1
    for (int i = 0; i <= n - 1; i++) {
        int j = i;
        
        // Inner loop: swap with the left neighbor 
        // as long as the left neighbor is greater
        while (j > 0 && arr[j - 1] > arr[j]) {
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            
            // Move index to the left to keep comparing
            j--; 
        }
    }
}