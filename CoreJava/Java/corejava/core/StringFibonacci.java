package corejava.core;

public class StringFibonacci {
    public static void main(String[] args){
        int count = 10;
        int a=0,b=1,c=1;
        for(int i =1; i<=count; i++){
            System.out.println(a+", ");
            a=b;
            b=c;
            c =a+b;
        }

    }
}
