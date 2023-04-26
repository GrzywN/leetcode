function addDigits(num: number): number {
    let curr_sum = sum(num, 0)

    while(curr_sum >= 10) {
        curr_sum = sum(curr_sum, 0)
    }

    return curr_sum
}

function sum(num: number, currSum: number): number {
    if (num < 10) {
        return num
    }

    return currSum + num % 10 + sum(Math.floor(num / 10), currSum)
}
