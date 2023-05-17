type F = () => Promise<any>;

function promisePool(functions: F[], n: number): Promise<any> {
  function evaluateNext() {
    if (functions.length === 0) return;

    const fn = functions.shift();
    return fn().then(() => evaluateNext());
  }

  const nPromises = Array(n).fill(0).map(evaluateNext);
  return Promise.all(nPromises);
}

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
