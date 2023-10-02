# Lockboxes

## Problem Description

You have a collection of locked boxes, each numbered sequentially from 0 to n - 1. Each box may contain keys to other boxes, represented as a list of lists. You need to determine if all the boxes can be opened by following the given rules.

- A key with the same number as a box opens that box.
- The first box (boxes[0]) is unlocked.
- All keys are positive integers, and there can be keys that do not have corresponding boxes.

Write a method `canUnlockAll(boxes)` that determines if all the boxes can be opened.

## Function Signature

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
```

## Input

- `boxes` (List[List[int]]): A list of lists representing the boxes and their keys.

## Output

- Returns `True` if all boxes can be opened, else returns `False`.

## Example

```python
boxes1 = [[1], [2], [3], []]
canUnlockAll(boxes1)  # Returns True

boxes2 = [[1], [2, 3], [], [4]]
canUnlockAll(boxes2)  # Returns False
```

## Constraints

- The length of the list `boxes` will be at most 1000.
- Each list within `boxes` will contain at most 1000 elements.
- Each element in the list will be a positive integer or an empty list.
