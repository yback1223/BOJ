import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ5339 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        solution();
    }

    private static void solution() throws Exception {

        sb.append("     /~\\").append("\n");
        sb.append("    ( oo|").append("\n");
        sb.append("    _\\=/_").append("\n");
        sb.append("   /  _  \\").append("\n");
        sb.append("  //|/.\\|\\\\").append("\n");
        sb.append(" ||  \\ /  ||").append("\n");
        sb.append("============").append("\n");
        sb.append("|          |").append("\n");
        sb.append("|          |").append("\n");
        sb.append("|          |").append("\n");
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
