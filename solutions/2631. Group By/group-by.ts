declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    const output = {};

    for (const item of this) {
        const key = fn(item);

        if (key in output) {
            output[key].push(item);
        } else {
            output[key] = [item];
        }
    }

    return output;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
