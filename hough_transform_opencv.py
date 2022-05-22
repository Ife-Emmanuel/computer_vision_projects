"""Explaination of the hough's transform in opencv."""
# Hough transform is a technique to detect any shape if you can represent that shape in a mathematical form.
# It can detect the shape even it is broken or distorted a little bit.

# consider a road, the thing you have to do first
# 1. you find the edge pixels using canny edge detection or any other edge detection method
# 2. Then find a geometrical representation of the edge. for example the slope or intercept

# 