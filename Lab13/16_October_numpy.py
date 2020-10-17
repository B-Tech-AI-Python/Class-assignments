import numpy as np

# %%
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,6,7,8,9])

arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(f"{arr1[4]} - {arr2[0]} = {arr1[4]-arr2[0]}")

print()
print("2nd elemnt of first dim:",arr3[0,1])
print("Last elemnt of third dim:",arr3[2,-1])

arr4 = np.ndarray(shape=(1,2), dtype=int)

print("\nShape:",arr4.shape)
print("Size:",arr4.size)
print("Data type:",arr4.dtype)
print("Dimensions:",arr4.ndim)

x = np.array([[1,2],
              [3,4],
              [5,6]])
y = x[[0,1,2],
      [0,1,1]]

print(f"\n{y}")
