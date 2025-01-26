#!/usr/bin/env python
# coding: utf-8

# # Basic matrix operations in `numpy`
# 
# **Learning goal:** By the end of this lesson, you will be familiar with the `numpy` library, `numpy` arrays, and some basic array manipulation tasks.
# 
# An important part of your data training relies on having a good understanding of how you can manipulate data structures and perform mathematical operations with them. We have already seen Python's native data structures (sets, lists, tuples, dictionaries), but today we will guide you through another one that is very convenient in a lot of use cases. This new structure is the **`array`**. This one is not supported out-of-the-box and requires using an external **library** called `numpy` (short for "numeric Python"); however, this line is trivial to **import**. You just have to run this line:

# In[1]:


import numpy as np


# We've just imported the `numpy` library and assigned an **alias** (in this case, `np`) to it. Thanks to this alias, whenever we need to call a `numpy` function, we don't have to type `numpy.some_function()`, but we can use `np.some_function()`instead. `numpy` and its associated libraries are extremely popular in data science and are used by many data practitioners around the world every day.

# ## Creating arrays
# 
# In many ways, `numpy` arrays are like Python lists. The main advantages of using arrays over lists are improved performance and an easier syntax when doing mathematical operations that involve several of them.
# 
# This is how you create an array of integers in `numpy`:

# In[2]:


np.array([1,2,3,4], dtype=np.int64)


# And this is how you create it specifying the data type as floating point (decimal numbers) instead of integers:

# In[3]:


np.array([1,2,3,4], dtype=np.float64)


# You can see that the first array stored the elements as integers, while the second one stored them as decimal numbers. Here's an array of text elements:

# In[4]:


np.array(["Once", "in", "a", "blue", "moon"], dtype=str)


# And this is one of boolean elements:

# In[5]:


np.array([True, False, False, False, True], dtype=bool)


# ### Exercise 1
# 
# Create this array:
# $$
# \begin{bmatrix}
# 25.7521 & 45.11112 & 50
# \end{bmatrix}
# $$

# **Answer.**

# In[6]:


np.array([25.7521, 45.11112, 50])


# You can paste multiple arrays together to make a single combined array that can be thought of as a table with rows and columns. For instance, take a look at these three arrays:

# In[7]:


np.array([99, 112, 44], dtype=np.float64)
np.array([7.89, 1.74, 22.3], dtype=np.float64)
np.array([9.879, 4.71, 3.22], dtype=np.float64)


# They could be made into a table like this:

# In[8]:


table = np.array([
    [99, 112, 44],
    [7.89, 1.74, 22.3],
    [9.879, 4.71, 3.22]
])
table


# You can take a look at the shape of this array by accessing the **`.shape`** attribute:

# In[9]:


table.shape


# This output means that `table` has three elements in each of its three sub-arrays.

# ### Exercise 2
# 
# Create this array:
# 
# $$
# \begin{bmatrix}
# 1 & 2 & 3 & 4 \\
# 5 & 6 & 7 & 8 \\
# 9 & 10 & 11 & 12 \\
# \end{bmatrix}
# $$

# **Answer.**

# In[12]:


np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])


# ### Exercise 3
# 
# Create this array:
# 
# $$
# \begin{bmatrix}
# [1 & 4] & [7 & 10] \\
# [3 & 6] & [9 & 12] \\
# \end{bmatrix}
# $$

# **Answer.**

# In[24]:


np.array([
    [[1,4], [7,10]],
    [[3,6],[9,12]]
])


# To access elements from an array, index it as you would a nested list:

# In[25]:


table


# In[26]:


table[0]


# In[27]:


table[1]


# In[28]:


table[1][2]


# ## Matrix arithmetic
# 
# You can do math on arrays just like with "normal" numbers. From here on in, we'll refer to arrays as **matrices**, which are 2-dimensional representations of arrays (with rows and columns).
# 
# ### Matrix addition and subtraction
# 
# Let $A$ and $B$ be two matrices such that
# 
# $$
# A = \begin{bmatrix}
# 1 & 2 & 3 \\
# 10 & 20 & 30
# \end{bmatrix}
# $$
# 
# and
# 
# $$
# B = \begin{bmatrix}
# 4 & 8 & 16 \\
# 3 & 9 & 27
# \end{bmatrix}
# $$
# 
# Two matrices must have the same shape in order to be added together. Their sum would be equal to the sum of each element in $A$ with the element that is exactly in the same location (same indexes) in $B$:
# 
# $$
# A + B = \begin{bmatrix}
# 1+4 & 2+8 & 3+16 \\
# 10+3 & 20+9 & 30+27
# \end{bmatrix} = \begin{bmatrix}
# 5 & 10 & 19 \\
# 13 & 29 & 57
# \end{bmatrix}
# $$
# 
# Adding two matrices in `numpy` is easy:

