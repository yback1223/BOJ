import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class boj2587 {

	public static void main(String[] args) {
		try {
			printOutput(sortNumbers(getInputData()));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static int[] getInputData() throws IOException {
		try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
			int[] inputData = new int[5];

			for (int i = 0; i < 5; i++) {
				inputData[i] = Integer.parseInt(br.readLine().strip());
			}
			return inputData;
		}
	}

	private static String sortNumbers(int[] inputData) {
		StringBuilder result = new StringBuilder();
		MergeSort.mergeSort(inputData, 0, inputData.length - 1);

		int average = Arrays.stream(inputData).sum() / 5;
		result.append(average).append("\n").append(inputData[2]);
		return result.toString();
	}

	private static void printOutput(String result) throws IOException {
		try (BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
			bw.write(result);
			bw.newLine();
		}
	}
}

class MergeSort {
	public static void mergeSort(int[] arr, int left, int right) {
		if (left < right) {
			int mid = (left + right) / 2;

			mergeSort(arr, left, mid);
			mergeSort(arr, mid + 1, right);

			merge(arr, left, mid, right);
		}
	}

	public static void merge(int[] arr, int left, int mid, int right) {
		int[] tmpArr = new int[right - left + 1];
		int i = left;
		int j = mid + 1;
		int k = 0;

		while (i <= mid && j <= right) {
			if (arr[i] <= arr[j]) tmpArr[k++] = arr[i++];
			else tmpArr[k++] = arr[j++];
		}

		while (i <= mid) tmpArr[k++] = arr[i++];
		while (j <= right) tmpArr[k++] = arr[j++];

		for (i = left, k = 0; i <= right; i++, k++) {
			arr[i] = tmpArr[k];
		}
	}
}