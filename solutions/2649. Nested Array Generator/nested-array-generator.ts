type MultidimensionalArray = (MultidimensionalArray | number)[]

function* inorderTraversal(arr: MultidimensionalArray): Generator<number, void, unknown> {
    if (!arr.length) {
        return;
    }

    const stack: MultidimensionalArray = [arr];
    while (stack.length > 0) {
        const curr = stack.pop();

        if (Array.isArray(curr)) {
            for (let i = curr.length - 1; i >= 0; i--) {
                stack.push(curr[i]);
            }
        } else {
            yield curr!;
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
