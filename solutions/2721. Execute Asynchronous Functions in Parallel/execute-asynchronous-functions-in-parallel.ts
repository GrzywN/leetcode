async function promiseAll<T>(functions: (() => Promise<T>)[]): Promise<T[]> {
    return new Promise<T[]>(async (resolve, reject) => {
        if (functions.length === 0) {
            resolve([]);
            return;
        }

        const results: T[] = new Array(functions.length).fill(null);

        let resolvedCount = 0;

        for (let i = 0; i < functions.length; i++) {
            const fn = functions[i];

            fn()
                .then((subResult) => {
                    results[i] = subResult;
                    resolvedCount++;
                    if (resolvedCount === functions.length) {
                        resolve(results);
                    }
                })
                .catch((err) => {
                    reject(err);
                });
        }
    });
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
