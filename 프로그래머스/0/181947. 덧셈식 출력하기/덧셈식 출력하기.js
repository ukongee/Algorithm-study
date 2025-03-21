const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', (line)=> {
    input = line.split(' ');
}).on('close', () =>{
   const a =  Number(input[0]);
   const b = Number(input[1]);
   const ret = a + b;
   console.log(`${a} + ${b} = ${ret}`);
});