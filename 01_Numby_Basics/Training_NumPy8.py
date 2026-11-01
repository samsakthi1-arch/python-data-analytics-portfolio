import numpy as np


# Python list
python_list = [1, 2, 3, 4, 5]
print("Python list:", python_list)
print("Type:", type(python_list))



# NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])
print("NumPy array:", numpy_array)
print("Type:", type(numpy_array))

# Array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)


# Array of ones
ones = np.ones(5)
print("Ones:", ones)


# Range of numbers
range_arr = np.arange(0, 10, 2)  # Start, stop, step
print("Range:", range_arr)


# Evenly spaced numbers
spaced = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1
print("Spaced:", spaced)

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Matrix:")
print(matrix)
print("Shape:", matrix.shape)  # (rows, columns)image = np.array([[0, 128, 255],

image = np.array([[0, 128, 255],
                 [64, 128, 192],
                 [255, 128, 0]])
print("Tiny image:")
print(image)
print("Shape:", image.shape)  # 3 pixels tall, 3 pixels wide

numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
   result.append(num + 10)
print("Loop result:", result)


# NumPy - fast way
numbers = np.array([1, 2, 3, 4, 5])
result = numbers + 10
print("NumPy result:", result)

arr = np.array([1,2,3,4,5])

print("origina:", arr)
print("Add 10:", arr + 10)
print("Multiplay by 2:", arr*2)
print("Square:", arr**2)
print("Divide by 2:", arr/2) 

arr1=np.array([10,20,30,40,50,60,70,80,90,100])

arr2=np.array([1,2,3,4,5,6,7,8,9,10])

print("array 1:", arr1)
print("array 2:", arr2)
print("ADD:", arr1+arr2)
print("Divide arrays:", arr1/arr2)


# 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("1D array:", arr_1d)
print("Shape:", arr_1d.shape)  # (6,) means 6 elements


#2D array
arr_2D = np.array([[1,2,3],
                   [4,5,6]])

print("\n2D arry:")
print(arr_2D)
print("shape arr_2D:", arr_2D.shape)

#3D array
arr_3D = np.array([[[1,2],[3,4]],
                   [[5,6],[7,8]]])
print("\n3Darray:")
print(arr_3D)
print("shape arr_3D:", arr_3D.shape)


# Start with 12 numbers
arr = np.arange(12)
print("Original (12 numbers):", arr)
print("Shape:", arr.shape)


reshaped_3x4=arr.reshape(3,4)

print("\nreshaped 3x4:")
print(reshaped_3x4)
print("shape reshaped_3x4:", reshaped_3x4.shape)

# Reshape to 4 rows × 3 columns
reshaped_4x3 = arr.reshape(4, 3)
print("\nReshaped to 4×3:")
print(reshaped_4x3)
print("Shape:", reshaped_4x3.shape)

# Reshape to 2×2×3
reshaped_3d = arr.reshape(2, 2, 3)
print("\nReshaped to 2×2×3:")
print(reshaped_3d)
print("Shape:", reshaped_3d.shape)


# Image data often comes as flat array
flat_image = np.arange(9)  # 9 pixels
print("Flat pixels:", flat_image)


# Reshape to 3×3 image
image = flat_image.reshape(3, 3)
print("\nAs image (3×3):")
print(image)


# Flatten back
flattened = image.reshape(-1)  # -1 = auto-calculate
print("\nFlattened:", flattened)

import time

# Create large dataset
size = 1000000  # 1 million numbers

# Python list approach
python_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in python_list]
python_time = time.time() - start
print(f"Python list time: {python_time:.4f} seconds")


# NumPy approach
numpy_array = np.arange(size)
start = time.time()
result_numpy = numpy_array * 2
numpy_time = time.time() - start
print(f"NumPy time: {numpy_time:.4f} seconds")


# Calculate speedup
speedup = python_time / numpy_time
print(f"\nNumPy is {speedup:.0f}x faster!")

import sys

# Python list
python_list = list(range(1000))
list_size = sys.getsizeof(python_list)
print(f"Python list size: {list_size} bytes")


# NumPy array
numpy_array = np.arange(1000)
array_size = numpy_array.nbytes
print(f"NumPy array size: {array_size} bytes")


print(f"\nNumPy uses {list_size / array_size:.1f}x less memory")

arr = np.array([10, 20, 30, 40, 50, 60])


