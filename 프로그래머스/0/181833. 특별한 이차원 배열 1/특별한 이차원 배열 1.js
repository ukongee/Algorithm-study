const solution=(n)=>{
    const row = Array(n).fill().map(e=>Array(n).fill(0))
    for(let i=0; i<n; i++){
       
        row[i][i] = 1;
      
    }
    return row;
}