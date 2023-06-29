function sortBy(arr: any[], fn: Function): any[] {
    function swap(a: any, b: any) {
        return (fn(a) < fn(b)) ? -1 : 1
    }

    return arr.sort(swap);
};
