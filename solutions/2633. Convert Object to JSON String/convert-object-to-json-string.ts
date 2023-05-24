function jsonStringify(object: any): string {
    let output = String(object);

    if (typeof object === "string") {
        output = `"${output}"`;

        return output;
    }

    if (Array.isArray(object)) {
        const values = [];

        for (const item of object) {
            values.push(jsonStringify(item));
        }

        output = `[${values.join(",")}]`;
        return output;
    }

    if (object === null) {
        return output;
    }

    if (typeof object === "object") {
        const pairs = [];

        for (const key in object) {
            pairs.push(`"${key}":${jsonStringify(object[key])}`);
        }

        output = `{${pairs.join(",")}}`;
    }

    return output;
}
