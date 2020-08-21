"""
合并两个有序数组:

给你两个有序整数数组 nums1 和 nums2，
请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

"""

def merge_sort(nums1, nums2):
    m = []
    i, j = 0, 0
    while nums1 and nums2:
        #只比较每个数组的第一位就可以，每次将两者小的一个数弹出添加到新的列表中，直到有一个列表为空
        if nums1[i] <= nums2[j]:
            temp = nums1.pop(i)
            m.append(temp)
        else:
            temp = nums2.pop(j)
            m.append(temp)

    m = m + nums1 + nums2
    return m


if __name__ == '__main__':
    n1 = [1, 2, 3, 4, 4, 5, 8, 9]
    n2 = [2, 4, 5, 6, 7]
    m = merge_sort(n1, n2)
    print(m)
