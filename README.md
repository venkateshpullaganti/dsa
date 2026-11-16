# DSA notes

Files and folders are numbered in the order the topics were studied, so a top-to-bottom listing is the revision order.

## Naming rules

1. **Prefix every topic file and folder with a two-digit number and an underscore**: `NN_name`, e.g. `08_stacks.py`, `18_koko_eating_bananas.py`.
2. **Always zero-pad** (`01`, `02`, … `09`, `10`). Without the zero, `10_` sorts before `2_`.
3. **The number is the order of study**, not difficulty or importance. A new item takes the next free number in its folder.
4. **Never renumber existing items.** Append at the end, even if the new problem logically belongs earlier.
5. **Names stay in `snake_case`** after the prefix.
6. **Each folder has its own sequence starting at `01`.** The root sequence covers topics; a topic folder's sequence covers the problems inside it.
7. **One topic, one slot.** Use a single file (`04_sorting.py`) while a topic is small; use a folder (`07_binary_search/`) when it has one file per problem.

## Adding something new

- New problem in an existing topic: look at the highest number in that folder and use the next one.

  ```
  07_binary_search/18_<problem_name>.py
  ```

- New topic: take the next root number (currently `08`).

  ```
  08_<topic>.py        # single file
  08_<topic>/          # folder, with 01_<problem>.py inside
  ```

- New markdown note: next number in `notes/`.

## Renaming or moving

Use `git mv` so history follows the file:

```
git mv old_name.py 08_old_name.py
```

Rename only; do not change file contents in the same commit.

## Not numbered

- `demo.py`, `input.txt`, `output.txt`: scratch files for the VS Code run task.
- `notes/`: supporting notes; the folder is unnumbered, the files inside are numbered.
- Images and other attachments inside topic folders (e.g. the PNGs in `06_hashing/`).

## Current order

```
01_patterns.py
02_basic_maths.py
03_recursion.py
04_sorting.py
05_arrays.py
06_hashing/
07_binary_search/
notes/
```

`06_hashing/` holds both the early basics (studied between recursion and sorting) and the later problems (studied after arrays); it sits at the position of the later work.
