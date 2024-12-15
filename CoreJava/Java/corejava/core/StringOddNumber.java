package corejava.core;

import java.util.List;

public class StringOddNumber {
    public static boolean onlyOddNumber(List<Integer> list){
        for (Integer integer : list) {
            if(integer % 2 == 0)
            return false;
        }
        return true;
    }
    public static boolean onlyOddNumberStream(List<Integer> list){
        return list.parallelStream().anyMatch(a-> a%2 != 0);
    }
}