# Basic indexing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Third element:", arr[2])


# Slicing
print("First 3:", arr[:3])
print("Last 2:", arr[-2:])
print("Every other:", arr[::2])

#2d
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


print("Element at row 1, col 2:", matrix[1, 2])  # 6
print("First row:", matrix[0])
print("First column:", matrix[:, 0])
print("2×2 submatrix:")
print(matrix[:2, :2])

scores = np.array([85, 92, 78, 95, 88, 73, 90])


# Find high scores
high_scores = scores > 85
print("Scores > 85?:", high_scores)
print("High scores:", scores[high_scores])


# Find specific range
mid_range = (scores >= 80) & (scores <= 90)
print("Scores 80-90:", scores[mid_range])

data = np.array([23, 45, 67, 89, 34, 56, 78, 90, 12])


print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Std deviation:", np.std(data))
print("Median:", np.median(data))

matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


print("Total sum:", np.sum(matrix))
print("Sum each column:", np.sum(matrix, axis=0))
print("Sum each row:", np.sum(matrix, axis=1))

def create_sample_image():
   """Create a tiny 5×5 grayscale image"""
   # Random values 0-255 (grayscale)
   np.random.seed(42)  # For consistent results
   image = np.random.randint(0, 256, size=(5, 5))
   return image


def adjust_brightness(image, amount):
   """Adjust brightness by adding/subtracting value"""
   adjusted = image + amount
   # Clip to valid range 0-255
   adjusted = np.clip(adjusted, 0, 255)
   return adjusted


def adjust_contrast(image, factor):
   """Adjust contrast by multiplying"""
   adjusted = image * factor
   adjusted = np.clip(adjusted, 0, 255)
   return adjusted


# Create image
image = create_sample_image()
print("Original Image:")
print(image)
print(f"Brightness range: {np.min(image)} to {np.max(image)}")


# Brighten
brightened = adjust_brightness(image, 50)
print("\nBrightened (+50):")
print(brightened)
print(f"New range: {np.min(brightened)} to {np.max(brightened)}")


# Darken
darkened = adjust_brightness(image, -30)
print("\nDarkened (-30):")
print(darkened)


# Increase contrast
high_contrast = adjust_contrast(image, 1.5)
print("\nHigh Contrast (×1.5):")
print(high_contrast.astype(int))

def create_grade_data():
   """Simulate scores for 30 students, 5 exams"""
   np.random.seed(42)
   # Scores between 60-100
   scores = np.random.randint(60, 101, size=(30, 5))
   return scores


def analyze_grades(scores):
   """Comprehensive grade analysis"""
   print("=== Grade Analysis ===")
   print(f"Total students: {scores.shape[0]}")
   print(f"Total exams: {scores.shape[1]}")

   # Overall statistics
   print(f"\nClass average: {np.mean(scores):.1f}")
   print(f"Highest score: {np.max(scores)}")
   print(f"Lowest score: {np.min(scores)}")
   print(f"Standard deviation: {np.std(scores):.1f}")

   # Per-exam analysis
   exam_averages = np.mean(scores, axis=0)
   print(f"\nExam averages:")
   for i, avg in enumerate(exam_averages, 1):
       print(f"  Exam {i}: {avg:.1f}")

   # Per-student analysis
   student_averages = np.mean(scores, axis=1)
   print(f"\nTop 5 students (by average):")
   top_indices = np.argsort(student_averages)[-5:][::-1]
   for rank, idx in enumerate(top_indices, 1):
       print(f"  {rank}. Student {idx+1}: {student_averages[idx]:.1f}")

   # Grade distribution
   a_students = np.sum(student_averages >= 90)
   b_students = np.sum((student_averages >= 80) & (student_averages < 90))
   c_students = np.sum((student_averages >= 70) & (student_averages < 80))

   print(f"\nGrade Distribution:")
   print(f"  A (90+): {a_students} students")
   print(f"  B (80-89): {b_students} students")
   print(f"  C (70-79): {c_students} students")

   # Students who need help
   struggling = student_averages < 70
   if np.any(struggling):
       print(f"\nStudents needing support: {np.sum(struggling)}")
       print(f"  IDs: {np.where(struggling)[0] + 1}")


# Run analysis
scores = create_grade_data()
print("Sample scores (first 5 students):")
print(scores[:5])
print()