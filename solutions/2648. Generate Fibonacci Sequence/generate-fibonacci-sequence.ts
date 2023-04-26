function* fibGenerator(): Generator<number, any, number> {
    let previousNum = 0
    let currentNum = 1

    yield previousNum
    yield currentNum

    while (true) {
        yield previousNum + currentNum

        const tmp = currentNum
        currentNum = previousNum + currentNum
        previousNum = tmp
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
