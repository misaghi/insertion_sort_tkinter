class insertionSort:

    @staticmethod
    def insertion_sort(unsorted_list:list) -> list:
        steps = []
        steps.append(str(unsorted_list))
        for i in range(1, len(unsorted_list)):
            key = unsorted_list[i]
            j = i - 1
            while j > -1 and unsorted_list[j] > key:
                unsorted_list[j + 1] = unsorted_list[j]
                j -= 1
            # Every time after loop, steps will be updated.
            unsorted_list[j + 1] = key
            unsorted_list_str = list(unsorted_list)
            unsorted_list_str.insert(j + 1, '*')
            unsorted_list_str.insert(j + 3, '*')
            steps.append(str(unsorted_list_str))
    
        return steps