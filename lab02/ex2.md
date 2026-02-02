1. Mention at least two aspects that make interpolation search better than binary search.

Binary search starts in the middle of the dataset while interpolation estimates the target's position based on its value relative to two data points. This makes it better than binary search for uniformly distributed data because it covers large portions of the array to converge on the element more efficiently, and it has a better time complexity (O(log(log(n))) compared to O(log(n)) for binary search).

2. Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?

Yes, the performance will be affected. This is because the interpolation search's time complexity will degrade to a time complexity similar to a linear search, which is O(n) in its worst case.

3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?

The line `pos = low + int(((float(high-low) / (arr[high] - arr[low])) * (x - arr[low])))` would be affected. This is a calculation of the expected position of the element using linear interpolation, which only works if the data is uniformly distributed. If we wanted it to follow a different distribution, we would need to modify this position calculation to accomodate for that.

4. When is linear search your only option for searching data as binary and interpolation search may fail?
If the dataset is unsorted, linear search will work while binary and interpolation will both fail, as they require data to be sorted in order to perform properly.

5. In which case will linear search outperform both binary and interpolation search, and why?
If the target is the first element in the dataset, linear search will outperform both binary and interpolation because it will find the element on its first check, while binary will start looking in the middle and interpolation will try to estimate its position. 

6. Is there a way to improve binary and interpolation search to solve this issue?

There are not many ways to improve binary and interpolations searches without changing the algorithm completely. However, the interpolation search could estimate lower in its position search so it has a better chance of catching the first element. This may not be ideal for all cases of using interpolation search. Since interpolation search and binary search are already much faster on average when compared to a linear search, the linear search outperforming both binary and interpolation searches would be in rarer cases.