# In[29]:


A = np.array([
    [1,2,3],
    [10,20,30]
])

B = np.array([
    [4,8,16],
    [3,9,27]
])

A + B


# Doing this same addition using just Python lists would have required us to write [some complicated for loops](https://www.geeksforgeeks.org/python-program-add-two-matrices/). We love tools that make our lives easier, and `numpy` arrays do exactly that.

# ### Exercise 4
# 
# Can you guess how to subtract $B$ from $A$ in `numpy`?

# **Answer**.

# In[31]:


B-A


# ### Scalar multiplication
# 
# You can multiply a matrix and a real number together (this real number is referred to as a **scalar**). For instance,
# 
# $$
# A = \begin{bmatrix}
# 1 & 2 & 3 \\
# 10 & 20 & 30
# \end{bmatrix}
# $$
# 
# if multiplied by $5$ would yield
# 
# $$
# 5 \cdot A = \begin{bmatrix}
# 5 \times 1 & 5 \times 2 & 5 \times 3 \\
# 5 \times 10 & 5 \times 20 & 5 \times 30
# \end{bmatrix}= \begin{bmatrix}
# 5 & 10 & 15 \\
# 50 & 100 & 150
# \end{bmatrix}
# $$
# 

# ### Exercise 5
# 
# Can you guess how to get $5 \cdot A$ in `numpy`?

# **Answer**.

# In[32]:


5*A


# This is how intuitive `numpy` syntax is!

# ### Linear combinations
# 
# You can **linearly combine** two matrices by using matrix addition *and* scalar multiplication at the same time. Mathematically, this is the formula for a linear combination of $A$ and $B$:
# 
# $$\alpha \cdot A + (1 - \alpha) \cdot B$$
# 
# where $\alpha$ is a scalar.
# 
# This can be a little bit difficult to visualize using only matrices with numbers. Let's use a pair of images instead, taking advantage of the fact that 2D images are simply matrices in which each element tells you the color of the corresponding pixel.
# 
# Let's first import a library that we need in order to import the images into Jupyter and display them inline:

# In[33]:


from PIL import Image # The library is PIL. We import a module from that library. The module is Image.


# And now let's load two images:

# In[34]:


A = Image.open("data/images/macaw.jpg", "r") # "r" stands for "read"
B = Image.open("data/images/tigers.jpg", "r")


# This is image `A`:

# In[35]:


A


# And this is image `B`:

# In[36]:


B


# Now let's convert both images to `numpy` arrays and inspect their shapes.

# In[37]:


A_array = np.asarray(A)
B_array = np.asarray(B)
A_array


# ### Question
# 
# Why do you think each element in this array has three integers inside?
# 
# 
# **Answer.** Pixels are made up of three colors: Red, Green, and Blue (the RGB standard). Therefore, each element in the array (each pixel) has one number for red, one number for green, and one number for blue. It is the combination of these three primary colors which creates all the colors we see on our screens.
# 
# Now let's view the shapes of the arrays:

# In[38]:


print(A_array.shape)
print(B_array.shape)


# Both images are 250 x 250 pixels in size and have three color channels (RGB).

# ### Exercise 6
# 
# Create a function that takes two matrices and one scalar as arguments and outputs the linear combination of the matrices. Call it `linear_combination`.
# 
# **Note:** We will be plotting the linear combinations that this function will generate. For technical reasons related to how images are handled under the hood, Python requires that the result of `linear_combinations` is of an `np.uint8` data type. To convert an array `a` into this data type you simply run `a = a.astype(np.uint8)`.

# In[48]:


def linear_combination(m1, m2, s):
    linear_combinations = m1*s + m2*s
    return linear_combinations.astype(np.uint8)


# Let's now linearly combine `A_array` and `B_array` using $\alpha=0.5$:

# In[49]:


lin_AB_array = linear_combination(A_array, B_array, 0.5)
lin_AB_array


# Let's now visualize the result:

# In[50]:


Image.fromarray(
    lin_AB_array
)


