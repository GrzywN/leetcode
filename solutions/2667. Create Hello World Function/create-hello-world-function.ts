function createHelloWorld(): () => string {
  const helloWorld = "Hello World";

  return function (): string {
    return helloWorld;
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
