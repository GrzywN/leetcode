function objDiff(obj1: any, obj2: any): any {
    if (obj1 === obj2) {
        return {};
    }

    if (obj1 === null || obj2 === null) {
        return [obj1, obj2];
    }

    if (typeof obj1 !== 'object' || typeof obj2 !== 'object') {
        return [obj1, obj2];
    }

    if (Array.isArray(obj1) !== Array.isArray(obj2)) {
        return [obj1, obj2];
    }

    const output = {}

    for (const key in obj1) {
        if (key in obj2) {
            const subDiff = objDiff(obj1[key], obj2[key]);

            if (Object.keys(subDiff).length > 0) {
                output[key] = subDiff;
            }
        }
    }

    return output;
};
