type Obj = Record<any, any>;

function compactObject(val: Obj): Obj | undefined {
  if (Array.isArray(val)) {
    let result: any[] = [];

    for (const subValue of val) {
      const sub: any = compactObject(subValue);

      if (Boolean(sub)) {
        result.push(sub);
      }
    }

    return result;
  }

  if (typeof val === 'object' && val !== null) {
    let result: Obj = {};

    for (const [key, subValue] of Object.entries(val)) {
      const sub = compactObject(subValue);

      if (Boolean(sub)) {
        result[key] = sub;
      }
    }

    return result
  }

  if (Boolean(val) === true) {
    return val
  }
};
