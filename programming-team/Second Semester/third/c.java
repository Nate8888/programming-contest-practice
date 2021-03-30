import java.util.*;

class Researcher implements Comparable<Researcher> {
    int a;
    int s;
    public Researcher(int a, int s) {
        this.a = a;
        this.s = s;
    }
    
    public int compareTo(Researcher r) {
        return this.a - r.a;
    }
    
    public String toString() {
        return String.format("(a = %d, s = %d)", a, s);
    }
}

public class c{
	public static void main(String[] args) {

		ArrayList<Researcher> researchers = new ArrayList<Researcher>();

		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();
		for (int i = 0; i < n; i++) {
			int start = scan.nextInt();
			int end = scan.nextInt() + start;
			Researcher a = new Researcher(start, end);
			researchers.add(a);
		}
		researchers.sort(null);

		PriorityQueue<Integer> priority_q = new PriorityQueue<Integer>();
		int ans = 0;
		for(int i = 0; i < n; ++i){
			while(!priority_q.isEmpty() && researchers.get(i).a > priority_q.peek() + m)
				priority_q.poll();
			if(priority_q.isEmpty() || priority_q.peek() > researchers.get(i).a){
				ans += 1;
				priority_q.add(researchers.get(i).s);
			}
			else{
				priority_q.poll();
				priority_q.add(researchers.get(i).s);
			}
	}
	System.out.println(n-ans);
	}
}