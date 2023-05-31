type Callback = (...args: any[]) => any;

type Subscription = {
  unsubscribe: () => void;
};

type Events = { [event: string]: Callback[] };

class EventEmitter {
  constructor(private events: Events = {}) {}

  subscribe(eventName: string, callback: Callback): Subscription {
    this.events[eventName] = this.events[eventName] ?? [];
    this.events[eventName].push(callback);

    return {
      unsubscribe: () => {
        this.events[eventName] = this.events[eventName].filter(
          (fn) => fn !== callback
        );

        if (this.events[eventName].length === 0) {
          delete this.events[eventName];
        }
      },
    };
  }

  emit(eventName: string, args: any[] = []): any {
    const output = [];

    for (const cb of this.events[eventName] ?? []) {
      output.push(cb(...args));
    }

    return output;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
