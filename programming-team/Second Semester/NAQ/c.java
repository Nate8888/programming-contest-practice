import java.util.*;
import java.lang.*;


class Main {
  public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	int amt = in.nextInt();
	in.nextLine();
	while(amt > 0){
		ArrayList<Double> ar = new ArrayList<>();
		int hour1, hour2, min1,min2, alpha;
		String line[] = in.nextLine().split(" ");

		hour1 = Integer.parseInt(line[0].split(":")[0]);
		min1 = Integer.parseInt(line[0].split(":")[1]);
		hour2 = Integer.parseInt(line[1].split(":")[0]);
		min2 = Integer.parseInt(line[1].split(":")[1]);
		alpha = Integer.parseInt(line[2]);

		double beginning = toMin(hour1,min1);
		double end = toMin(hour2,min2);
		System.out.println("Beginning: "+beginning);
		System.out.println("Ending: "+end);

		for(int i = 0; i < 12; i++){
			double currentHour = i; //1hr 2hr
			double t = (30 * currentHour + alpha)/11; //2.72 //
			double currentMin = 2 * t; //5.45
			ar.add(toMin(currentHour, currentMin));
			ar.add(toMin(currentHour + 12, currentMin));
		}

		if(alpha == 90){
			for(int i=0; i<12; i++) {
				double currentHour = i;
				double t = (30 * currentHour - alpha) / 11;
				double currentMin = 2 * t;
				ar.add(toMin(currentHour, currentMin));
				ar.add(toMin(currentHour + 12, currentMin));
			}
		}

		int res = 0;
		Collections.sort(ar);
		for(int i = 0; i<ar.size(); i++){
			if(i >= 1 && Math.abs(ar.get(i-1) - ar.get(i)) < 1e-8)
				continue;
			if(beginning <= ar.get(i) && ar.get(i) <= end)
				res++;
		}
		System.out.printf("%d %d %d %d %d\n",hour1,min1,hour2,min2,alpha);
		System.out.println(res);
		System.out.println(ar);
		amt--;
	}
  }
  public static double toMin(double hour, double min){
	return hour * 60 + min;
  }
}