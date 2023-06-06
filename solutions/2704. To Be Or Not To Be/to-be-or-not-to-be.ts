type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

const NOT_EQUAL = "Not Equal";
const EQUAL = "Equal";

function expect(val: any): ToBeOrNotToBe {
  const toBe = (val2: any) => {
    if (val === val2) {
      return true;
    } else {
      throw new Error(NOT_EQUAL);
    }
  }

  const notToBe = (val2: any) => {
    if (val !== val2) {
      return true;
    } else {
      throw new Error(EQUAL);
    }
  }

  return {
    toBe,
    notToBe
  }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
