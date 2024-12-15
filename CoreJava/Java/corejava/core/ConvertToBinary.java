package corejava.core;

public class ConvertToBinary{
    public static void main(String[] args){
        int number = 100;
        String number2 = "1100100";
     String binary = convertBinary(number);
     System.out.println(binary);

     int decimal = convertDecimal(number2);
     System.out.println(decimal);
    }
    static String convertBinary(int n){
        String result ="";        
        while(n>0){
            if(n%2 == 1){
                result+="1";
            }else{
                result+="0";
            } 
            n=n/2;           
        }
        return new StringBuilder(result).reverse().toString();
    }
    static int convertDecimal(String s){
        int len=s.length(),p2 = 1,number = 0;
        for(int i=len-1;i>=0;i--){
            if(s.charAt(i) == '1'){
                number=number+p2;           
            }
            p2 = p2*2;
        }
        return number;

    }
}