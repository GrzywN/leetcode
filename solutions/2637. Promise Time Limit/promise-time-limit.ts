type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
	return async function(...args) {
        const timeLimitedFunction = fn(...args);

        const timer = new Promise((_, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)
        })

        return Promise.race([timeLimitedFunction, timer])
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
