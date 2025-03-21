const solution = (a, b) => {
    const result = parseInt(String(a) + String(b));
    const multiple = 2 * a * b;
    return result >= multiple ? result : multiple;
}