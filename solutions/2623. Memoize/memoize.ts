type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache = new Map();

    return function(...args) {
        const stringifiedArgs = JSON.stringify(args)

        if (cache.has(stringifiedArgs)) {
            return cache.get(stringifiedArgs)
        }

        const returnValue = fn(...args)
        cache.set(stringifiedArgs, returnValue)

        return returnValue
    }
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
