package corejava.core;

public class Singleton {
    public static Singleton single_instance = null;
    private String s;

    private Singleton(){
        s = "new string test";
    }

    public static synchronized Singleton getInstance(){
        if(single_instance == null)
        single_instance = new Singleton();

        return single_instance;
    }
}
 