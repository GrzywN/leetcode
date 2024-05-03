function compareVersion(version1: string, version2: string): number {
  const firstSegments = version1.split('.');
  const secondSegments = version2.split('.');
  const highestWeight = Math.max(firstSegments.length, secondSegments.length);

  for (let i = 0; i < highestWeight; i++) {
    let comparision = 0;

    if (firstSegments[i]) {
      comparision += parseInt(firstSegments[i], 10);
    }

    if (secondSegments[i]) {
      comparision -= parseInt(secondSegments[i], 10);
    }

    if (comparision != 0) {
      return Math.sign(comparision);
    }
  }

  return 0;
}
