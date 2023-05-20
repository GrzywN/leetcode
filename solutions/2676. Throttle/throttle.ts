type F = (...args: any[]) => void

function throttle(fn: F, t: number): F {
  let shouldWait = false;
  let waitingArgs: any[] | null;

  const timeoutFn = () => {
    if (waitingArgs == null) {
      shouldWait = false;
    } else {
      fn(...waitingArgs)
      waitingArgs = null;
      setTimeout(timeoutFn, t)
    }
  };

  return function (...args) {
    if (shouldWait) {
      waitingArgs = args;
      return
    }

    fn(...args);
    shouldWait = true;

    setTimeout(timeoutFn, t)
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