# So you can see that a linear combination does actually combine both matrices. It has combined our macaw and our tiger in a single image! And even better, you can control the amount of each image that will end up in the mixed version. This one, for instance, used $\alpha=0.5$, which means that both images were mixed in equal parts.

# ### Exercise 7
# 
# Calculate and display the linear combination of the photos with:
# 
# * $\alpha = 0$
# * $\alpha = 1$
# * $\alpha = 0.25$
# * $\alpha = 0.75$

# **Answer.**

# In[51]:


lin_AB_array = linear_combination(A_array, B_array, 0)
Image.fromarray(
    lin_AB_array
)


# In[52]:


lin_AB_array = linear_combination(A_array, B_array, 1)
Image.fromarray(
    lin_AB_array
)


# In[53]:


lin_AB_array = linear_combination(A_array, B_array, 0.25)
Image.fromarray(
    lin_AB_array
)


# In[54]:


lin_AB_array = linear_combination(A_array, B_array, 0.75)
Image.fromarray(
    lin_AB_array
)


# This is great. Now you know how filmmakers create fade-ins and fade-outs! They simply linearly vary the amount of each image in each successive frame using the parameter $\alpha$.

# You can *slice* these arrays as well. To slice an array, you use a syntax similar to the one you use when you slice a list. You use positional indexes between brackets, like this: `my_array[6]`. Since `numpy` is zero-indexed, this example would get you the item that is in the seventh position of the array `my_array`. If you have nested arrays, you can do multiple indexing like this: `my_array[6][3]`. This code would get you the fourth element of the seventh sub-array of `my_array`.
# 
# Additionally, you can use `:` to tell `numpy` to return all the elements in an array. Thus, `my_array[:]` is the same as `my_array`, and `my_array[6][:]` is the same as `my_array[6]`. This shortcut becomes more useful when you need to access all the <i>n</i>-th elements of all the sub-arrays. For instance, `my_array[:, 4]` will get you *all* the fifth elements of *all* the sub-arrays of `A`. Notice that this is *different* from `my_array[:][4]`, which first retrieves all the elements of `my_array` and then *only* the fifth element of the result.
# 
# To slice using ranges of positions, you use `my_array[start_range:end_range]`, and so `my_array[3:7]` would retrieve the elements of `my_array` that are between those positions.
# 
# Let's slice our photos:

# In[55]:


Image.fromarray(
    A_array[50:100, :] # Slice vertically, show all pixels horizontally
)


# In[56]:


Image.fromarray(
    A_array[: ,50:100] # Show all pixels vertically, then slice horizontally
)


# In[57]:


Image.fromarray(
    A_array[:][50:100]
)


# ### Exercise 8
# 
# Slice the tiger photo to crop it to 200 x 200 pixels (you need to remove 25 pixels from each border).

# **Answer.** One possible answer is below:

# In[64]:


Image.fromarray(
    B_array[200:][:200]
)


# ### Other useful operations
# 
# We can extract just the red component of an image by doing some clever slicing (here, the reddest parts of the image are shown as the brightest - since we got rid of the G and B channels, we're not in the RGB standard anymore and therefore Python interprets this as a greyscale image):

# In[65]:


Image.fromarray(
    # The first ":" means "Take all the pixels from the first dimension (height)"
    # The second ":" means: "Take all the pixels from the second dimension (width)"
    # The 0 means "Take only the red channel (the first color value - index 0)"
    # Try with 1 (green) or 2 (blue) instead and see what happens
    A_array[:, :, 0]
)


# We can also add random noise using `numpy`'s random number generation function **`np.random.rand()`** and matrix addition. `np.random.rand()` produces a random float number between 0 and 1:

# In[66]:


random_noise = np.random.rand(250,250,3)  # 250 x 250 pixels, 3 color channels
random_noise = random_noise * 255 # Multiply the noise matrix by a scalar to make the noise more noticeable

A_noisy = A_array + random_noise # This is matrix addition!
A_noisy = A_noisy.astype(np.uint8) # Converting to the required data type

Image.fromarray(
        A_noisy
)


# It looks like the random noise image you would see on television channels that you didn't have access to as a kid!

# ### Exercise 9
# 
# Adapt the code from the previous cell to create a function that adds noise to an image in proportion to some user-defined scalar. Call it `add_random_noise`.

# **Answer.**

# In[67]:


