function multiplyMatrix(matrixA, matrixB)
{
    var result = new Array();  
    numColsRows=2;
    for (var i = 0; i < numColsRows; i++) 
    {
        for (var j = 0; j < numColsRows; j++) 
        { 
            var matrixRow = new Array();
            var rrr = new Array();
            var resu = new Array();
            for (var k = 0; k < numColsRows; k++) 
            {
                rrr.push(parseInt(matrixA[i][k])*parseInt(matrixB[k][j]));
            }
            resu.push(parseInt(rrr[i])+parseInt(rrr[i+1]));

            result.push(resu);
        }
    }
    console.log(result);
}
var matrixA = [
  [1, 2],
  [3, 4]
];
var matrixB = [
  [1, 2],
  [5, 6]
];
multiplyMatrix(matrixA,matrixB)
