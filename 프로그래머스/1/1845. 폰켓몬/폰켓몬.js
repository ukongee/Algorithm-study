function solution(nums) {
    const poketmon = nums.length/2;
    const maxPoketmonType = [...new Set(nums)];
    

    return Math.min(poketmon , maxPoketmonType.length);
}