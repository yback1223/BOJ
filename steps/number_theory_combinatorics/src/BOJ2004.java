import java.io.*;
import java.util.StringTokenizer;

public class BOJ2004 {
     public static void main(String[] args) throws IOException {
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
          StringTokenizer st = new StringTokenizer(br.readLine());
          long N = Long.parseLong(st.nextToken());
          long M = Long.parseLong(st.nextToken());
          long count5 = five_power_n(N) - five_power_n(N - M) - five_power_n(M);
          long count2 = two_power_n(N) - two_power_n(N - M) - two_power_n(M);
          bw.write(Math.min(count2, count5) + "\n");
          br.close();
          bw.flush();
          bw.close();
     }

     static long five_power_n(long num) {
          int count = 0;

          while(num >= 5) {
               count += num/5;
               num /= 5;
          }
          return count;
     }

     static long two_power_n(long num) {
          int count = 0;

          while(num >= 2) {
               count += num/2;
               num /= 2;
          }
          return count;
     }
}
