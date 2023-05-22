function areDeeplyEqual(o1: any, o2: any): boolean {
  if (o1 === o2) {
    return true;
  }

  if (o1 === null || o2 === null) {
    return false;
  }

  if (String(o1) !== String(o2)) {
    return false;
  }

  if (Array.isArray(o1)) {
    if (o1.length !== o2.length) {
      return false;
    }

    for (let i = 0; i < o1.length; i++) {
      if (!areDeeplyEqual(o1[i], o2[i])) {
        return false;
      }
    }

    return true;
  }

  const [o1Keys, o2Keys] = [Object.keys(o1), Object.keys(o2)];

  if (o1Keys.length !== o2Keys.length) {
    return false;
  }

  for (const key in o1) {
    if (!areDeeplyEqual(o1[key], o2[key])) {
      return false
    }
  }

  return true;
};
