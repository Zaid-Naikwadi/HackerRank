// Problem Statement Link: https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    static void insert(HashMap<Integer, Integer> hm, int x) {
        hm.computeIfPresent(x, (k,v) -> v + 1);
        hm.putIfAbsent(x, 1);
    }

    static void delete(HashMap<Integer, Integer> hm, int y) {
        hm.computeIfPresent(y, (k,v) -> v -1);
        hm.remove(y, 0);
    }

    static boolean checkOccurence(HashMap<Integer, Integer> hm, int z){
        return hm.containsValue(z);
    }

    // Complete the freqQuery function below.
    static List<Integer> freqQuery(List<List<Integer>> queries) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        List<Integer> ans = new ArrayList<>();

        queries.forEach(query -> {
            switch (query.get(0)) {
                case 1:
                    insert(hm, query.get(1));
                    break;
                case 2:
                    delete(hm, query.get(1));
                    break;
                case 3:
                    if (checkOccurence(hm, query.get(1))) ans.add(1);
                    else ans.add(0);
                    break;
                default:
                    break;
            }
        });

        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> ans = freqQuery(queries);

        bufferedWriter.write(
            ans.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
