package corejava.core;

public class StringReverse {
    public static void main(String[] args){
        String s = "Gajendra";
        char[] c =s.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (int i=c.length-1;i>=0;i--) {
            sb.append(c[i]);
        }
        System.out.println(sb.toString());
    }
}