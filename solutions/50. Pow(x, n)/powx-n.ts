function myPow(x: number, n: number): number {
  if (n < 0) {
    return x ** n; // 💀
  }

  if (n == 0) {
    return 1;
  }

  if (n % 2 == 1) {
    return x * myPow(x, n - 1);
  }

  const w = myPow(x, n / 2);
  return w * w;
}
