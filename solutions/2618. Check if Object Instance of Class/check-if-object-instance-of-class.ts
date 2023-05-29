function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj === null || obj === undefined || typeof classFunction !== "function") {
        return false;
    }

    let inputObject = obj;
    if (typeof obj !== "object") {
        inputObject = Object(obj);
    }

    return inputObject instanceof classFunction;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */