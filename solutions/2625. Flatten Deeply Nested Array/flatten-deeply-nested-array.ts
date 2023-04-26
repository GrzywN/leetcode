type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    return flatten(arr, n, 0, [])
};

function flatten(arr: MultiDimensionalArray, maxDepth: number, currentDepth: number, flattenedArray: MultiDimensionalArray): MultiDimensionalArray {
    if (currentDepth == maxDepth) {
        flattenedArray.push(...arr)

        return flattenedArray
    }

    for (const item of arr) {
        const isItemAnArray = Array.isArray(item)

        if (isItemAnArray) {
            flatten(item, maxDepth, currentDepth + 1, flattenedArray)
        } else {
            flattenedArray.push(item)
        }
    }

    return flattenedArray
}
