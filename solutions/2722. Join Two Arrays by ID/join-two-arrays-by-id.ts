function join(arr1: any[], arr2: any[]): any[] {
    const ids = new Map<number, { [key: string]: number }>();

    for (const el of arr1) {
        ids.set(el.id, el);
    }

    for (const el of arr2) {
        ids.set(el.id, { ...ids.get(el.id), ...el});
    }

    return Array.from(ids.values()).sort((a, b) => a.id > b.id ? 1 : -1);
};