def add_random_noise(image_array, random_noise):
    noisy = image_array + random_noise
    noisy = noisy.astype(np.uint8)
    return noisy


# Now we can parametrize our noise addition:

# In[68]:


Image.fromarray(
        add_random_noise(A_array, 100) # Try with different values!
)


# **Note:** A common application of `numpy` is random number generation between two integers. You can use this code to generate a random number between 4 and 15, for instance:

# In[69]:


np.random.randint(4,15) # Run this cell several times to see how the output changes at random


# In the RGB standard, `(0,0,0)` is the color black, and `(255,255,255)` is the color white. All the other colors are created by varying the channel values within those limits. For instance, we can create arrays of black images by telling numpy to generate a matrix with all its values set to zero. For this we use **`np.full()`**:

# In[70]:


black = np.full(shape=(250,250,3), fill_value=0)
black = black.astype(np.uint8)

Image.fromarray(
        black
)


# Blue is `(0,0,255)`. We can create and display a blue square of 250 x 250 pixels by first creating a black square and then replacing its blue channel with the integer `255`:

# In[71]:


blue = black.copy()
blue[:, :, 2] = 255
blue


# In[72]:


Image.fromarray(
        blue
)


# ### Exercise 10
# 
# Create a red square and linearly combine it with the blue square we've just created. Use $\alpha=0.3$ and $\alpha=0.6$.
# 
# **Hint:** Red in the RGB standard is `(255,0,0)`.
# 

# In[73]:


red = black.copy()
red[:,:,0] = 255
red


# In[76]:


Image.fromarray(
    linear_combination(red, blue, 0.3)
)


# In[77]:


Image.fromarray(
    linear_combination(red, blue, 0.6)
)


# ## Appendix
# 
# This is a summary of the operations we covered in this case.
# 
# * **Creating arrays**: `np.array(list_or_lists_of_elements, dtype=a_dtype)`. There are [several data types in `numpy`](https://numpy.org/devdocs/user/basics.types.html), but the ones we used here were `np.int64`, `np.float64`, `np.uint8`, `str`, and `boolean`.
# * **Matrix addition**: `A + B`, where `A` and `B` are `numpy` arrays.
# * **Matrix subtraction**: `A - B`, where `A` and `B` are `numpy` arrays.
# * **Multiplication of a scalar and a matrix**: `r * A`, where `r` is a real number (a scalar), and `A` is a `numpy` array.
# * **Converting an image to a `numpy` array**: `np.asarray(I)` where `I` is a [Pillow image object](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open).
# * **Showing the shape of a `numpy` array**. `A.shape` where `A` is a `numpy` array. Remember that the shape of an array is the number of elements it has in each one of its sub-arrays.
# * **Slicing a `numpy` array:** For the most part, it is just like slicing lists, with the added benefit of being able to use the `:` operator to retrieve all the elements in a subset of the array. For more information, you can find a tutorial [here](https://www.w3schools.com/python/numpy_array_slicing.asp).
# * **Converting an array to another data type**: `A.astype(data_type)`, where `A` is a `numpy` array.
# * **Creating an array of random numbers between 0 and 1:** `np.random.rand(shape)`. For instance, `np.random.rand(250,250,3)` will create a matrix of 250 x 250 in which element is itself an array that has 3 elements.
# * **Generating a random integer between two integers:** `np.random.randint(lower_boundary,upper_boundary)`.
# * **Creating a matrix and filling it with a given number:** `np.full(shape, fill_value)`. For instance, `np.full(shape=(25,25), fill_value=0)` will create a 25x25 array full of zeroes.
# * **Creating a copy of an array:** `A.copy()` where `A` is a `numpy` array.
# 
# 
# There are lots of applications of matrices, and `numpy` offers a treasure trove of functions to make them possible. Image processing is just one of those applications. We encourage you to learn more about `numpy` in its [documentation](https://numpy.org/doc/stable/user/quickstart.html).

# ## Attribution
# 
# *Ara macao - Scarlet Ara*. Quartl. October 9, 2011. Creative Commons Attribution-Share Alike 3.0 Unported license. https://commons.wikimedia.org/wiki/File:Ara_macao_qtl1.jpg
# 
# *The two female cubs of T-19 in a playful mood at Ranthambore tiger reserve*. Vedang Vadalkar. June 18, 2015. Creative Commons Attribution-Share Alike 4.0 International license. https://commons.wikimedia.org/wiki/File:Flying_Princess_(cropped).jpg
