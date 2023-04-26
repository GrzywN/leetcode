async function sleep(millis: number): Promise<boolean> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(true)
        }, millis)
    })
}


/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
