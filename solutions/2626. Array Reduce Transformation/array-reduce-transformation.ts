type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let curr = init;

    for (const num of nums) {
        curr = fn(curr, num);
    }

    return curr;
};
