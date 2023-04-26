type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache = new Map()
    const result = Symbol()

    return function(...args) {
        let node = cache;

        for (const arg of args) {
            const nodeHasArgument = node.has(arg)

            if (!nodeHasArgument) {
                node.set(arg, new Map())
            }

            node = node.get(arg)
        }

        const hasCachedResult = node.has(result)

        if (!hasCachedResult) {
            node.set(result, fn(...args))
        }

        return node.get(result)
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
