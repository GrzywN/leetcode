type Key = number;
type Value = number;
type Duration = number;
type Timeout = ReturnType<typeof setInterval>;
type Expired = boolean;

type CacheMap = Map<Key, [Value, Duration, Timeout, Expired]>;

class TimeLimitedCache {
  private cache: CacheMap;

  constructor() {
    this.cache = new Map();
  }

  set(key: number, value: number, duration: number): boolean {
    const entry = this.cache.get(key);
    const doesExist = entry != null;

    const currTimeout = setTimeout(() => {
      const entry = this.cache.get(key)!;

      let updatedEntry = new Array(4) as [Value, Duration, Timeout, Expired];
      updatedEntry.push(...entry);
      updatedEntry[3] = true;

      this.cache.set(key, updatedEntry);
    }, duration);

    let unexpiredKeyExists = false;

    if (doesExist) {
      const expired = entry[3];
      unexpiredKeyExists = !expired;

      const prevTimeout = entry[2];
      clearTimeout(prevTimeout);
    }

    this.cache.set(key, [value, duration, currTimeout, false]);
    return unexpiredKeyExists;
  }

  get(key: number): number {
    const entry = this.cache.get(key);

    if (entry == null) {
      return -1;
    }

    const value = entry[0];
    const expired = entry[3];

    return expired ? -1 : value;
  }

  count(): number {
    let counter = 0;

    this.cache.forEach((tuple) => {
      const unexpired = !tuple[3];

      if (unexpired) counter++;
    });

    return counter;
  }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
