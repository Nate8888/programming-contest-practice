import java.util.Scanner;

class e {
  public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	while(true){
		int rows=sc.nextInt();
		int columns=sc.nextInt();
		if(rows == 0 && columns == 0) break;
		else{		
			int matrix[][]=new int[rows][columns];
			for(int i=0; i<rows;i++)
			{            
				for(int j=0; j<columns;j++)
				{
					matrix[i][j]=sc.nextInt();
				}
			}
		System.out.println(maximalSquare(matrix));}
	}
  	}

  public static int maximalSquare(int[][] matrix) {
        int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
        int[] dp = new int[cols + 1];
        int maxsqlen = 0, prev = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                int temp = dp[j];
                if (matrix[i - 1][j - 1] == 1) {
                    dp[j] = Math.min(Math.min(dp[j - 1], prev), dp[j]) + 1;
                    maxsqlen = Math.max(maxsqlen, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return maxsqlen;
    }
}