function curry(fn: Function): Function {
    return function curried(...args: any[]) {
        if (args.length >= fn.length) {
            return fn(...args);
        }

        return (...nextArgs: any[]) => curried(...args, ...nextArgs);
    };
};

/**
 * It's not possible to use generics in this leetcode problem,
 * because types of curried functions are not explicitly set.
 */

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */