function chunk(arr: any[], size: number): any[][] {
    const division = arr.length / size;
    let howManyChunks = Math.floor(division);
    const isNotDividedOutright = howManyChunks !== division;

    if (isNotDividedOutright) {
        howManyChunks += 1;
    }

    const output = new Array(howManyChunks);
    for (let i = 0; i < howManyChunks; i++) {
        output[i] = [];
    }

    let i = 0;
    for (const chunk of output) {
        for (let j = 0; j < size && i < arr.length; j++, i++) {
            chunk.push(arr[i]);
        }
    }

    return output;
}
