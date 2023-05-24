function jsonToMatrix(arr: any[]): (string | number | boolean | null)[][] {
  const keySet: Set<string> = new Set<string>();

  for (const curr of arr) {
    const keys = getKeys(curr);
    for (const k of keys) {
      keySet.add(k);
    }
  }

  const keys: string[] = Array.from(keySet).sort();
  const matrix: (string | number | boolean | null)[][] = [keys];

  for (const obj of arr) {
    const row: (string | number | boolean | null)[] = [];
    for (const key of keys) {
      row.push(getValue(obj, key));
    }
    matrix.push(row);
  }

  return matrix;
}

function isObject(x: any): x is object {
    return x !== null && typeof x === 'object';
}

function getKeys(arg: any): string[] {
    if (!isObject(arg)) {
      return [''];
    }

    const keys: string[] = [];
    for (const curr in arg) {
      const subKeys = getKeys(arg[curr]);
      for (const x of subKeys) {
        const key = x ? `${curr}.${x}` : curr;
        keys.push(key);
      }
    }
    return keys;
}

function getValue(obj: any, path: string): string | number | boolean | null {
    const paths: string[] = path.split('.');
    let i = 0;
    let value: any = obj;

    while (i < paths.length) {
      if (!isObject(value)) {
        break;
      }
      value = value[paths[i++]];
    }

    if (i < paths.length || isObject(value) || value === undefined) {
      return '';
    }

    return value;
}
