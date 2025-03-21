const solution = (n) => {
    const fibo = (n, memo = {}) => {
        if (n === 0) return 0;
        if (n === 1) return 1;
        
        // 초기값 설정
        memo[0] = 0;
        memo[1] = 1;
        
        for (let i = 2; i <= n; i++) {
            memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
        }
        
        return memo[n];
    };
    return fibo(n);
};
